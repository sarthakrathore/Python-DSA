
def binsea(arr,n,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]<n:
            low=mid+1
        else:
            high=mid-1
    return -1
    
arr=[4,5,6,7,8,9]
n=int(input("enter the value of n:"))

result = binsea(arr, n, 0, len(arr)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")