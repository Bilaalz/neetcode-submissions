class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        string = s.lower()

        while l < r:

            while string[l].isalnum() == False and l < r:
                l += 1
            
            while string[r].isalnum() == False and l < r:
                r -= 1

            if string[l] != string[r]:
                return False

            l += 1
            r -=1
        
        return True
        