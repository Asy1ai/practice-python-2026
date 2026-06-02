def is_palindrome_sentence(sentence):
    clean = sentence.replace(" ", "").lower()
    return clean == clean[::-1]

text = "A man a plan a canal Panama"

if is_palindrome_sentence(text):
    print("Палиндром")
else:
    print("Палиндром емес")