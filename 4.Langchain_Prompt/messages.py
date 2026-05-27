from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_cohere import ChatCohere
from dotenv import load_dotenv

load_dotenv()
model=ChatCohere(model="command-a-03-2025")
messages = [
    SystemMessage(content="You are a helpful assistant. Answer all my questions to the best of your ability."),
    HumanMessage(content="What is the range of temperature parameter in any LLM?")
]

respomse = model.invoke(messages)
messages.append(AIMessage(content=respomse.content))
print(messages)