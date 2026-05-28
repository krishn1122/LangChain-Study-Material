from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatCohere(model='command-a-03-2025')

schema = [
    ResponseSchema(
        name="fact_1",
        description="Fact 1 about the topic"
    ),
    ResponseSchema(
        name="fact_2",
        description="Fact 2 about the topic"
    ),
    ResponseSchema(
        name="fact_3",
        description="Fact 3 about the topic"
    )
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="""
Give me 3 facts about the following topic: {topic}

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

prompt = template.invoke({
    'topic': 'The impact of AI on society'
})

result = model.invoke(prompt)

print(result.content)

parsed_output = parser.parse(result.content)

print(parsed_output)