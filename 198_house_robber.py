from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        REACTO
        Repeat:
            - each element in nums is the money 
            - cannot plus the adjacent element
            - find the max sum 
        Example:
        [2,1,1,1,1,4] 
        max(rob1 + n, rob2)
        2+1 >1
        1+1 <3
        1+1 <3 
        3+4 <3
        
        2 1 3 3 3 7
         
        """
        # two variables to store the prev-prev and the prev 
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, ...]
        # [rob1, rob2, n+1]
        # [rob1, rob2, n+2]
        # [n, rob1, rob2, n + 3]
        # iteration
        for n in nums:
            # find the max between prev-
            tmp = max(rob1 + n ,rob2)
            rob1 = rob2
            # rob2 always keep the max
            rob2 = tmp
        return rob2


def main():
    solution = Solution()
    nums = [2,1,1,1,1,4] 
    result = solution.rob(nums)
    print(result)


if __name__ == "__main__":
    main()