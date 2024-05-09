import random
import time
import psutil

def generate_prime_number(length):
    # Function to generate a prime number of specified length (in bits)
    while True:
        p = random.getrandbits(length)
        if is_prime(p):
            return p

def is_prime(n, k=5):
    # Miller-Rabin primality test
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Find r and s such that n-1 = 2^r * s
    s = n - 1
    r = 0
    while s % 2 == 0:
        r += 1
        s //= 2

    # Perform Miller-Rabin test k times
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def primitive_root(p):
    # Find a primitive root modulo p
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1

    while True:
        g = random.randint(2, p - 1)
        if not (pow(g, (p - 1) // p1, p) == 1):
            if not pow(g, (p - 1) // p2, p) == 1:
                return g

def generate_keys(p, g):
    # Generate public and private keys
    a = random.randint(2, p - 2)
    A = pow(g, a, p)
    return A, a

def generate_shared_secret(public_key, private_key, p):
    # Generate shared secret using public and private keys
    return pow(public_key, private_key, p)

# Measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    memory_usage = process.memory_info().rss
    return memory_usage

# Measure CPU usage
def measure_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Example usage
# Generate a large prime number and primitive root
start_time = time.time()
p = generate_prime_number(256)
g = primitive_root(p)
keygen_time = time.time() - start_time

# Key Generation Metrics
print("Key generation time:", keygen_time, "seconds")
print("Memory usage:", measure_memory_usage(), "bytes")
print("CPU usage:", measure_cpu_usage(), "%")

# Alice's key generation
start_time = time.time()
A, a = generate_keys(p, g)
alice_keygen_time = time.time() - start_time

# Bob's key generation
start_time = time.time()
B, b = generate_keys(p, g)
bob_keygen_time = time.time() - start_time

# Key Exchange Metrics
print("Alice's key generation time:", alice_keygen_time, "seconds")
print("Bob's key generation time:", bob_keygen_time, "seconds")
print("Memory usage:", measure_memory_usage(), "bytes")
print("CPU usage:", measure_cpu_usage(), "%")

# Exchange public keys
start_time = time.time()
shared_secret_Alice = generate_shared_secret(B, a, p)
shared_secret_Bob = generate_shared_secret(A, b, p)
exchange_time = time.time() - start_time

# Shared Secret Exchange Metrics
print("Shared Secret exchange time:", exchange_time, "seconds")
print("Memory usage:", measure_memory_usage(), "bytes")
print("CPU usage:", measure_cpu_usage(), "%")

# Verify shared secrets match
assert shared_secret_Alice == shared_secret_Bob
print("Shared Secret (Alice):", shared_secret_Alice)
print("Shared Secret (Bob):", shared_secret_Bob)
