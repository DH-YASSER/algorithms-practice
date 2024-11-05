# Binary Search - O(log n) time
# Only works on sorted arrays. Cuts search space in half each iteration.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(arr, 7))   # Output: 3
print(binary_search(arr, 6))   # Output: -1
