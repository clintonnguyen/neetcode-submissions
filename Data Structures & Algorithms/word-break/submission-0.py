class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            res = False
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    res = res or dfs(j + 1)
            dp[i] = res
            return res
        return dfs(0)