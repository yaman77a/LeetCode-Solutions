class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        total = None
        l, r= 0, len(numbers) - 1
        while r > l:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]