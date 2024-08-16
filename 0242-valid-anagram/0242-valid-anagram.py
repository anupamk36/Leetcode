class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dicti = {}
        for i in range(len(s)):
            if s[i] in dicti:
                dicti[s[i]] += 1
            else:
                dicti[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in dicti:
                dicti[t[i]] -= 1
            else:
                return False
        
        for value in dicti.values():
            if value != 0:
                return False
            return True
        

        
        
