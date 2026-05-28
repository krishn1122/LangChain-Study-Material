from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

chain= template1 | model | parser | template2 | model | parser

result=chain.invoke({"topic": "The impact of AI on society"})
print(result)