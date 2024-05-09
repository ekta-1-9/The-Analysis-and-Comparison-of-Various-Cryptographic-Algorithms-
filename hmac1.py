import time
import psutil
import hmac
import hashlib

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
if __name__ == "__main__":
    message = b"Hello, World!"
    key = b"SecretKey"

    # Compute HMAC-SHA256
    start_time = time.time()
    hmac_sha256 = hmac.new(key, message, hashlib.sha256).hexdigest()
    hashing_time = time.time() - start_time

    # Measure memory usage
    memory_usage = measure_memory_usage()

    # Measure CPU usage
    cpu_usage = measure_cpu_usage()

    # Display metrics
    print("HMAC-SHA256:", hmac_sha256)
    print("Hashing time:", hashing_time, "seconds")
    print("Memory usage:", memory_usage, "bytes")
    print("CPU usage:", cpu_usage, "%")
