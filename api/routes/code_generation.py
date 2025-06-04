from fastapi import APIRouter, HTTPException
from api.schemas.code_generation import CodeGenerationRequest, CodeGenerationResponse
from api.services.code_generation import generate_python_code

router = APIRouter() # Create a router for the code generation API

# Generate code based on the prompt
@router.post("/generate")
async def generate_code(request: CodeGenerationRequest):
    """
    Generate Python code based on the provided prompt.

    Args:
        request (CodeGenerationRequest): The request object containing the prompt for code generation.

    Returns:
        CodeGenerationResponse: The response object containing the generated code.

    Raises:
        HTTPException: If the code generation fails or if the prompt is empty.
    """
    try:
        if not request.prompt.strip():
            return {"error": "Prompt cannot be empty"}

        generated_code = generate_python_code(request.prompt) # Generate code using the OpenAI API

        return CodeGenerationResponse(code=generated_code)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Code generation failed: {str(e)}")
