from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatCohere(model='command-a-03-2025')

prompt=PromptTemplate(
    template="Write 5 interesting facts about: {Superhero}",
    input_variables=['Superhero']
)
parser=StrOutputParser()
chain= prompt | model | parser
result=chain.invoke({'Superhero': 'Batman'})
print(result)

chain.get_graph().print_ascii()