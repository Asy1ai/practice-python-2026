def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_avg(numbers):
    return sum(numbers) / len(numbers)

nums = [12, 45, 7, 89, 23]

print("Max:", find_max(nums))
print("Min:", find_min(nums))
print("Avg:", find_avg(nums))