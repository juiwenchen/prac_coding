from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # N-sum is fundamentally based on two-sum.
        # The recursion can create the generic function to dive into the (N-1)-sum, till it reaches two-sum  
        sorted_nums = sorted(nums)
        output = self.sum_helper(sorted_nums, target, 4)
        
        return output
    
    def sum_helper(self, nums: List[int], target: int, elements: int) -> List[List[int]]:
        """Move the index of the current leavel (N) and dive into next level (N - 1).

        This run recursively, till the N reaches 2. Once the 2-sum finishes, the index of the number moves to the next.

        :param: nums: sorted numbers
        :param: target: the value in which the N-sum should equal to
        :param: elements: N level
        :return: the sets equal to the target
        """
        if elements < 2 or len(nums) < elements:
            return
        
        if elements > 2:
            output = []
            for idx in range(len(nums) - elements + 1) :
                if idx > 0 and results:
                    if nums[idx - 1] == nums[idx]:
                        continue
                next_target = target - nums[idx]
                results = self.sum_helper(nums[idx + 1:], next_target, elements - 1)
                if results:
                    for result in results:
                        result.append(nums[idx])
                        
                    output.extend(results)
            return output
        
        elif elements == 2:
            results = self.twoSum(nums, target)
            
            return results
        
    
    def twoSum(self, nums:List[int], target: int) -> List[List[int]]:
        results = []
        seen_nums = {}
        
        for idx, num in enumerate(nums):
            if results and idx >= 1:
                if num == nums[idx - 1]:
                    continue
            
            remaining = target - num
            if remaining in seen_nums:
                results.append([num, remaining])
            if num not in seen_nums:
                seen_nums[num] = idx
            
        return results
                    

def main():
    nums = [1,0,-1,0,-2,2]
    target = 0
    solution = Solution()
    result = solution.fourSum(nums, target)
    print(result)
    pass

if __name__ == "__main__":
    main()
    