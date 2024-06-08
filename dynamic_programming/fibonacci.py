# Fibonacci - Dynamic Programming (Memoization)
# Without memoization: O(2^n). With memoization: O(n).

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

for i in range(10):
    print(f"fib({i}) = {fib(i)}")
