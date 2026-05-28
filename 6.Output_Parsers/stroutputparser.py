from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatCohere(model='command-a-03-2025')

# 1st prompt -> Detailed Report

template1 = PromptTemplate(
    template="Write a detailed report about the following topic: {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text.\n{text}",
    input_variables=["text"]
)

prompt1 = template1.format(topic="The impact of AI on society")
result1 = model.invoke(prompt1)

prompt2 = template2.format(text=result1.content)
result2 = model.invoke(prompt2)

print(result2.content)