''' 
question: https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ''
        
        nmax = min([len(s) for s in strs]) # find the shortest string
        terminate = False

        # Loop through each pair of string find find unmatch character
        for i in range(nmax):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    terminate = True
                    break
            if not terminate:
                out += char
                
        return out