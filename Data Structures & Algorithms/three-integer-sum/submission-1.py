class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: #skipping duplicates
                continue 
            
            # 2 sum pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 #increment so we dont keep on appending the same values forever
                    r -= 1
                
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1


                # 2 sum finding
                if total < 0:
                    l += 1
                
                if total > 0:
                    r -= 1
        
        return res

        