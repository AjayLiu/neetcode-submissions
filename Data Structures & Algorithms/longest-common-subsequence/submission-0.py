class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Let text1 be the shorter one
        # DP[i][j] = length of LCS of text1[0:i] and text2[0:j]
        # DP[i][j] = 
        #             if text1[i] == text2[j], 
        #               DP[i][j] = 1 + DP[i-1][j-1] 
        #             otherwise 
        #               DP[i][j] = max(DP[i][j-1], DP[i-1][j])
        # return last corner

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[len(text1)-1][len(text2)-1]
