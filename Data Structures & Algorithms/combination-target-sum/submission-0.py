class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, total):

            if total == target:
                res.append(path.copy())
                return
            
            #i points to the current branch we are on
            if i >= len(nums) or total > target:
                return
            
            #we are choosing to continue using the same number
            path.append(nums[i])
            dfs(i, total + nums[i])

            #pop and use different number
            path.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)

        return res