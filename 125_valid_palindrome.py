class Solution:
    # Repeat: What is palindrome? reading from left or the other way around is the same
    # only alphabets count and case insensetive
    # E: amanaplanacanalpanama
    # Approach:
    # -remove non-aphabet chars
    # -two pointers from start and end respectively
    # till the right < left
    # edge/corner cases : no char and one char?
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphabetic chars
        string =""
        for char in s:
            if char.isalnum():
                string += char
        
        if len(string) == 0:
            return True
        
        left = 0
        right = len(string) - 1
        # Iteration of string till right < left
        while right >= left:
            if string[left].lower() != string[right].lower():
                return False
            # move pointers
            left += 1
            right -= 1
        
        return True

def main():
    s = "0P"
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)

if __name__ == "__main__":
    main()