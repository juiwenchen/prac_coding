"""https://leetcode.com/problems/palindromic-substrings/"""
from typing import List

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        REACTO
            REPEAT:
                - a single character is considered as a palindromic substring
            Example:
                aaa
                odd and even
                o:a , e: aa  p_str=["a","aa"]
                  o and e : left pointer out of range
                 
                odd:a, even:aa p_str=["a","aa", "a", "aa"]
                 o:aaa, e: right pointer out of range   p_str=["a","aa", "a", "aa","aaa"]
                 o: left and right OOR
                
                odd:a, even: right pointer OOR   p_str=["a","aa", "a", "aa","aaa", "a"]
                 o: right pointer OOR 
            Action:
                - count odd and even
                - left and right pointers start from the same character for the odd
                - the left at the iterated character while the right is the next one
                - declare a global conunter

        """
        count = 0
        
        for idx in range(len(s)):
            
            # left and right pointer at the iterated char for the odd palindrome
            l, r = idx, idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # the iterated char is counted in this first loop
                count += 1
                # pointers shifted to the left and right
                l -= 1
                r += 1
            
            # the left at the iterated char while the right at the next one for the even palindrome
            l, r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                # pointers shifted to the left and right
                l -= 1
                r += 1
        
        return count 

def main():
    solution = Solution()
    s = "aaa"
    result = solution.countSubstrings(s)
    print(result)


if __name__ == "__main__":
    main()