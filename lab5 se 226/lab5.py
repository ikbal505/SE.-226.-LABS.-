def factorial(x):

    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


calc_term = lambda x, i: (x**i) / factorial(i)

def exp_x(x, n):

    total_sum = 0
    for i in range(n):
        total_sum += calc_term(x, i)
    return total_sum
x = float(input("Enter x: "))
n = int(input("Enter number of terms n: "))
print(f"exp({x}) ≈ {exp_x(x, n)}")


def result(n):
    """
This function Sn = 1 - 1/2 + 1/3 - 1/4 + ... + (-1)^(n+1)/n calculates the series with recursive

    Recursive function logic
    - The function calls itself at every step, decrementing the value of n by 1.
    - It stops when n is equal to 1.

    - Because of (-1)^(n+1)
      if n is odd (1, 3, 5...) result is positive
     if n is even (2, 4, 6...) result is negative
    """
    global S
    if n == 1:
        S += 1
        return
    result(n - 1)
    S += ((-1) ** (n + 1)) / n

n = int(input("Enter n: "))
S = 0
result(n)
print(f"S_{n} = {S}")




