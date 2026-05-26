san = int(input("Сан енгізіңіз: "))

fact = 1
i = 1

while i <= san:
    fact *= i
    i += 1

print("Факториал:", fact)