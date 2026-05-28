from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere
from dotenv import load_dotenv
load_dotenv()
model = ChatCohere(model="command-a-03-2025")
chat_prompt = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("user", "Explain the concept of {concept} in simple terms."),  
])
while True:
    domain = input("Enter the domain (or 'exit' to quit): ")
    if domain.lower() == 'exit':
        break
    concept = input("Enter the concept: ")
    prompt = chat_prompt.invoke({"domain": domain, "concept": concept})
    response = model.invoke(prompt)
    print("Bot: ", response.content)

print(prompt)