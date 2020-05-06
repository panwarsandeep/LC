class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-","")
        S = S.upper()
        l = len(S)
        res = ""
        while l > K:
            res = "-" + S[-K:] + res
            S = S[:l-K]
            l -= K
        res = S+res
        
        return res