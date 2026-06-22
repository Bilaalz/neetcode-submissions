class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []

        def dfs(i):
            if i >= len(s):
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                piece = s[i: j + 1]
                if self.isPalindrome(piece):
                    path.append(piece)
                    dfs(j + 1)
                    path.pop()



        
        dfs(0)
        return res
        
        
        
        
    def isPalindrome(self, word):
        l = 0
        r = len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False
                
            l += 1
            r -= 1
        return True
