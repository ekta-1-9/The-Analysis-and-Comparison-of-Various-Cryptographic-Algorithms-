import time
import psutil
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    memory_usage = process.memory_info().rss
    return memory_usage

# Measure CPU usage
def measure_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Key generation for DSA
def generate_dsa_keypair(key_size):
    start_time = time.time()
    key = DSA.generate(key_size)
    keygen_time = time.time() - start_time
    return key, keygen_time

# Sign message with DSA private key
def sign_message(message, private_key):
    hash_obj = SHA256.new(message)
    signer = DSS.new(private_key, 'fips-186-3')
    start_time = time.time()
    signature = signer.sign(hash_obj)
    signing_time = time.time() - start_time
    return signature, signing_time

# Verify signature with DSA public key
def verify_signature(message, signature, public_key):
    hash_obj = SHA256.new(message)
    verifier = DSS.new(public_key, 'fips-186-3')
    start_time = time.time()
    try:
        verifier.verify(hash_obj, signature)
        verification_time = time.time() - start_time
        return True, verification_time
    except ValueError:
        return False, 0

# Example usage
if __name__ == "__main__":
    message = b"Hello, World!"

    # Generate DSA key pair
    key_size = 1024  # Choose key size (in bits)
    dsa_keypair, keygen_time = generate_dsa_keypair(key_size)
    private_key = dsa_keypair.export_key()
    public_key = dsa_keypair.publickey().export_key()

    # Sign the message with the private key
    signature, signing_time = sign_message(message, dsa_keypair)

    # Verify the signature with the public key
    verification_result, verification_time = verify_signature(message, signature, dsa_keypair.publickey())

    # Measure memory usage
    memory_usage = measure_memory_usage()

    # Measure CPU usage
    cpu_usage = measure_cpu_usage()

    # Display metrics
    print("Key generation time:", keygen_time, "seconds")
    print("Signing time:", signing_time, "seconds")
    print("Verification time:", verification_time, "seconds")
    print("Memory usage:", memory_usage, "bytes")
    print("CPU usage:", cpu_usage, "%")
