def frogJump(self, heights):
    n = len(heights)
    if n <= 2:
        return abs(heights[0] - heights[n - 1])

    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(heights[0] - heights[1])

    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(heights[i] - heights[i - 1]),
                    dp[i - 2] + abs(heights[i] - heights[i - 2]))

    return dp[n - 1]