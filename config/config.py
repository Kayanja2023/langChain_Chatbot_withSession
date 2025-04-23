from dotenv import load_dotenv
import os

def load_api_keys():
    """
    Loads and validates the OpenAI API key from environment variables.

    This function:
    - Loads variables from a `.env` file using `python-dotenv`
    - Retrieves the value of `OPENAI_API_KEY`
    - Ensures the key is present, raising a ValueError if not
    - Explicitly sets the key in `os.environ` for SDK compatibility
    """

    # Load environment variables from .env into the runtime environment
    load_dotenv()

    # Retrieve the OpenAI API key from loaded environment
    api_key = os.getenv("OPENAI_API_KEY")

    # Validate that the key exists, else raise a critical error
    if not api_key:
        raise ValueError("Missing OpenAI API Key in .env")

    # Ensure the variable is accessible for LangChain/OpenAI integrations
    os.environ["OPENAI_API_KEY"] = api_key
