from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

model = ChatCohere(model="command-a-03-2025")

# Schema
class Review(BaseModel):
    summary: str
    sentiment: str

structured_output = model.with_structured_output(Review)

review = structured_output.invoke("""
The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove.
Also, the UI looks outdated compared to other brands.
Hoping for a software update to fix this.
""")

print(review)