from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatCohere(model='command-a-03-2025')

prompt1=PromptTemplate(
    template="Write a detailed report about: {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Summarize the following report in 5 bullet points: {report}",
    input_variables=['report']
)
parser=StrOutputParser()
chain= prompt1 | model | parser | prompt2 | model | parser
result=chain.invoke({'topic': 'The history of the internet'})
print(result)
chain.get_graph().print_ascii() 