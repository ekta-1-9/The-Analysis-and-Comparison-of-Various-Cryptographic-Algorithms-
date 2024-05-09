import time
import psutil
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import hashes

# Measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    memory_usage = process.memory_info().rss
    return memory_usage

# Measure CPU usage
def measure_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Generate ECDSA key pair
def generate_ecdsa_keypair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

# Sign message with ECDSA private key
def sign_message(message, private_key):
    start_time = time.time()
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    signing_time = time.time() - start_time
    return signature, signing_time

# Verify signature with ECDSA public key
def verify_signature(message, signature, public_key):
    start_time = time.time()
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        verification_time = time.time() - start_time
        return True, verification_time
    except:
        return False, 0

# Example usage
if __name__ == "__main__":
    # Generate ECDSA key pair
    private_key, public_key = generate_ecdsa_keypair()

    # Generate a random message to sign
    message = b"Hello, World!"

    # Sign the message with the private key
    signature, signing_time = sign_message(message, private_key)

    # Verify the signature with the public key
    verification_result, verification_time = verify_signature(message, signature, public_key)

    # Measure memory usage
    memory_usage = measure_memory_usage()

    # Measure CPU usage
    cpu_usage = measure_cpu_usage()

    # Display metrics
    print("Signing time:", signing_time, "seconds")
    print("Verification time:", verification_time, "seconds")
    print("Memory usage:", memory_usage, "bytes")
    print("CPU usage:", cpu_usage, "%")
