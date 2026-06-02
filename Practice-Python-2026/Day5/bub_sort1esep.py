arr = [5, 2, 9, 1, 6] 
n = len(arr) 
for i in range(n): 
    for j in range(n - i - 1): 
        if arr[j] > arr[j + 1]: 
            arr[j], arr[j + 1] = arr[j + 1], arr[j] 
            
print(arr)