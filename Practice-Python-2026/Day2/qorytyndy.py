name = input("Атыңыз: ")
age = int(input("Жасыңыз: "))
number = int(input("Сан енгізіңіз: "))

print("\nСәлем,", name)
print("Жасыңыз:", age)

# Жұп немесе тақ
if number % 2 == 0:
    print("Сан жұп")
else:
    print("Сан тақ")

# for циклі
summa = 0

for i in range(1, 6):
    summa += i

print("1-ден 5-ке дейінгі қосынды:", summa)

# while циклі
count = 1

while count <= 3:
    print("Қайталау:", count)
    count += 1
