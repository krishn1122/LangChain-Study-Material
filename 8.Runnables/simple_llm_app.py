from langchain_cohere import ChatCohere
from langchain_cohere.llms import Cohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize model
model = ChatCohere(model='command-a-03-2025')
# Create prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the following question:\n{question}"
)

# User input
question = input("What topic would you like to ask about? ")

# Format prompt
formatted_prompt = prompt.format(question=question)

# Generate response
answer = model.invoke(formatted_prompt)

# Print response
print("\nAI Response:\n")
print(answer.content)
