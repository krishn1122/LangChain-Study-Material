from langchain_cohere import ChatCohere
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

model = ChatCohere(model='command-a-03-2025')

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt=18,description="The person's age")
    city: str = Field(description="The person's city")

parser = PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Give me the name, age, and city of a fictional {place} person \n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)
chain= template | model | parser
result=chain.invoke({'place': 'Indian'})
print(result)
# prompt=template.format(place="India")
# print(prompt)
# model_response=model.invoke(prompt)
# result=parser.parse(model_response.content)
#print(result)