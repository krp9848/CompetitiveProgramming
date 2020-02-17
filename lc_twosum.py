# BruteForce - O(n^2) solution -> Hash Map approach would be faster
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        return indices of the two numbers such that they add up to a specific
        target
        """
        for i in range(0, len(nums) -1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
