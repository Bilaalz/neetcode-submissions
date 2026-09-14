class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #this is 2sum but target is now the the index you are at 

        nums = sorted(nums)
        res = []



        for i in range(len(nums)):
            if nums[i] > 0:
                break #since sorted in increasing
            
            if i > 0 and nums[i] == nums[i - 1]: #skip duplicate
                continue
            
            target = -nums[i]

            l = i + 1
            r = len(nums) - 1
    
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                elif nums[l] + nums[r] > target:
                    r -= 1
                
                else:
                    l += 1
        
        return res


