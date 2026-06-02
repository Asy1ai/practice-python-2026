def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [5, 12, 7, 20, 9]
target = 7

result = linear_search(numbers, target)

print("Нәтиже индексі:", result)