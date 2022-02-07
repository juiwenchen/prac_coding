from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        REACTO
        Repeat: 
            - What does "product" means?
            - "product" refers to the result of one or more multiplications.  
            - find the biggest product
            - a subarray shall be a continuous sequence. It means the elements are adjacent
        Example:
            - [2,3,-2,4]
            max, min, res = 
            2,2,2,
            6,6,6,
            -2,-12,6,
            -4,-48,6
        ACtion:
            - dynamic programming
            - **Not only the max but also the min should be counted because the min can be the max if it and its next element are negative
            - iteration of nums
            - find the greatest and smallest product among the maximum, the minimum and the number in each iteration
            - find the maximun from each iteration 
            - edge case:
                same number in the list
                only one element in the list
        Coding:
        Optimization: time O(n) , space O(1)
        """
        # Coding:

        # the maximum in the overall
        res = max(nums)

        # the maximom and minimum of each iteration
        cur_max, cur_min = 1, 1

        # iteration
        for n in nums:
            tmp = cur_max * n

            # find the max and min product of each iteration
            # n itself is evaluated to address the case like [-1, 8]. 
            # If n is the max, it means the start of the subarray is reset
            cur_max = max(tmp, cur_min * n, n)
            cur_min = min(tmp, cur_min* n, n)

            # find out the max by evaluating the max from previous iteration and current one
            res = max(res, cur_max)

        return res


def main():
    solution = Solution()
    nums = [2, 3, -2, 4]
    max_product = solution.maxProduct(nums)
    print(max_product)


if __name__ == "__main__":
    main()