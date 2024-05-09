import time
import psutil
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    memory_usage = process.memory_info().rss
    return memory_usage

# Measure CPU usage
def measure_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Key generation for RSA
def generate_rsa_keypair(key_size):
    start_time = time.time()
    key = RSA.generate(key_size)
    keygen_time = time.time() - start_time
    return key, keygen_time

# Encrypt message with RSA public key
def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message)
    return ciphertext

# Decrypt message with RSA private key
def decrypt_message(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Example usage
if __name__ == "__main__":
    # Generate RSA key pair
    key_size = 2048  # Choose key size (in bits)
    rsa_keypair, keygen_time = generate_rsa_keypair(key_size)
    private_key = rsa_keypair
    public_key = rsa_keypair.publickey()

    # Generate a random message to encrypt
    message = b"Hello, World!"

    # Encrypt the message with RSA public key
    start_time = time.time()
    ciphertext = encrypt_message(message, public_key)
    encryption_time = time.time() - start_time

    # Decrypt the ciphertext with RSA private key
    start_time = time.time()
    plaintext = decrypt_message(ciphertext, private_key)
    decryption_time = time.time() - start_time

    # Measure memory usage
    memory_usage = measure_memory_usage()

    # Measure CPU usage
    cpu_usage = measure_cpu_usage()

    # Display metrics
    print("Key generation time:", keygen_time, "seconds")
    print("Encryption time:", encryption_time, "seconds")
    print("Decryption time:", decryption_time, "seconds")
    print("Memory usage:", memory_usage, "bytes")
    print("CPU usage:", cpu_usage, "%")
