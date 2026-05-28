from langchain_cohere import ChatCohere
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv, parser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatCohere(model='command-a-03-2025')

Parser = JsonOutputParser()

template=PromptTemplate(
    template="Give me the name, age, and occupation of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': Parser.get_format_instructions()}
)
prompt=template.format()
print(prompt)

model_response=model.invoke(prompt)
print(model_response)

parsed_output=Parser.parse(model_response.content)
print(parsed_output)
print(type(parsed_output))