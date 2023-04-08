"""
2. Add Two Numbers

source:https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        for i in range(100): #100 is max contraint
            if l1 is not None:
                total += (l1.val* pow(10,i))
                l1 = l1.next

            if l2 is not None:
                total += (l2.val* pow(10,i))
                l2 = l2.next

            if l1 is None and l2 is None: # no more node
                break


        result = ListNode()
        for single in str(total):
            if not result.val and result.next is None:
                result.val = int(single)
            else:
                result = ListNode(val=int(single),next=result)

        return result
    
"""
most popular solution
source: https://leetcode.com/problems/add-two-numbers/solutions/1016/clear-python-code-straight-forward/?orderBy=most_votes&languageTags=python

explaination:
each loop will remove the current node 

using `divmod` 
the `carry` is carry forward to next node whenever l1 + l2 is more than 10 to make sure the next node value will + 1

root.next because root is for init always will be empty, all the upcoming node will be added to n

root and n initial refer to the same object, after first loop
n.next = 1st node
root.next = 1st node

second loop
n.next= 2nd node
root.next = 1st node


root = [0, 1st, 2nd, 3rd ....]

class Solution:
# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
"""


        
"""
For testing

l1 = ListNode(val=2,next=ListNode(val=4,next=ListNode(val=3)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))

solution = Solution()
final = solution.addTwoNumbers(l1,l2)
print(final)
"""
