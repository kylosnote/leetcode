"""
9. Palindrome Number
source:https://leetcode.com/problems/palindrome-number/ 

Given an integer x, return true if x is a palindrome , and false otherwise.

Explaination: Palindrome checking is easier with python due to list manipulation where you can reverse a list easily with [::-1]

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False

"""
Interesting solution provided by others

source: https://leetcode.com/problems/palindrome-number/solutions/785314/python-3-1-solution-is-89-20-faster-2nd-is-99-14-faster-explanation-added/?orderBy=most_votes&languageTags=python

explaination: the question is solved by math equation where the number is fall under palindrome pattern or not

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
            return False
        
        result = 0
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
            
        return True if (x == result or x == result // 10) else False

"""