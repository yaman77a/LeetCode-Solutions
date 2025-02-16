class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        total = None # Stores the sum of current two numbers
        l, r = 0, len(numbers) - 1 # Two pointers at both end of the list
        while r > l: # A loop while left pointer is before right pointer
            total = numbers[l] + numbers[r] # Compute the sum of two items            
            if total > target:    
                r -= 1 # If sum is larger than target, then move right pointer left
            elif total < target:
                l += 1 # If sum is smaller than targer, then move left pointer right 
            else:
                return [l + 1, r + 1] # When we found the target sum, return 1-based indices