class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        count2 = {}
        
        # Populate char counts of s1
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            
            if (r - l + 1) > len(s1):
                if count2[s2[l]] == 1:
                    del count2[s2[l]]
                else:
                    count2[s2[l]] -= 1
                l += 1
            
            if count1 == count2:
                return True
        
        return False

        