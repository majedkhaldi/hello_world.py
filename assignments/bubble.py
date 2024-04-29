arr = [100,4,6,7,2,1,5,90,15,-19]
for i in range (len(arr)):
    for j in range (len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print (arr)
