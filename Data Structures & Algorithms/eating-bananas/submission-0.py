class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        res = r


        while l <= r:
            k = (r + l) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1 #try a smaller speed
            
            else:
                l = k + 1

        return res
            
            
                
        