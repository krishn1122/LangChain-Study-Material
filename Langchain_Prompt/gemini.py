from collections import Counter

document = """
Python is easy and Python is powerful.
Many people learn Python because Python is beginner friendly.
"""

document = document.lower()  # Convert to lowercase for uniformity

for ch in '.,!?;':
    document = document.replace(ch, '')  # Remove punctuation
result=[]
k=int(input("Enter the number of most common words to display: "))
word_counts = Counter(document.split())  # Count the frequency of each word

for word, count in word_counts.items():
    if count == k:
        result.append(word)

print(f"Words that appear exactly {k} times: {result}")

