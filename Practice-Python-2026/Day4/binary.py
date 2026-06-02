def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = [3, 8, 12, 18, 25, 30]
target = 18

result = binary_search(numbers, target)

print("Нәтиже индексі:", result)