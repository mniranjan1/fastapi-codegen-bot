# fastapi-codegen-bot
A FastAPI-based Backend for Python Code Generation that responds to natural language
prompts and returns corresponding Python code snippets.

# Project Setup
## 1. Clone the repository
```bash
git clone https://github.com/mniranjan1/fastapi-codegen-bot.git
cd fastapi-codegen-bot
```
## 2. Set the environmental variables:
Copy the `.env.example` file to `.env` and update it with the necessary values.

## Running Locally
### 1. Install Required Dependencies: Python, uv
- Python 3.8+
- uv 
    ```bash
    curl -Ls https://astral.sh/uv/install.sh | sh
    ````
### 2. Create and activate a virtual environment
```bash
uv venv .venv
source .venv/bin/activate
```
### 3. Install dependencies using `uv`
```bash
uv pip install -r requirements.txt
```
### 4. Run the FastAPI app
```bash
python3 main.py
```
### 5. Open in browser
- App: http://localhost:8000
- Docs: http://localhost:8000/docs

## Running with Docker
### 1. Build the Docker image
```bash
docker build -t codegen-bot .
```
### 2. Run the container
```bash
docker run -p 8000:8000 -d codegen-bot
```
### 3. Open in browser
- App: http://localhost:8000
- Docs: http://localhost:8000/docs

## How to Use the API

Once the FastAPI server is running (locally or in Docker), you can interact with the API to generate Python code based on text prompts.

### Endpoint

**POST** `/generate`

- **Description**: Generates Python code from a given natural language prompt.

### Request Body (JSON)

```json
{
  "prompt": "create a python program for sum of 2 numbers"
}
```

### Response (JSON)

```json
{
  "code": "a = float(input(\"Enter the first number: \"))\nb = float(input(\"Enter the second number: \"))\nprint(\"The sum is:\", a + b)"
}
```

### Example: Using `curl`

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "create a python program for sum of 2 numbers"}'
```

## Interactive Documentation

You can also test the API directly in your browser using the built-in documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Examples

A few example prompts and their corresponding responses are provided in the `examples/` folder, stored in the `responses.json` file.

## Libraries Used

- FastAPI – For building the API

- Uvicorn – ASGI server for serving FastAPI

- Pydantic – Data validation and settings management

- OpenAI – For interacting with OpenAI’s API

- python-dotenv – For loading environment variables from .env

- uv – Fast Python package manager


