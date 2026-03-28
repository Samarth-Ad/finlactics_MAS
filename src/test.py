from groq import Groq
from dotenv import load_dotenv
from os import getenv
load_dotenv()

client = Groq(api_key=getenv("GROQ_API_KEY"))

print(client.models.list())