def insertionSort(arr):
       
    for i in range(1, 10):         
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 

arr=[10,9,3,4,5,6,7,2,3,4]
insertionSort(arr)
print(arr)