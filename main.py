import os
from load_dotenv import load_dotenv
import logging
from typing import Union
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from requests import post
from requests.exceptions import RequestException
from app.middleware.exception import exception_message
from app.models.report import ReportInput

# Load environment variables from a .env file
load_dotenv()

CHATGPT_API_ENDPOINT = os.getenv("CHATGPT_API_ENDPOINT")

# Setup logging
logging.basicConfig(level=logging.ERROR)
system_logger = logging.getLogger(__name__)

app = FastAPI()

# CORS middleware setup to allow requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post("/calibrate_report/", response_model=str)
async def calibrate_report(report_input: ReportInput = Form(...)) -> str:
    """Endpoint to calibrate the CXR report based on the CT report."""
    input_text = generate_prompt(report_input.cxr_report, report_input.ct_report)
    calibrated_report = send_request(input_text)
    calibrated_report_text = calibrated_report['choices'][0]['message']['content']
    # Replace newlines with spaces in the calibrated report
    calibrated_report_text = calibrated_report_text.replace("\n", " ")
    return calibrated_report_text

def send_request(input_text: str) -> Union[dict, str]:
    """Send a request to the ChatGPT API with the given input text."""
    url = CHATGPT_API_ENDPOINT
    payload = input_text
    try:
        response = post(url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            system_logger.error(f"Failed to send request to ChatGPT: {response.text}")
    except RequestException as e:
        system_logger.error(exception_message(e))

def generate_prompt(cxr_report: str, ct_report: str) -> str:
    """Generate the input text for the ChatGPT API based on the original CXR and CT reports."""
    system_prompt = (
        "You are a seasoned radiologist proficient in interpreting chest X-ray (CXR) and CT images. "
        "Your goal is to produce an X-ray style report that remains concise, objective, and aligned with typical CXR reporting conventions."
    )
    user_prompt = (
        "Below are two reports for the same patient: "
        f"[Original CXR Report] {cxr_report}"
        f"[Original CT Report] {ct_report}"
        "Your tasks: "
        "- Merge the findings into one concise CXR report without mentioning CT. "
        "- Enhance the CXR report while ensuring: "
        "  - Use typical CXR language and structure. Do not use 'patient' as a subject. "
        "  - Incorporate relevant findings from the CT report as if they are CXR findings. "
        "  - When referring to a location or size, provide an accurate description. Exclude any findings not visible on a CXR. "
        "  - Check both reports for mentions of further investigation. If any are found, conclude with a similar statement. "
        "  - Use short sentences to produce ONLY CXR findings. Do not indicate that findings are from the CT report. "
        "  - Avoid titles or additional information. Do not format the text. "
        "  - Do not extend the content in your response."
    )
    input_text = {
        "model": os.getenv("MODEL"),
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "temperature": 0,
        "top_p": 0.15,
        "max_tokens": 150,
        "stream": False
    }
    return input_text


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=7890,
        reload=True,
    )