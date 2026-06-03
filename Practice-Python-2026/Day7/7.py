file = open("text.txt", "r", encoding="utf-8")

content = file.read()

lines = content.split("\n")
words = content.split()

print("Жолдар саны:", len(lines))
print("Сөздер саны:", len(words))

file.close()