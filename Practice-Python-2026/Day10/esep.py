tasks = []

# 1. Тапсырма қосу
def add_task():
    task = input("Тапсырма енгізіңіз: ")
    tasks.append(task)
    print("✔️ Тапсырма қосылды!")

# 2. Тапсырмаларды көру
def show_tasks():
    if not tasks:
        print("❌ Тапсырма жоқ!")
    else:
        print("\n📋 Тапсырмалар тізімі:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

# 3. Тапсырма өшіру
def delete_task():
    try:
        show_tasks()
        num = int(input("Өшіру нөмірін енгізіңіз: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"✔️ Өшірілді: {removed}")
        else:
            print("❌ Қате нөмір!")
    except ValueError:
        print("❌ Тек сан енгізіңіз!")

# 4. Тапсырмаларды сұрыптау (алгоритм)
def sort_tasks():
    tasks.sort()
    print("✔️ Тапсырмалар сұрыпталды (A-Z)")

# 5. Ең ұзын тапсырманы табу (алгоритмдік ойлау)
def longest_task():
    if not tasks:
        print("❌ Тапсырма жоқ")
    else:
        longest = max(tasks, key=len)
        print("📌 Ең ұзын тапсырма:", longest)

# 6. Рекурсия мысалы (факториал)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def show_factorial():
    try:
        n = int(input("Сан енгізіңіз: "))
        print("Факториал:", factorial(n))
    except:
        print("❌ Қате енгізу!")

# 7. Негізгі меню
def menu():
    while True:
        print("\n===== PYTHON ЖОБА МӘЗІРІ =====")
        print("1. Тапсырма қосу")
        print("2. Тапсырмаларды көру")
        print("3. Тапсырма өшіру")
        print("4. Сұрыптау")
        print("5. Ең ұзын тапсырма")
        print("6. Факториал (рекурсия)")
        print("7. Шығу")

        choice = input("Таңдаңыз: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            sort_tasks()
        elif choice == "5":
            longest_task()
        elif choice == "6":
            show_factorial()
        elif choice == "7":
            print("Бағдарлама аяқталды!")
            break
        else:
            print("❌ Қате таңдау!")

menu()