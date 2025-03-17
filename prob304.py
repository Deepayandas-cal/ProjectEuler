import random

MOD = 1234567891011
START = 10**14
LIMIT = 100000

def mod_mult(a, b, mod):
    return (a * b) % mod

def mod_exp(base, exp, mod):
    result = 1
    while exp:
        if exp & 1:
            result = mod_mult(result, base, mod)
        base = mod_mult(base, base, mod)
        exp >>= 1
    return result

def is_prime(n):
    if n < 2 or (n % 2 == 0 and n != 2):
        return False
    if n in (2, 3):
        return True

    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(5):  
        a = random.randint(2, n - 2)
        x = mod_exp(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = mod_mult(x, x, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def next_prime(n):
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n

def generate_primes(start, count):
    primes = []
    num = next_prime(start)
    while len(primes) < count:
        primes.append(num)
        num += 2
        while not is_prime(num):
            num += 2
    return primes

def fibonacci(n, mod):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % mod
    return a

def main():
    primes = generate_primes(START, LIMIT)
    result = sum(fibonacci(p, MOD) for p in primes) % MOD
    print(result)

if __name__ == "__main__":
    main()
