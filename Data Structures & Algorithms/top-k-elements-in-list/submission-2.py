class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}
        freq = [[] for i in range(len(nums) + 1)] #creating a bucket

        for num in nums:
            mp[num] = mp.get(num, 0) + 1 #counted the frequency of each number
        
        #fill the bucket up
        for key, value in mp.items():
            freq[value].append(key) #indicies are freqs, and value is number

        res =[]
        for i in range(len(freq) - 1, 0, -1): #traverse from last index since its the biggest
            for num in freq[i]: # we loop over an index
                res.append(num)
                
                if len(res) == k:
                    return res
        
        
        

        