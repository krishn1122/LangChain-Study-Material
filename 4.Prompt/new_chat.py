import cohere

co = cohere.ClientV2(api_key="cohere_tma8vq27noMXz4wPUPagTS0r7oBunhdwzY0lPh1J3QwzoK")

res = co.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": "Write a title for a blog post about API design. Only output the title text.",
        }
    ],
)

print(res.message.content[0].text)
# "The Ultimate Guide to API Design: Best Practices for Building Robust and Scalable APIs"
