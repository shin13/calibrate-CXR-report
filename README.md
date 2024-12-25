# CXR Report Calibration

This project provides a tool to calibrate Chest X-Ray (CXR) reports based on corresponding CT reports using a FastAPI backend and a Streamlit frontend.

## Project Structure

- `main.py`: Main entry point, starts the FastAPI server.
- `app/models/report.py`: Defines the data models for the input and output reports.
- `app/app.py`: Contains the Streamlit app for user interaction and communication with the FastAPI server.

## Setup Instructions

### Prerequisites

- Python 3.7+
- FastAPI
- Streamlit
- Requests
- Requests-Toolbelt

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/shin13/calibrate-CXR-report.git
    cd calibrate-CXR-report
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the local LLM server using LM Studio. 
    Modify the `CHATGPT_API_ENDPOINT`. Make sure to use the `POST /v1/chat/completions` endpoint.

2. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload --port 7890
    ```

3. Start the Streamlit app:
    ```sh
    streamlit run app/app.py
    ```

## Usage

1. Open the Streamlit app in your browser. It should be running at `http://localhost:8501`.
2. Select an example report or enter your own CXR and CT reports.
3. Click the "Submit" button to calibrate the CXR report based on the CT report.
4. The calibrated CXR report will be displayed below the submit button.

## Example Reports

The app includes several example pairs of CXR and CT reports to demonstrate the calibration process. You can select any of these examples from the dropdown menu in the Streamlit app.

## Troubleshooting

- Ensure that both the FastAPI server and the Streamlit app are running.
- Check the console for any error messages if the calibration process fails.
- Verify that the input reports are correctly formatted.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
