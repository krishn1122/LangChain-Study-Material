from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatCohere(model='command-a-03-2025')

text = """
Absolutely incredible. The balance of flavors caught me off guard in the best way possible — every bite felt thoughtfully crafted.
I came in curious and left planning my next visit just to order it again. If this is the restaurant’s new direction, they’re onto something special.
— Aarav Mehta, food blogger
"""

# Pydantic schema
class FeedbackSentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="The sentiment of the feedback"
    )

# Parser
parser = PydanticOutputParser(
    pydantic_object=FeedbackSentiment
)

# Classification prompt
prompt1 = PromptTemplate(
    template="""
Classify the following feedback text into either
'positive' or 'negative'.

{feedback}

{format_instructions}
""",
    input_variables=['feedback'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

# Classifier chain
classifier = prompt1 | model | parser

# Positive response prompt
positive_prompt = PromptTemplate(
    template="""
Write an appropriate response to this positive feedback:

{feedback}
""",
    input_variables=['feedback']
)

# Negative response prompt
negative_prompt = PromptTemplate(
    template="""
Write an appropriate response to this negative feedback:

{feedback}
""",
    input_variables=['feedback']
)

# Branch logic
branch = RunnableBranch(
    (
        lambda x: x.sentiment == "positive",
        positive_prompt | model
    ),
    (
        lambda x: x.sentiment == "negative",
        negative_prompt | model
    ),
    RunnableLambda(lambda x: "Invalid sentiment")
)

# Full chain
chain = classifier | branch

# Invoke
result = chain.invoke({
    "feedback": text
})

print(result.content)

chain.get_graph().print_ascii()