arr = [10, 3, 7, 1, 9] 
for i in range(len(arr)): 
    min_i = i 
    for j in range(i + 1, len(arr)): 
        if arr[j] < arr[min_i]: 
            min_i = j 
            arr[i], arr[min_i] = arr[min_i], arr[i]
            
print("Сұрыпталған массив:", arr) 
print("Ең кіші элемент:", arr[0])