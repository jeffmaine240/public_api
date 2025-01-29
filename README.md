# HNG12 Backend Stage 0 - Public API

## Description
This project implements a public API that returns basic information in JSON format. The API responds with the following information:

- The registered email address (used to register on the HNG12 Slack workspace).
- The current datetime in ISO 8601 format (UTC).
- The GitHub URL of the project’s codebase.

This is the Stage 0 task for the Backend internship at HNG12, developed using **FastAPI**.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- `pip` for managing dependencies

### Install Dependencies
To run this project locally, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/jeffmaine240/public_api.git
   cd public_api

2. Create a virtual environment (recommended):
    ```bash
   python3 -m venv venv
    source venv/bin/activate  

3. Install the project dependencies:
     ```bash
     pip install -r requirements.txt


### Run Locally
4. To run the FastAPI app locally:

    * If you have fastapi-cli installed:
         ```bash
         fastapi dev src/
    or 
    * Use uvicorn directly:
    ```bash
         uvicorn src:app --reload

This will start the app at http://127.0.0.1:8000 (default). The --reload flag ensures the server reloads automatically when you make changes to the code.

### Testing Locally
Once the server is running, open your browser and visit through a GET request:

    http://127.0.0.1:8000/api/v1/public/


You should receive the following JSON response and response status of (200 ok):

    {
        "email": "oyeniyij43@gmail.com",
        "current_datetime": "2025-01-29T14:40:20.094887Z",
        "github_url": "https://github.com/jeffmaine240/public_api"
    }