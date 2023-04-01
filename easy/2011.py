"""
question: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

"""
from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return 0 + sum([-1 if "--"in i else 1 for i in operations]) # if has -- then -1 else +1
     