# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://www.youtube.com/watch?v=1pkOgXD63yU
from typing import List

class Solution:
    # R: The index of the list is the certain day and the price is the value of the list. Find the buying day and selling day for the max profit. (I know the future already) 
    # E: [7,6,5,3,4]
    # A: 
    # -use two pointers
    # -if L>R; shift the window and L shall be R because it's the smallest
    # -find the max value of R-L
    # -edge/coner case: only  two value in the given list
    # O: time: O(n) space: O(1)
    
    def maxProfit(self, prices: List[int]) -> int:
    
        # define two pointers and max var
        left = 0
        right = 1
        max_profit = 0
        
        # corner case
        if 2 == len(prices):
            return max(max_profit, prices[right] - prices[left])
        
        # iterate the prices
        while right < len(prices) :
            # if R-L <= 0; shift window; L=R, as R is so far smallest
            if prices[left] >= prices[right]:
                left = right
            else:
            # if R-L > 0; check if it's max value 
                max_profit = max(max_profit, prices[right] - prices[left])
                
            right += 1
        

        return max_profit
    

def main():
    prices = [7,1,5,3,6,4]
    solution = Solution()
    profit = solution.maxProfit(prices)
    print(profit)

if __name__ == "__main__":
    main()