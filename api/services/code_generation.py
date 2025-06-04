import os
from api.prompts.code_generation import CODE_GENERATION_PROMPT
from api.services import client


def generate_python_code(prompt: str) -> str:
    """
    Generate Python code based on the provided prompt using OpenAI's API.

    Args:
        prompt (str): The user's prompt describing the code to generate.

    Returns:
        str: The generated Python code.

    Raises:
        RuntimeError: If the OpenAI API call fails.
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL"), # Use the model specified in the environment variables
            messages=[
                {"role": "system", "content": CODE_GENERATION_PROMPT}, # Use the prompt specified in the environment variables
                {"role": "user", "content": prompt}, # Use the prompt provided by the user
            ],
            temperature=float(os.getenv("OPENAI_TEMPERATURE")), # Use the temperature specified in the environment variables
            max_tokens=int(os.getenv("OPENAI_MAX_TOKENS")), # Use the max tokens specified in the environment variables
        )
        return response.choices[0].message.content # Return the generated code
    except Exception as e:
        raise RuntimeError(f"OpenAI API call failed: {e}")
