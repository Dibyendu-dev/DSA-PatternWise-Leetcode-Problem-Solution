def fibonacci_series(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_series(n - 1, memo) + fibonacci_series(n - 2, memo)
    return memo[n]