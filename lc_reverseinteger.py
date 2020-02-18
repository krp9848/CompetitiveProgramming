class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse digits of an integer
        """
        sign = 1
        #tracking the sign
        if x < 0:
            sign = -1
        rems = []
        x = abs(x)

        while x:
            rems.append(x % 10)
            x = x // 10

        length = len(rems)
        total = 0
        for i in range(length):
            total += rems[i] * 10 ** (length - i - 1)
        #reversed number should be less than 2 ** 31(signed integer)
        if total > pow(2, 31):
            return 0

        return sign * total
