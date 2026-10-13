# Function to find the k-th largest element
def findKthLargest(nums, k):
    # Sort in descending order
    nums.sort(reverse=True)
    return nums[k-1] 

# Function to find minimum and maximum in the array
def findMinMax(nums):
    if not nums:
        raise ValueError("Array is empty")
    min_val = nums[0]
    max_val = nums[0]
    for num in nums[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return (min_val, max_val)

nums = [3, 2, 1, 5, 6, 4]
print("3rd largest:", findKthLargest(nums, 3)) 
print("Min and Max:", findMinMax(nums))     
