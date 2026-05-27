from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatCohere(model="command-a-03-2025")


class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review in a list"
    )

    summary: str = Field(
        description="A brief summary of the review"
    )

    sentiment: str = Field(
        description="Return ONLY one of these values: positive, negative, neutral"
    )

    pros: list[str] = Field(
        default_factory=list,
        description="Write down all the pros inside a list"
    )

    cons: list[str] = Field(
        default_factory=list,
        description="Write down all the cons inside a list"
    )

    name: str = Field(
        default="",
        description="Write the name of the reviewer"
    )


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!
The Snapdragon 8 Gen 3 processor makes everything lightning fast.

Review by KJ Styles
""")

print(result.name)