import random

MODULO = 1234567891011
START_PRIME = 10**14
PRIME_COUNT = 100000

def mulmod(a, b, mod):
    return (a * b) % mod

def powmod(base, exp, mod):
    res = 1
    while exp:
        if exp % 2:
            res = mulmod(res, base, mod)
        base = mulmod(base, base, mod)
        exp //= 2
    return res

def is_prime(n, k=5):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = powmod(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = mulmod(x, x, n)
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
    n = next_prime(start)
    while len(primes) < count:
        primes.append(n)
        n = next_prime(n + 2)
    return primes

def fibonacci(n, mod):
    if n == 0: return 0
    if n == 1: return 1
    
    def fib_helper(n):
        if n == 0: return (0, 1)
        a, b = fib_helper(n // 2)
        c = mulmod(a, (b * 2 - a) % mod, mod)
        d = (mulmod(a, a, mod) + mulmod(b, b, mod)) % mod
        return (d, (c + d) % mod) if n % 2 else (c, d)
    
    return fib_helper(n)[0]

def main():
    primes = generate_primes(START_PRIME, PRIME_COUNT)
    result = sum(fibonacci(p, MODULO) for p in primes) % MODULO
    print(result)

if __name__ == "__main__":
    main()