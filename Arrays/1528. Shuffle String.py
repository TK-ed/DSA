class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r=""
        f = [0] * len(s)
        for i in range(0, len(s)):
            f[indices[i]]=s[i]
            print(f)
        for i in f:
            r=r+i
        return r

