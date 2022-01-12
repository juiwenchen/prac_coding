from typing import List
class Solution:
    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        # record the seen numbers and their indices {num: inedx} by hash table
        seen_nums = {}
        for idx, value in enumerate(nums):
            remaining = target - value
            if remaining in seen_nums:
                return [seen_nums[remaining], idx]
            
            seen_nums[value] = idx

    def twoSum_pointer(self, nums: List[int], target: int) -> List[int]:
        # Two pointers solution for the sorted list
        sorted_nums = sorted(nums)
        # smallest 
        left = 0
        # biggest
        right = len(nums) - 1
        
        while(1):
            _sum = sorted_nums[left] + sorted_nums[right]
            
            if _sum > target:
                # need to reduce the value, so right pointer should shift towards to the left
                right = right - 1
            elif _sum < target:
                # need to increse the value, so left pointer should shift towards to the right
                left = left + 1
            else:
                
                left_index = nums.index(sorted_nums[left])
                
                if sorted_nums[left] == sorted_nums[right]:
                    # In case, two values are the same, the index searching needs to be taken care to avoid the duplicate
                    right_index = nums.index(sorted_nums[right], left_index + 1)
                else:
                    right_index = nums.index(sorted_nums[right])
                    
                return [left_index, right_index]

def main():
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    result_hash = solution.twoSum_hash(nums, target)
    result_pointer = solution.twoSum_pointer(nums, target)
    print(result_pointer)
    print(result_hash)
    pass

if __name__ == "__main__":
    main()