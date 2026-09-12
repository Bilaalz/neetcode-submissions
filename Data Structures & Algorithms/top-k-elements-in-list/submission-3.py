class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count the frequencies of numbers
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        #create list where index is freq and value is number
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num) #for the case of same freqs across nums
        

        #find k most frequent
        res = []
        for num in range(len(bucket) - 1, 0, -1):
            if bucket[num]:
                res.extend(bucket[num])
            
            if len(res) == k:
                return res


            
