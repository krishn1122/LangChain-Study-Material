from transformers import pipeline

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

result = pipe("Write a detailed report about the following topic: The impact of AI on society")

print(result)