from langchain_gemini import ChatGemini
from dotenv import load_dotenv

load_dotenv()
model = ChatGemini(model="gemini-2.0-pro")
response = model.invoke("What is the capital of India?")
print(response.content)