# 35. Search Insert Position
# Easy
# Topics
# premium lock icon
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

nums = [int(x) for x in input("enter the number in acendng order: ").split()]
target = int(input("Enter the target element: "))
def insert_position(arr, target_val):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target_val:
            return mid              # return index
        elif arr[mid] < target_val:
            low = mid + 1
        else:
            high = mid - 1 
    
    return low   # insert position if not found

result = insert_position(nums, target)

print(f"Insert position index: {result}")