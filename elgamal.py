import time
import psutil
import os
import math
import random
import hashlib

# Function to generate a large prime number
def generate_large_prime(bits):
    while True:
        potential_prime = random.getrandbits(bits)
        if is_prime(potential_prime):
            return potential_prime

# Miller-Rabin primality test
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Modular inverse
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# ElGamal Key Generation
def generate_keys(bits):
    p = generate_large_prime(bits)
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)
    h = pow(g, x, p)
    return (p, g, h, x)

# ElGamal Encryption
def encrypt(plaintext, p, g, h):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    s = pow(h, k, p)
    c2 = (plaintext * s) % p
    return (c1, c2)

# ElGamal Decryption
def decrypt(c1, c2, p, x):
    s = pow(c1, x, p)
    plaintext = (c2 * modinv(s, p)) % p
    return plaintext

if __name__ == "__main__":
    # Key Generation
    start_time_keygen = time.time()
    p, g, h, x = generate_keys(512)  # Adjust bits as needed
    end_time_keygen = time.time()

    # Encryption
    plaintext = random.randint(0, p - 1)
    start_time_encrypt = time.time()
    c1, c2 = encrypt(plaintext, p, g, h)
    end_time_encrypt = time.time()

    # Decryption
    start_time_decrypt = time.time()
    decrypted_plaintext = decrypt(c1, c2, p, x)
    end_time_decrypt = time.time()

    # Metrics
    keygen_time = end_time_keygen - start_time_keygen
    asymmetry_keygen_time = keygen_time / 2
    encryption_time = end_time_encrypt - start_time_encrypt
    decryption_time = end_time_decrypt - start_time_decrypt

    # Memory usage
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss

    # CPU usage
    cpu_usage = psutil.cpu_percent()

    # Other Metrics
    key_length = int(math.log2(p))
    entropy = hashlib.sha512(str(p).encode()).hexdigest()
    num_threads = 1  # Assuming single-threaded
    num_processes = os.cpu_count()

    print("Key generation time:", keygen_time, "seconds")
    print("Asymmetry in key generation time:", asymmetry_keygen_time, "seconds")
    print("Encryption time:", encryption_time, "seconds")
    print("Decryption time:", decryption_time, "seconds")
    print("Memory usage:", memory_usage, "bytes")
    print("CPU usage:", cpu_usage, "%")
    print("Key length:", key_length, "bytes")
    print("Entropy:", entropy)
    print("Number of threads used:", num_threads)
    print("Number of processes used:", num_processes)
