"""https://leetcode.com/problems/longest-repeating-character-replacement/"""
from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        REACTO
        Repeat:
            find the longest substring containing the same letter
            k times replacement of the letter
        Example:
            "AABABBA" k=1
            AABA 
             ABA
              BAB
                BBB
        
        length_substing - count(max(letter)) <= 1
        
        Ideally,  the max length of substring equals to max number of the letter in the substring

        the max length of substring <= max number of the letter in the substring + the times of the replacement

        if the equation is NOT satisfied, it means the substing does NOT consist of the same letter and vice versa

        Action: 
            sliding window formed by two pointers
            a hashmap for letter - count (to count the max number of the letter)
            iterate the given string and exanimate it with the equation
        Coding:
        """
        # two pointers for a sliding window
        l = 0
        # maximum number of a substring 
        res = 0

        # hashmap to count letters
        letter_count_map = {}

        # interate the sting 
        for r in range(0, len(s), 1):
            # count letters
            letter_count_map[s[r]] = letter_count_map.get(s[r], 0) + 1

            # check if the equation is not satisfied, find the next substring
            # the length of the current window is r - l - 1
            while ((r - l + 1) - max(letter_count_map.values())) > k:
                # as the window will move to the left, the count of the letter in the substring should be deducted by 1
                letter_count_map[s[l]] -= 1

                # shift the sliding window to the left
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            


def main():
    solution = Solution()
    s = "AABABBA"
    k = 1
    result = solution.characterReplacement(s, k)
    print(result)


if __name__ == "__main__":
    main()