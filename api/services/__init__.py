from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Create a client for the OpenAI API