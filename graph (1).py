import matplotlib.pyplot as plt

# Data
algorithms = ['ecdsa', 'sha', 'rsads', 'rsa', 'rc4', 'pgp', 'elgamalcns', 'eccns', 'dsa', 'diffievrsa', 'diffie', 'des', 'blowfish', 'aes', '3des']
encryption_times = [0.0, 0.0, 0.0040051937103271484, 0.0019762516021728516, 0.0, 0.0009999275207519531, 0.0009105205535888672, 0.008513927459716797, 0.0, 0.0009992122650146484, 0.0, 1.0008811950683595e-06, 0.0, 4.001855850219727e-06, 3.08990478515625e-06]
decryption_times = [0.0, None, 0.0, 0.002998828887939453, 0.0, 0.0010006427764892578, 0.0009996891021728516, 0.008514642715454102, 0.0, 0.0036051273345947266, 0.0, 9.61780548095703e-07, 3.009319305419922e-06, 2.0008087158203124e-06, 9.121894836425781e-07]
memory_usage = [24944640, 15880192, 22351872, 22589440, 15360000, 24862720, 16244736, 53035008, 24129536, 22118400, 15646720, 21155840, 21381120, 21348352, 21139456]
cpu_usage = [0.2, 16.0, 5.6, 14.2, 10.1, 4.7, 10.0, 10.9, 2.1, 2.9, 2.7, 2.5, 5.0, 1.9, 1.4]
key_generation_time = [0.0, 0.0, 0.172, 0.631, 0.0, 0.0, 0.305, 0.00499, 0.753, 0.479, 0.021, 0.0, 0.0, 0.0, 0.0]

# Creating subplots
fig, axs = plt.subplots(5, 1, figsize=(10, 20), sharex=True)

# Encryption Time
axs[0].plot(algorithms, encryption_times, marker='o', color='b', linestyle='-', label='Encryption Time')
axs[0].set_ylabel('Encryption Time (seconds)')
axs[0].legend()

# Decryption Time
axs[1].plot(algorithms, decryption_times, marker='o', color='r', linestyle='-', label='Decryption Time')
axs[1].set_ylabel('Decryption Time (seconds)')
axs[1].legend()

# Memory Usage
axs[2].plot(algorithms, memory_usage, marker='o', color='g', linestyle='-', label='Memory Usage')
axs[2].set_ylabel('Memory Usage (bytes)')
axs[2].legend()

# CPU Usage
axs[3].plot(algorithms, cpu_usage, marker='o', color='y', linestyle='-', label='CPU Usage')
axs[3].set_ylabel('CPU Usage (%)')
axs[3].legend()

# Key Generation Time
axs[4].plot(algorithms, key_generation_time, marker='o', color='m', linestyle='-', label='Key Generation Time')
axs[4].set_ylabel('Key Generation Time (seconds)')
axs[4].legend()

# Setting common title and x-axis label
fig.suptitle('Performance Metrics for Various Algorithms')
plt.xlabel('Algorithm')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
