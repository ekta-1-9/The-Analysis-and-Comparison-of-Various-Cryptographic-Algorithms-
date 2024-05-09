import time
import psutil

def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

def encrypt(message, key):
    key_stream = RC4(key)
    encrypted = bytearray()
    for char in message:
        encrypted.append(char ^ next(key_stream))
    return encrypted

def decrypt(encrypted, key):
    return encrypt(encrypted, key)  # Decryption is the same as encryption in RC4

# Measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    memory_usage = process.memory_info().rss
    return memory_usage

# Measure CPU usage
def measure_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

if __name__ == "__main__":
    message = b"Hello, World!"
    key = b"SecretKey"

    # Generate metrics for RC4 encryption
    start_time = time.time()
    encrypted_message = encrypt(message, key)
    encryption_time = time.time() - start_time
    encryption_memory = measure_memory_usage()
    encryption_cpu = measure_cpu_usage()

    # Generate metrics for RC4 decryption
    start_time = time.time()
    decrypted_message = decrypt(encrypted_message, key)
    decryption_time = time.time() - start_time
    decryption_memory = measure_memory_usage()
    decryption_cpu = measure_cpu_usage()

    # Display metrics
    print("Encryption time:", encryption_time, "seconds")
    print("Encryption memory usage:", encryption_memory, "bytes")
    print("Encryption CPU usage:", encryption_cpu, "%")
    print("Decryption time:", decryption_time, "seconds")
    print("Decryption memory usage:", decryption_memory, "bytes")
    print("Decryption CPU usage:", decryption_cpu, "%")
