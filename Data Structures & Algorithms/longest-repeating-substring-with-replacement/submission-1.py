class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        #trick here is to know how many replacements needed not which characters are being replaced
        l = 0
        r = 0
        count = {}
        res = 0


        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            length = r - l + 1

            if length - max(count.values()) <= k: #how many replacements needed
                res = max(res, length)

            else: 
                count[s[l]] -= 1
                l += 1
            
        return res



            

        
        