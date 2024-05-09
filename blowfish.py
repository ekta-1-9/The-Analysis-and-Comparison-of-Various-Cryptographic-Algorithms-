import time
import psutil
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes

# Blowfish Key Generation
def generate_blowfish_key(key_length):
    start_time = time.time()
    key = get_random_bytes(key_length)
    keygen_time = time.time() - start_time
    return key, keygen_time

# Blowfish Encryption
def encrypt(message, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    # Pad the message to be a multiple of 8 bytes (Blowfish block size)
    padded_message = message + b"\0" * (Blowfish.block_size - len(message) % Blowfish.block_size)
    start_time = time.time()
    ciphertext = cipher.encrypt(padded_message)
    encryption_time = time.time() - start_time
    return ciphertext, encryption_time

# Blowfish Decryption
def decrypt(ciphertext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    start_time = time.time()
    plaintext = cipher.decrypt(ciphertext)
    decryption_time = time.time() - start_time
    return plaintext.rstrip(b"\0"), decryption_time

# Measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    memory_usage = process.memory_info().rss
    return memory_usage

# Measure CPU usage
def measure_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Generate Blowfish key
key_length = 16  # 128 bits key
blowfish_key, keygen_time = generate_blowfish_key(key_length)

# Encrypt and decrypt message multiple times
num_iterations = 1000
total_encryption_time = 0
total_decryption_time = 0
for _ in range(num_iterations):
    # Encrypt message
    message = b'Hello, World!'
    ciphertext, encryption_time = encrypt(message, blowfish_key)
    total_encryption_time += encryption_time

    # Decrypt message
    plaintext, decryption_time = decrypt(ciphertext, blowfish_key)
    total_decryption_time += decryption_time

# Measure memory usage
memory_usage = measure_memory_usage()

# Measure CPU usage
cpu_usage = measure_cpu_usage()

# Display metrics
print("Key generation time:", keygen_time, "seconds")
print("Average encryption time per iteration:", total_encryption_time / num_iterations, "seconds")
print("Average decryption time per iteration:", total_decryption_time / num_iterations, "seconds")
print("Memory usage:", memory_usage, "bytes")
print("CPU usage:", cpu_usage, "%")
