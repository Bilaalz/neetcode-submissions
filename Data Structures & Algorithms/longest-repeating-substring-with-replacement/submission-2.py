class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        #trick here is to know how many replacements needed not which characters are being replaced
        l = 0
        r = 0
        count = {}
        res = 0
        maxf = 0


        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            length = r - l + 1
            maxf = max(maxf, count[s[r]])

            if length - maxf > k: #how many replacements needed
                count[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res) #length changed
            
        return res



            

        
        