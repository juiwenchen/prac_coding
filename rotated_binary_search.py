from typing import List

class Solution_find_target_by_pivot:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            # Edge case where only one element in the given list.
            if nums[0] == target:
                return 0
            return -1
        
        pivot_index = len(nums) - 1  # The index of the biggest nummber in the given list.
        
        for idx in range(len(nums)):
            # Find the pivot index
            if idx >= len(nums) - 1:
                break
            
            if nums[idx] > nums[idx + 1]:
                # In an ascending-sorted array, the current number shall be smaller than its right number.
                # If the exception occurs, the current index is the pivot index.
                # It is the maximum number in the given array.
                pivot_index = idx
                break
        
        start = 0
        if pivot_index < len(nums) - 1:
            # If the elements are rotated in the given sorted list, The next number of the biggest is the smallerset
            start = pivot_index + 1
            
        if nums[start] == target:
            # Edge case
            return start
        if nums[pivot_index] == target:
            # Edge case
            return pivot_index
        
        result = self.binary_search(nums, start, pivot_index, target)
        return result
    
    def binary_search(self, nums: List[int], start, end, target):        
        if start > end:
            # rotated list
            # the half amount of the elements in between start and end plus start is the middle.
            middle = (end + len(nums) - start) // 2 + start
            if middle >= len(nums):
                # As it is rotated, the middle may exceed the length of the list. 
                # In this case, the middle shall be circulated from the beginning
                middle = middle - len(nums)
                
        elif end > start:
            middle = (start + end) // 2
        else:
            return -1
        
        if nums[middle] == target:
            # Target is found
            return middle
        elif nums[middle] > target:
            if middle == start or middle == end:
                # No more middle number in between
                return -1
            result = self.binary_search(nums, start, middle, target)
        elif nums[middle] < target:
            if middle == start or middle == end:
                # No more middle number in between
                return -1
            result = self.binary_search(nums, middle, end, target)
        
        return result


class Solution_find_min:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while (right >= left):
            mid = (right + left) // 2
            if left == mid:
                return min(nums[left], nums[right])
            
            if nums[left] > nums[right]:
                # Numbers in between are rotated, it means the smallest number maybe on the right
                if nums[mid] > nums[left]:
                    # Middle is bigger than left, it means the numbers from left to middle are ascending only
                    # The pivot may be in right part
                    left = mid + 1
                else:
                    # the left may have the pivot 
                    right = mid
            else:
                # Ascending numbers from the left to right.
                # Address it like normal binary search
                if nums[mid] > nums[left]:
                    #The left part has the smallest number
                    right = mid
                else:
                    left = mid + 1


def main():
    nums = [4,5,6,7,0,1,2]
    target = 5
    solution = Solution()
    result = solution.search(nums, target)
    print(result)


if __name__ == "__main__":
    main()
