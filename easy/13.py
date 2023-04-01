# question: https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s_list = []
        s_list[:0] = s
        result = 0
        size = len(s_list)
        
        for x in range(0,size,1):
            if x-1 >=0 and roman[s_list[x]] > roman[s_list[x-1]]:
                continue

            if x != size-1:
                print(roman[s_list[x]], roman[s_list[x+1]])
                result += (roman[s_list[x+1]] - roman[s_list[x]] if roman[s_list[x+1]] > roman[s_list[x]] else roman[s_list[x]])
            else:
                result += roman[s_list[x]]
        return result