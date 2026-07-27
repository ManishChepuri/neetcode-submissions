class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        strs: List[str] = []
        i = 0
        while i < len(s):
            s_len = ""
            while (s[i] != "#"):
                s_len += s[i]
                i += 1
            i += 1
            s_len = int(s_len)
            strs.append(s[i : i + s_len])
            i += s_len
        return strs
            
