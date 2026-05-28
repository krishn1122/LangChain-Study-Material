from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()
model1 = ChatCohere(model='command-a-03-2025')
model2 = ChatCohere(model='command-a-plus-05-2026')
model3 = ChatCohere(model='c4ai-aya-expanse-32b')

prompt1=PromptTemplate(
    template="Generate short and simple notes from the following text: \n {text}",
    input_variables=['text']
)
prompt2=PromptTemplate(
    template="Generate a 5 quiz questions on the: \n {text}",
    input_variables=['text']
)
prompt3=PromptTemplate(
    template="Merge the provided notes and quiz questions into a single document: \n -> {notes} and {quiz}",
    input_variables=['notes', 'quiz']
)

parser=StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text="""Python decorators allow you to modify or extend the behavior of functions and methods without changing their actual code. When you use a Python decorator, you wrap a function with another function, which takes the original function as an argument and returns its modified version. This technique provides a simple way to implement higher-order functions in Python, enhancing code reusability and readability.

By the end of this tutorial, you’ll understand that:

Practical use cases for decorators include logging, enforcing access control, caching results, and measuring execution time.
Custom decorators are written by defining a function that takes another function as an argument, defines a nested wrapper function, and returns the wrapper.
Multiple decorators can be applied to a single function by stacking them before the function definition.
The order of decorators impacts the final output since each decorator wraps the next, influencing the behavior of the decorated function.   """

result = chain.invoke({'text': text})
# print(result)

chain.get_graph().print_ascii()
