class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = {}

        for i in range(len(s1)):
            if s1[i] not in s1_count: 
                s1_count[s1[i]] = 1
            else:
                s1_count[s1[i]] += 1
        
        size = len(s1)

        s2_count = {}

        for i in range(size):
            if s2[i] not in s2_count:
                s2_count[s2[i]] = 1
            else:
                s2_count[s2[i]] += 1
        if s2_count == s1_count:
            return True
        
        for j in range(size, len(s2)):
            if s2[j] not in s2_count:
                s2_count[s2[j]] = 1
            else:
                s2_count[s2[j]] += 1
            if s2[j - size] in s2_count:
                s2_count[s2[j - size]] -= 1
            if s2_count[s2[j - size]] == 0:
                s2_count.pop(s2[j - size], None)
            if s2_count == s1_count:
                return True
        print(s2_count)
        return False
