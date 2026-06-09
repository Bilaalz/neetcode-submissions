class Solution:
    """
    Input: nums = [1,2,3]

    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    goal -> all possible subsets, no dups..

    ignore dup numbers, if no dup numbers then how do we do it?

    [a, b, c]

    pick each one of them as starting val and make that a set, plus [] is a set

    [] // this is like base
    
    [a]

    [b]

    [c]

    now each time from here, only go forward until end of arr and make that a set
    
    [a, b]
    [a, c]

    [b, c]

    last time

    [a, b, c]

    we can do this but how to deal with dups?
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]

        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # you not the first guy, and you the same as prev, skip..
                continue

            arr = [nums[i]]
            self.backtrack(arr, i, nums)

        return self.res

    def backtrack(self, subset, start, nums):
        self.res.append(subset)

        for i in range(start + 1, len(nums)):
            if i > start + 1 and nums[i] == nums[i - 1]:
                continue

            self.backtrack(subset + [nums[i]], i, nums)
        return

