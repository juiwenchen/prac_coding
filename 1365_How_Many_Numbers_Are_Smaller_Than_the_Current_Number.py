class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sort and hash table
        # sort numbers from the smallest to the biggest
        sorted_nums = sorted(nums)
        len_nums = len(nums)
        num_win_dict = {}
        
        for idx in range(len_nums):
            if sorted_nums[idx] not in num_win_dict:
                # avoid the duplicates
                num_win_dict[sorted_nums[idx]] = idx
        
        output = [num_win_dict[num] for num in nums]
        return output
            
        
       # len_nums = len(nums)
       # idx_nums_dict = { idx: num for idx, num in enumerate(nums)}
       # num_count_dict = { num: nums.count(num) for num in nums}
       # # nums = list(set(nums))
       # sorted_nums = sorted(nums, reverse=True)
       # idx_win_dict = {}
       # nums_win_dict = {}
       # for idx, num in idx_nums_dict.items():
       #     if num in nums_win_dict:
       #         idx_win_dict[idx] = nums_win_dict[num]
       #         continue
       #     sorted_idx = sorted_nums.index(num)
       #     num_count = num_count_dict[num]
       #     win_others_num =  len_nums - sorted_idx - num_count
       #     idx_win_dict[idx] = win_others_num
       #     nums_win_dict[num] = win_others_num
       # 
       # output = [count for idx, count in idx_win_dict.items()]
       # return output
            