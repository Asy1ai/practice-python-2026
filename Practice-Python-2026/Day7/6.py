try:
    file = open("text.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    file = open("text.txt", "w", encoding="utf-8")
    file.write("Бұл файл автоматты түрде құрылды.")
    file.close()

    file = open("text.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
    file.close()