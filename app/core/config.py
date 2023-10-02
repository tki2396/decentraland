from os import environ
from dotenv import load_dotenv
load_dotenv()

MONGODB_URI=environ.get("MONGODB_URI")
OPENAI_API_KEY = environ.get("OPENAI_API_KEY")