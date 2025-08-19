def is_prime(n):

    if n <= 1:
        return f" {n} isn't  prime number"
    
    for i in range(2, n):
        if n % i == 0:
            return f"{n} isn't  prime number"
    return f"{n} is  prime number"
res = is_prime(7)
print(res)