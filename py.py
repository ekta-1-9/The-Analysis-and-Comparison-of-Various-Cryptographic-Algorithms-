#4 digit pin
from Crypto.Cipher import AES
import base64
import time

# Simulated plain text data
plain_text = "Sensitive information"

# Simulated encrypted data intercepted by the attacker
encrypted_data = b'xFgWBBq64YvMnZ5bJTvTGg=='

# Simulated brute-force attack on encrypted data
def brute_force_attack(encrypted_data):
    # Brute-force all 4-digit PINs
    for pin in range(10000):
        # Convert PIN to 4-digit string with leading zeros
        pin_str = str(pin).zfill(4)
        
        # Attempt decryption using the current PIN
        try:
            # Decrypt using AES with the current PIN as the key
            cipher = AES.new(pin_str.encode(), AES.MODE_ECB)
            decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data)).decode('utf-8')
            
            # Print the decrypted data and the corresponding PIN if successful
            print(f"Decrypted data: {decrypted_data}, PIN: {pin_str}")
            return True  # Return True if decryption is successful
        except:
            pass  # Ignore decryption errors (e.g., incorrect key)
    
    return False  # Return False if decryption fails for all PINs

# Define number of iterations
num_iterations = 5

# Loop for multiple iterations
for i in range(num_iterations):
    # Simulate unencrypted communication
    print(f"\nIteration {i+1}: Unencrypted Communication (Normal Data):")
    start_time = time.time()
    print(f"Sent from client to server: {plain_text}")
    end_time = time.time()
    unencrypted_time = end_time - start_time
    print(f"Time taken for attacker to intercept unencrypted data: {unencrypted_time:.2f} seconds")

    # Simulate encrypted communication
    print("\nEncrypted Communication:")
    start_time = time.time()

    # Attempt decryption of intercepted encrypted data
    if brute_force_attack(encrypted_data):
        print("Attacker successfully decrypted the encrypted data.")
    else:
        print("Attacker failed to decrypt the encrypted data.")

    end_time = time.time()
    encrypted_time = end_time - start_time
    print(f"Time taken for attacker to decrypt encrypted data: {encrypted_time:.2f} seconds")
