import time
import hashlib
import os
import psutil

from sympy import mod_inverse
from sympy import isprime
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

def point_addition(P, Q, curve):
    if P is None:
        return Q
    if Q is None:
        return P
    if P.x == Q.x and P.y != Q.y:
        return None

    if P.x == Q.x:
        m = (3 * P.x**2 + curve.a) * mod_inverse(2 * P.y, curve.p)
    else:
        m = (Q.y - P.y) * mod_inverse(Q.x - P.x, curve.p)

    x = (m**2 - P.x - Q.x) % curve.p
    y = (m * (P.x - x) - P.y) % curve.p
    return Point(x, y)

def scalar_multiply(k, P, curve):
    if k == 0 or P is None:
        return None
    if k == 1:
        return P

    Q = None
    R = P
    while k:
        if k & 1:
            Q = point_addition(Q, R, curve)
        R = point_addition(R, R, curve)
        k >>= 1
    return Q

def generate_keys(curve):
    private_key = random.randint(1, curve.p - 1)
    public_key = scalar_multiply(private_key, curve.g, curve)
    return (private_key, public_key)

def encrypt(public_key, plaintext, curve):
    k = random.randint(1, curve.p - 1)
    c1 = scalar_multiply(k, curve.g, curve)
    c2 = point_addition(plaintext, scalar_multiply(k, public_key, curve), curve)
    return (c1, c2)

def decrypt(private_key, curve, c1, c2):
    s = scalar_multiply(private_key, c1, curve)
    inverse = mod_inverse(s.x, curve.p)
    return point_addition(c2, scalar_multiply(inverse, c1, curve), curve)

def main():
    p = 233970423115425145524320034830162017933
    a = -95051
    b = 11279326
    G = Point(182, 85518893674295321206118380980485522083)
    curve = EllipticCurve(a, b, p)
    curve.g = G  

    start_time_keygen = time.time()
    private_key, public_key = generate_keys(curve)
    end_time_keygen = time.time()

    plaintext = Point(192, 10507756419667021335617425864029694432)
    start_time_encrypt = time.time()
    c1, c2 = encrypt(public_key, plaintext, curve)
    end_time_encrypt = time.time()

    start_time_decrypt = time.time()
    decrypted_plaintext = decrypt(private_key, curve, c1, c2)
    end_time_decrypt = time.time()

    keygen_time = end_time_keygen - start_time_keygen
    asymmetry_keygen_time = keygen_time / 2
    encryption_time = end_time_encrypt - start_time_encrypt
    decryption_time = end_time_decrypt - start_time_decrypt

    memory_usage = psutil.Process(os.getpid()).memory_info().rss
    cpu_usage = psutil.cpu_percent()

    key_length = private_key.bit_length() // 8
    entropy = hashlib.sha512(str(private_key).encode()).hexdigest()
    num_threads = 1  
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

if __name__ == "__main__":
    main()
