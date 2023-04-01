"""
question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Need to mutate the given `nums`

        original_len = len(nums)
        unique_nums = sorted(set(nums))
        unique_len = len(unique_nums)

        nums.clear()
        nums.extend([n for n in unique_nums])
        nums.extend([0 for x in range(original_len-unique_len)])

        return unique_len