from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
document = ["The capital of France is Paris.", "The capital of India is New Delhi.", "The capital of the United States is Washington D.C."]
result = embeddings.embed_documents(document)
print(str(result))