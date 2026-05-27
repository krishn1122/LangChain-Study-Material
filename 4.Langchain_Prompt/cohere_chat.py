from langchain_cohere import ChatCohere
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
model=ChatCohere(model='command-a-03-2025')
template = ChatPromptTemplate.from_messages([
    ("system", "You are a Senior Software Engineer. Your task is to share all insights "
               "regarding code-level understanding. You will assist in code development, "
               "integration, and debugging."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])

chat_history=[]

while True:
    user = input("You: ")
    
    if user.lower() == 'exit':
        print("Goodbye!")
        break

    # Build the prompt by injecting history + current input
    prompt = template.invoke({
        "chat_history": chat_history,
        "user_input": user
    })

    result = model.invoke(prompt)

    # Store as proper message objects for history
    chat_history.append(HumanMessage(content=user))
    chat_history.append(AIMessage(content=result.content))

    print("Bot:", result.content)
