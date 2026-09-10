class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #hashmap where the keys are sorted string and values are the words
        mp = {}

        for word in strs:
            #keys need hashable string
            key = "".join(sorted(word))

            if key not in mp:
                mp[key] = []
            
            mp[key].append(word)
        
        return list(mp.values())