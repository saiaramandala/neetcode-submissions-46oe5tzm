class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        for c in s:
            s_counter[c] = 1 + s_counter.get(c,0)

        t_counter = {}
        for c in t:
            t_counter[c] = 1 + t_counter.get(c,0)

        if s_counter == t_counter:
            return True
        return False    
        