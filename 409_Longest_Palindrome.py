class Solution:
    def longestPalindrome(self, s: str) -> int:
        # hash table/counting/understand of palindrome
        char_count_dict = {}
        for char in s:
            char_count_dict[char] = char_count_dict.get(char, 0) + 1
        
        # Palindrome needs the combination of even-count letters and only one even-count letter
        # for the odd-count letter, it needs to be deducted by 1 to make it even
        total_count = 0
        odd_flag = False
        for key in char_count_dict:
            if char_count_dict[key] % 2 == 0:
                # sum up all even counts of the char
                total_count += char_count_dict[key]
            else:
                # sum up all the odd-count char which has been deducted by one 
                total_count += (char_count_dict[key] - 1)
                odd_flag = True
        
        if odd_flag:
            total_count += 1
        
        return total_count

def main():
    s = "abccccdd"
    result = Solution().longestPalindrome(s=s)
    print(result)


if __name__ == '__main__':
    main()