import pdb
import collections
class Solution:
    def lengthOfLongestSubstring(self, row, col):
        max_x, max_y = 7, 4
        dp = [[[[0 for _ in range(3)] for _ in range(3)] for _ in range(max_y+1)] for _ in range(max_x+1)]
        dp[0][0][0][0] = 1  

        for i in range(1,3):
            dp[i][0][i][0] = 1
            dp[0][i][0][i] = 1

        for x in range(1, max_x + 1):
            for y in range(1, max_y + 1):
                dp[x][y][0][1] += (dp[x][y-1][2][0] + dp[x][y-1][1][0])
                dp[x][y][0][2] += dp[x][y-1][0][1]
                dp[x][y][1][0] += (dp[x-1][y][0][1] + dp[x-1][y][0][2])
                dp[x][y][2][0] += dp[x-1][y][1][0]


        return sum(dp[7][4][r][u] for r in range(3) for u in range(3))


# 示例
solution = Solution()
print(solution.lengthOfLongestSubstring(5,4)) 
                
