file = open("text.txt", "r", encoding="utf-8")

content = file.read()

print(content)

file.close()