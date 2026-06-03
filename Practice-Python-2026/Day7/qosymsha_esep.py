def palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])

word = input("Сөз енгізіңіз: ")

if palindrome(word):
    print("Палиндром")
else:
    print("Палиндром емес")