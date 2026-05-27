from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
load_dotenv()
model = ChatCohere(model="command-a-03-2025")
# Define a chat prompt template with a messages placeholder
chat_prompt = ChatPromptTemplate([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{query}")
])

chat_history = []
with open("chat_history.txt", "r") as file:
    text = file.readlines()
    chat_history.extend(text)

prompt = chat_prompt.invoke({"history": chat_history, "query": "What is the Status of my refund?"})
model_response = model.invoke(prompt)
print("Bot: ", model_response.content)
