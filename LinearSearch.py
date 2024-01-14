def linsea(arr, n):
    for i in range(len(arr)):  # Loop through indices
        if arr[i] == n:  # Compare element at index i with n
            return i  # Return the index if found
    return -1  # Return -1 if not found

arr = [3, 2, 4, 1, 8, 5, 6, 9]
n = int(input("Enter the number:"))

result = linsea(arr, n)
print(str(result))
