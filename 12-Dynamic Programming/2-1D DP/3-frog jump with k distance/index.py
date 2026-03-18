def frogJump(self, heights, k):
    n = len(heights)
    if n <= 2:
        return abs(heights[0] - heights[n - 1])

    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(heights[0] - heights[1])

    for i in range(2, n):
        dp[i] = min(dp[i - j] + abs(heights[i] - heights[i - j]) for j in range(1, min(k, i) + 1))

    return dp[n - 1]