from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 

load_dotenv()

chat=ChatOpenAI(model='gpt-4o')
response=chat.invoke("Who is the current preident of India?")
print(response.content)