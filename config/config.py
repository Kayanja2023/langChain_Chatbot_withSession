from dotenv import load_dotenv
import os

def load_api_keys():
    load_dotenv()  # loads from .env
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing OpenAI API Key in .env")
    os.environ["OPENAI_API_KEY"] = api_key  # needed for LangChain/OpenAI
