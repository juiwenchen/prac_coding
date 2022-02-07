"""https://leetcode.com/problems/longest-palindromic-substring/"""
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """REACTO
            Repeat:
                -longest palindromic substing
                -what is palindrome? a word/phrase read from the left or the right are same
                -e.g aaaaa, aabaa, cccc, cbbc
            Example:
                -Odd palindrome:
                Iterate each char and check its adjacent 
                babad
                b   pal = b
                    the left is out of index 
                a
                    bab  pal=bab
                b
                    aba  pal=bab, aba
                    babad
                a
                    bad
                -Even Palindrome:
                Iterate each char check the iterated char and its right char initially. Afterwards, move the two index toward the left and the right
                aabbbb
                aa  pal=aa
                    the left out of index
                ab 
                bb  pal=bb
                    abbb
                bb
                    bbbb    pal=bbbb
                bb
                    the right out of the index
            Action:
                -two pointers
                -iterate each char
                Odd:
                    -two pointer point to the same char initially
                Even:
                    -one pointer points to the iterated char and the other one points to its right.
                -The two pointers move to the left and the right respectively
                -Store the longest one
        """
        max_substr = ""
        longest = 0
        for idx in range(len(s)):

            # Odd palindromic substring
            l, r = idx, idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    max_substr = s[l:r + 1]
                l -= 1
                r += 1

            # Even palindromic substring
            l, r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    max_substr = s[l:r + 1]
                l -= 1
                r += 1

        return max_substr

def main():
    solution = Solution()
    s = "ababababa"
    result = solution.longestPalindrome(s)
    print(result)


if __name__ == "__main__":
    main()