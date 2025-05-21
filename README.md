# Auto Test Scenario Generator

## This project provides a system that can can generate test scenario for test cases from a SRS document

## Features

- Generate test scenario in CSV format
- Designed for extensibility and API integration (FastAPI-ready)
- Dockerization enabled

---

## Project Structure

```
auto-test-scenario/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── .env
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── logger.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_inference.py
│   │   ├── json_to_csv.py
│   └── data/
│   │   ├── Sample_SRS.pdf
│   └── result/
│   │   ├── Sample_SRS.csv
│   └── models/
│       ├── __init__.py
│       └── schemas.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Installation

#### 1. Clone the Repository

```bash
git https://github.com/AnisH521/auto-test-scenario-app.git
cd auto-test-scenario-app
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file within `app/.env` and put you API Key within it

```bash
# GEMINI_API_KEY
GEMINI_API_KEY=************************
```

#### Running the Application

Start the API server:

```bash
uvicorn app.main:app --reload
```

#### Docker Options

Built the image

```bash
docker build -t name-of-docker-image .
```

Run the Container

```bash
docker run -p 8000:8000 name-of-docker-image
```

The API will be available at http://localhost:8000, and the interactive API documentation at http://localhost:8000/docs.

## API Endpoints

### Generate Test Scenario

```
POST api/automation-test-scenario
```

Upload SRS document in pdf format and get the result of test scenarios in csv format.

## Response Format

```json
{
  "conversion": "success",
  "file_name": "Sample_SRS.pdf"
}
```

## License

[MIT](LICENSE)

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
