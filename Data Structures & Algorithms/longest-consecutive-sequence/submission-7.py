class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        length, longest = 0, 0

        for num in nums:

            if num - 1 not in numSet: #beginning of sequence
                length = 1

                while num + 1 in numSet:
                    length += 1
                    num += 1
            
            longest = max(length, longest)
        
        return longest

