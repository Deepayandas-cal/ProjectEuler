import random

MOD = 1234567891011
START = 10**14
LIMIT = 100000

def mod_mult(a, b, mod):
    return (a * b) % mod

def mod_exp(base, exp, mod):
    result = 1
    while exp:
        if exp % 2:
            result = mod_mult(result, base, mod)
        base = mod_mult(base, base, mod)
        exp //= 2
    return result

def is_prime(n, tests=5):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    for _ in range(tests):
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

def find_next_prime(n):
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n

def generate_primes(start, count):
    primes = []
    num = find_next_prime(start)
    while len(primes) < count:
        primes.append(num)
        num = find_next_prime(num + 2)
    return primes

def fibonacci(n, mod):
    if n in (0, 1):
        return n
    
    def fib_helper(n):
        if n == 0: return (0, 1)
        a, b = fib_helper(n // 2)
        c = mod_mult(a, (b * 2 - a) % mod, mod)
        d = (mod_mult(a, a, mod) + mod_mult(b, b, mod)) % mod
        return (d, (c + d) % mod) if n % 2 else (c, d)
    
    return fib_helper(n)[0]

def main():
    primes = generate_primes(START, LIMIT)
    result = sum(fibonacci(p, MOD) for p in primes) % MOD
    print(result)

if __name__ == "__main__":
    main()
