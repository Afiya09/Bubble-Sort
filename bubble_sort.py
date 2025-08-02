#Bubble Sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

#driver code
arr=[64,34,11,24,90,7]  

#function call
bubble_sort(arr)
for i in range(len (arr)):
    print(arr[i],end=" ")
    