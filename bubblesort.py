#bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
            elif swapped==False:
                break

#driver code
arr=[64,34,25,12,22,11,90]

bubble_sort(arr)
print("Sorted Array :")
for i in range(len(arr)):
    print(arr[i],end=" ")

