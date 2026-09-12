class Solution:

    def encode(self, strs: List[str]) -> str:
        #to encode, encode string length and delimiter, put it at the beginning of the encode
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        #extract string length and decode word after delimiter. search for delimiter
        res = []
        i = 0
        
        #slicing starts from index a to b but not including b
        while i < len(s):
            j = i

            while s[i] != "#":
                i += 1
            
            length = int(s[j:i])
            res.append(s[i + 1: i + 1 + length])
        
            i = i + length + 1
        
        return res
            
            

            


