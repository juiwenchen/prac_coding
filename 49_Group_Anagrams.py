"""https://leetcode.com/problems/group-anagrams/"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """REACTO
        Repeat:
        Anagrams is a word or phrase consist of the same letters of a different word or phrase.
        For example, "eat" "tea" and "ate" are anagrams as they all consist of the same letters which are one a, one e and one t.

        Example:
        eat has 1a, 1e and 1t.
        tea has 1a, 1e and 1t.
        ate has 1a, 1e and 1t.
        They are the anagram

        Action:
            -count the letters 
            -put the count like 1a1e1t (eat, ate, tea) to the key of a hash map.
            -the word/phrase/string is its value of the hash map 
            -e.g {"1a1e1t": [eat,ate,tea]}
            -***tuple can be the key of a dict
            -***ord() converts char to ASCII  
        Code:

        """
        # a hash map 
        anagrams_dict = {}
        
        # iterate the given strings
        for string in strs:
            # declare a fixed list with 26 elements containing the initial value 0
            count_list = [0] * 26 # a- z
            
            # iterate the char in a string
            for char in string:
                # convert char to ASCII using ord()
                # For example, a=80, b=81 ..., so the char minus a is the correspoding index in the letter-count list
                count_list[ord(char) - ord("a")] += 1
            
            if tuple(count_list) in anagrams_dict:
                anagrams_dict[tuple(count_list)].append(string)
            else:
                anagrams_dict[tuple(count_list)] = [string]
        
        # anagrams_dict.values() should also work
        return [anagram for anagram in anagrams_dict.values()]


def main():
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = solution.groupAnagrams(strs)
    print(result)


if __name__ == "__main__":
    main()