from fastapi import FastAPI
from api.routes import code_generation
import uvicorn
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv() # Load environment variables from .env file

app = FastAPI(
    title="Python Code Generator",
    root_path="/api",
    docs_url="/docs",
    version="1.0.0",
) # Create a FastAPI app

app.include_router(code_generation.router, prefix="/api", tags=["code-generation"]) # Include the code generation router


@app.get("/")
def read_root():
    return {"message": "Welcome to the Python Code Generator API"}


if __name__ == "__main__":
    uvicorn.run(
        app="main:app", # Run the app
        host="0.0.0.0", # Run the app on all interfaces
        port=8000, # Run the app on port 8000
    )

