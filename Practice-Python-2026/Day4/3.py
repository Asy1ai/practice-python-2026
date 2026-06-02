def is_palindrome(word):
    return word == word[::-1]

text = "kazak"

if is_palindrome(text):
    print("Палиндром")
else:
    print("Палиндром емес")