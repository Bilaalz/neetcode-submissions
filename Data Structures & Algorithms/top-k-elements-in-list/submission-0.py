class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}

        for num in nums:
            mp[num] = mp.get(num, 0) + 1 #counted the frequency of each number
        
        
        return sorted(mp, key=mp.get, reverse = True)[:k]
        

        