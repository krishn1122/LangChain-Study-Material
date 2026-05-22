from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere(model='command-a-03-2025')
messages = [
    SystemMessage(content="You are a helpful assistant. Answer all my questions to the best of your ability.")
]

while True:
    user = input("You: ")
    messages.append(HumanMessage(content=user))
    if user.lower() == 'exit':
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: ", response.content)
print(messages)