file = open("text.txt", "r", encoding="utf-8")

content = file.read()

file.close()

new_content = content.upper()

new_file = open("new_text.txt", "w", encoding="utf-8")

new_file.write(new_content)

new_file.close()

print("Мәтін жаңа файлға жазылды.")