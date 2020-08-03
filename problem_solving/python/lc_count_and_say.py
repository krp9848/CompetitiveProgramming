# Brute force solution to the problem. Optimize this.


class Solution:
    def countAndSay(self, n: int) -> str:
        final_string_list = []

        if n == 1: 
            return '1'

        if n > 1: 
            result = list(self.countAndSay(n - 1))
            i = 0
            length = len(result)
            while i < length:
                count = 1
                value = result[i]
                j = i + 1
                while j < length:
                    if result[i] != result[j]:
                        break
                    else: 
                        count += 1
                        j += 1
                i = j 
                final_string_list.extend([str(count), value]) 
                
        return ''.join(final_string_list)

