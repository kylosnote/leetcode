"""
question: https://leetcode.com/problems/valid-parentheses/

Explaination: keep replace any (),[],{} until the len no changes. if 0 mean valid parenthesis
Improvement: using while and keep looping the string is not time efficient.
"""
class Solution:
    def isValid(self, s: str) -> bool:        
        current_length = len(s)
        latest_length = 0
        while current_length!=latest_length:
            current_length = len(s)
            s = self.replace_set(s)
            latest_length = len(s)
            
        return True if current_length== 0 else False

    def replace_set(self, s:str):
        set_list = ['()','[]','{}']
        for pair in set_list:
            s = s.replace(pair,"")
        return s


"""
Comparing popular solution
source: https://leetcode.com/problems/valid-parentheses/solutions/2411675/very-easy-100-fully-explained-c-java-python-js-python3/?orderBy=most_votes&languageTags=python3

Explaination: open parenthesis as key and close as value,
each open into a queue and achieve last in first out through pop and check against the key:value 
return false if the last open parent thesis is not the key of current character

class Solution:
    def isValid(self, s: str) -> bool:
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0
"""
