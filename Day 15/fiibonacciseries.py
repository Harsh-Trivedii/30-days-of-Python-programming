# Fibonacci Series
def fibonacci(n):
    fib_series = [0, 1]  # Initialize the first two Fibonacci numbers

    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
        fib_series.append(next_num)

    return fib_series
n = 10  
result = fibonacci(n)
print(result)
