class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(Log N) binary search
        
        middle_idx = len(nums) // 2
        smallest_idx = 0
        biggest_idx = len(nums) - 1
        
        # deal with the extreme indices
        if nums[biggest_idx] == target:
            return biggest_idx
        if nums[smallest_idx] == target:
            return smallest_idx
        
        while(1):
            num = nums[middle_idx]
            if num == target:
                return middle_idx
            
            if middle_idx == smallest_idx:
                return - 1
            
            if num > target:
                biggest_idx = middle_idx
            else:
                smallest_idx = middle_idx
                
            middle_idx = (biggest_idx + smallest_idx) // 2
            
def main():
    nums = [-1,0,3,5,9,12]  # the pre-condition for binary search is the given list must be sorted
    target = 9
    result = Solution().search(nums=nums, target=target)
    print(result)


if __name__ == '__main__':
    main()