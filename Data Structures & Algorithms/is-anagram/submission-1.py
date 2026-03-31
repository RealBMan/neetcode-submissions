class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        if len(s) != len(t):
            return False

        for letter in s: 
            if letter not in s_hash:
                s_hash[letter] = 1
            else :
                s_hash[letter]+=1

        for letter in t: 
            if letter not in t_hash:
                t_hash[letter] = 1
            else :
                t_hash[letter]+=1
        
        for key in s_hash:
            if key not in t_hash:
                return False
            elif s_hash[key] != t_hash[key]:
                return False
        return True