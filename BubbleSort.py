# Bubble Sort: 
# Simple and easy to understand, but inefficient for large datasets. 
# It repeatedly iterates through the list, swapping adjacent elements if they are in the wrong order.

# arr=[3,6,2,8,1,9,4]
# for i in range(len(arr)):
#     if arr[i]>arr[i+1]:
#         arr[i],arr[i+1]=arr[i+1],arr[i]
# print(arr)

# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break

# # Example usage
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(arr)
# print("Sorted array:", arr)


def bubble_sort(list1):   
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
print("The sorted list is: ", bubble_sort(list1))
