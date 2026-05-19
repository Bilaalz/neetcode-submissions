class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return "None"

        encoded_s = 'break'.join(strs)
        return encoded_s

    def decode(self, s: str) -> List[str]:
        if s == "None": return []
        
        decoded_s = s.split('break')
        return decoded_s