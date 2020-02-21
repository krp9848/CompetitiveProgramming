class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        check whether the given number is palindrome or not
        """
        if x < 0:
            return False
        original_num = abs(x)
        #Use of extra array could be avoided(optimize this)
        right_to_left = []
        while original_num:
            rem = original_num % 10
            original_num = original_num // 10
            right_to_left.append(rem)
        left_to_right = right_to_left[::-1]
        if right_to_left == left_to_right:
            return True
        else:
            return False
