# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Double loop to go through each pair of the number combination and finally returning the matching pair indices
        for x in range(len(nums)-1):
            for y in range(x+1,len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]

        return []

