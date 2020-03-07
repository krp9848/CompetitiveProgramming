class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        inline removal of an given value 'val' from the given list 'nums'
        """
        i = 0
        while True:
            if i < len(nums):
                if nums[i] == val:
                    del nums[i]
                else:
                    i += 1
            else:
                break
        return len(nums)
