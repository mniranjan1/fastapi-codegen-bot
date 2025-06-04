from fastapi import FastAPI

app = FastAPI(
    title="Python Code Generator", root_path="/api", docs_url="/", version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}