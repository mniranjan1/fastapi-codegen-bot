from pydantic import BaseModel


# Request schema for code generation
class CodeGenerationRequest(BaseModel):
    prompt: str


# Response schema for code generation
class CodeGenerationResponse(BaseModel):
    code: str
