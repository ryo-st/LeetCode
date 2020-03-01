# coding: utf-8
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for current_index in range(len(nums)):
            current_num=nums[current_index]    
            current_nums=nums[current_index+1:]
            for num_index in range(len(current_nums)):
                if target-(current_nums[num_index]+current_num) is 0:
                    return [current_index,(current_index+1)+num_index]