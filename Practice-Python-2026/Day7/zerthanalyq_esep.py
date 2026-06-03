# 1. Жолдық деректерді өңдеу

text = input("Мәтін енгізіңіз: ")

print("Үлкен әріптермен:", text.upper())
print("Кіші әріптермен:", text.lower())
print("Сөздер саны:", len(text.split()))

# 2. Рекурсивті функция (факториал)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Сан енгізіңіз: "))
print("Факториал:", factorial(number))

# 3. Файлдан деректерді оқу

file = open("text.txt", "r", encoding="utf-8")
content = file.read()
file.close()

print("\nФайл мазмұны:")
print(content)

# 4. Нәтижелерді талдау

lines = content.split("\n")
words = content.split()

print("\nЖолдар саны:", len(lines))
print("Сөздер саны:", len(words))

# 5. Нәтижені жаңа файлға жазу

new_file = open("result.txt", "w", encoding="utf-8")
new_file.write(content.upper())
new_file.close()

print("Өңделген мәтін result.txt файлына сақталды.")