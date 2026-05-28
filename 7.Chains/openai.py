from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-2024-08-06')
response = model.invoke("What are the benefits of using LangChain for building applications?")
print(response)
