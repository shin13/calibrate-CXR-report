# CXR Report Calibration

This project provides a tool to calibrate Chest X-Ray (CXR) reports based on their corresponding CT reports. It utilizes a FastAPI backend for server-side processing and a Streamlit frontend for user interaction.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Example Reports](#example-reports)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)

## Project Structure

```bash
.
├── LICENSE
├── LM Stidio format.json   # Template
├── README.md
├── app
│   ├── app.py              # Streamlit app for user 
interaction
│   ├── config.py
│   ├── middleware
│   │   └── exception.py
│   └── models
│       └── report.py       # Data models for input
├── main.py                 # Main entry point for starting the FastAPI server
└── requirements.txt
```

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following software installed:

- Python 3.7+
- FastAPI
- Streamlit
- Requests
- Requests-Toolbelt
- LM Studio (I use the model `llama-3.2-3b-instruct`, you can choose yuor own model)

### Installation

To install the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/shin13/calibrate-CXR-report.git
    cd calibrate-CXR-report
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

To run the application:

1. **Start the local LLM server** using LM Studio with the specified model. Make sure to configure the `CHATGPT_API_ENDPOINT` correctly, using the `POST /v1/chat/completions` endpoint.

2. **Start the FastAPI server**:
    ```sh
    uvicorn app.main:app --reload --port 7890
    ```

3. **Start the Streamlit app**:
    ```sh
    streamlit run app/app.py
    ```

## Usage

1. Open the Streamlit app in your browser at `http://localhost:8501`.
2. Select an example report or enter your own CXR and CT reports in the provided input fields.
3. Click the "Submit" button to calibrate the CXR report based on the CT report.
4. The calibrated CXR report will appear below the submit button.

## Example Reports

The app includes several example pairs of CXR and CT reports. You can access these examples via the dropdown menu in the Streamlit app for demonstration purposes.

## Troubleshooting

If you encounter issues, consider the following steps:

- Ensure both the FastAPI server and the Streamlit app are running.
- Check the terminal or console for any error messages if the calibration fails.
- Confirm that the input reports are properly formatted.

## License

This project is licensed under the MIT License. For details, see the [LICENSE](LICENSE) file.

## Contributing

We welcome contributions! If you have suggestions for improvements or want to report bugs, please open an issue or submit a pull request.