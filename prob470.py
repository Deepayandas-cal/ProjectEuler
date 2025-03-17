from typing import Tuple

def fpm(b: int, e: int, m: int) -> int:
    """
    Fast modular exponentiation: Computes (b^e) % m efficiently.
    """
    t = 1
    while e > 0:
        if e & 1:  # If the current bit of the exponent is 1
            t = (t * b) % m  # Multiply the result by the base
        b = (b * b) % m  # Square the base
        e >>= 1  # Shift the exponent to the right
    return t

def chkmin(a: float, b: float) -> Tuple[float, bool]:
    """
    Returns the smaller value (minimum) between a and b, and a flag indicating if a was updated.
    """
    if a > b:
        return b, True
    return a, False

def chkmax(a: float, b: float) -> Tuple[float, bool]:
    """
    Returns the larger value (maximum) between a and b, and a flag indicating if a was updated.
    """
    if a < b:
        return b, True
    return a, False

def sqr(x: float) -> float:
    """Computes the square of a given number."""
    return x * x

def gcd(x: int, y: int) -> int:
    """
    Computes the greatest common divisor (GCD) using the Euclidean algorithm.
    """
    while x != 0:
        t = x  # Temporary variable
        x = y % x
        y = t
    return y

class Graph:
    """
    Represents an undirected graph using an adjacency list.
    """
    def __init__(self, n: int = 0):
        # Initialize the adjacency list with n + 5 empty lists
        self.adj = [[] for _ in range(n + 5)]

    def resize(self, n: int):
        """Resizes the graph to accommodate n + 5 nodes."""
        self.adj = [[] for _ in range(n + 5)]

    def add(self, s: int, e):
        """Adds an edge between nodes s and e."""
        self.adj[s].append(e)

    def delete(self, s: int, e):
        """Removes an edge between nodes s and e."""
        self.adj[s].remove(e)

    def __getitem__(self, t: int):
        """Allows access to the adjacency list of node t."""
        return self.adj[t]

# Constants for the problem
N = 20
w = [0] * (N + 1)  # Helper array for bit manipulation

def R(S: int, c: float) -> float:
    """
    Recursive function to calculate a value based on a bitmask S
    and a penalty constant c.
    """
    ret = 0.0  # Maximum value to be calculated
    E = 0.0  # Expected value
    n = 0  # Number of bits in S
    t = bin(S).count('1')  # Count the number of 1s in S

    # Populate the bitmask array
    while S >> n:
        w[n + 1] = (S >> n) & 1
        n += 1

    # If the penalty is zero, return the number of bits
    if c == 0:
        return n

    T = 1  # Iteration counter
    while True:
        cur = 0.0
        # Compute the current value based on the bitmask
        for i in range(1, n + 1):
            if w[i]:
                cur += max(float(i), E)
        cur /= t  # Normalize the value
        E = cur
        # Update the maximum value
        if ret < E - c * T:
            ret = E - c * T
        else:
            break
        T += 1
    return ret

# Array to store intermediate results
f = [0.0] * (N + 2)
# Combination values
cb = [[0] * (N + 2) for _ in range(N + 2)]

def main():
    """Main function to calculate and output results."""
    ans = 0.0
    # Precompute combinations
    for i in range(N + 1):
        for j in range(i + 1):
            if j == 0:
                cb[i][j] = 1  # Base case for combinations
            else:
                cb[i][j] = cb[i - 1][j - 1] + cb[i - 1][j]

    # Iterate over values of d
    for d in range(4, N + 1):
        f[1] = d
        # Compute intermediate values for f
        for i in range(1, d):
            f[i + 1] = (f[i] - f[i - 1] * (d - i + 1) / d) * d / (i + 1)
        # Normalize f values
        for i in range(1, d + 1):
            f[i] /= cb[d][i]

        # Iterate over values of c
        for c in range(N + 1):
            cur = 0.0
            # Sum up values for all subsets of size d
            for S in range(1, 1 << d):
                t = bin(S).count('1')
                cur += f[t] * R(S, c)
            print(f"{d} {c} {cur}")  # Output results for d and c
            ans += cur
    print(ans)  # Output the final result

if __name__ == "__main__":
    main()