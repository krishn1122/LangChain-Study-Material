from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
document = ["The capital of France is Paris.",
            "The capital of India is New Delhi.",
            "The capital of the United States is Washington D.C."]
result = embeddings.embed_documents(document)
print(str(result))