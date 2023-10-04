from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_index = {}
    
    for index, num in enumerate(nums):

        complement = target - num
        
        if complement in num_index:
            return [num_index[complement], index]
        
        num_index[num] = index
    
    return []

# Example 1
print(twoSum([2,7,11,15], 9))  # Output: [0, 1]

# Example 2
print(twoSum([3,2,4], 6))  # Output: [1, 2]

# Example 3
print(twoSum([3,3], 6))  # Output: [0, 1]
