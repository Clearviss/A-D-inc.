class Solution:
    def romanToInt(self, s: str) -> int:
        exc_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        N = len(s)
        i = N - 1
        out = 0
        while i >= 0:
            if i < N - 1 and exc_dict[s[i]] < exc_dict[s[i+1]]:
                out = out - exc_dict[s[i]]
            else: 
                out = out + exc_dict[s[i]]
            i = i - 1
        return out
            
