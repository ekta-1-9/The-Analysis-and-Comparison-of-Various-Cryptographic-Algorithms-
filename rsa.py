import time
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import psutil
import threading
import random

def measure_memory_usage():
    process = psutil.Process()
    mem_usage = process.memory_info().rss
    return mem_usage

def measure_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage

def generate_rsa_keypair(key_size=2048):
    prime_start_time = time.time()
    key = RSA.generate(key_size)
    prime_end_time = time.time()
    keygen_time = prime_end_time - prime_start_time
    return key, keygen_time

def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    start_time = time.time()
    encrypted_message = cipher.encrypt(message.encode())
    end_time = time.time()
    encryption_time = end_time - start_time
    return encrypted_message, encryption_time

def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    start_time = time.time()
    decrypted_message = cipher.decrypt(encrypted_message)
    end_time = time.time()
    decryption_time = end_time - start_time
    return decrypted_message.decode(), decryption_time

def generate_and_measure_keys(key_size=2048):
    def generate_key():
        return generate_rsa_keypair(key_size)

    keygen_thread = threading.Thread(target=generate_key)
    start_time = time.time()
    keygen_thread.start()
    keygen_thread.join()
    end_time = time.time()
    key, keygen_time = generate_key()
    asymmetry_time = end_time - start_time - keygen_time

    # Count the number of threads and processes used
    num_threads = threading.active_count()
    num_processes = psutil.cpu_count(logical=True)

    return key, keygen_time, asymmetry_time, num_threads, num_processes

def main():
    # Generate RSA key pair
    key, keygen_time, asymmetry_time, num_threads, num_processes = generate_and_measure_keys()

    # Encrypt message
    message = "Hello, this is a test message."
    encrypted_message, encryption_time = encrypt_message(message, key.publickey())

    # Decrypt message
    decrypted_message, decryption_time = decrypt_message(encrypted_message, key)

    # Measure memory usage
    memory_usage = measure_memory_usage()

    # Measure CPU usage
    cpu_usage = measure_cpu_usage()

    # Calculate key length
    key_length = len(key.exportKey("PEM"))

    # Check entropy
    entropy = random.getrandbits(256)

    # Print metrics
    print("RSA key generation time:", keygen_time, "seconds")
    print("Asymmetry in key generation time:", asymmetry_time, "seconds")
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
