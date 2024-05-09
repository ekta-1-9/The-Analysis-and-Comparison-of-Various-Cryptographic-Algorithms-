import matplotlib.pyplot as plt

# Data
algorithms = ['ecdsa', 'sha', 'rsads', 'rsa', 'rc4', 'pgp', 'elgamalcns', 'eccns', 'dsa', 'diffievrsa', 'diffie', 'des', 'blowfish', 'aes', '3des']
encryption_times = [0.0, 0.0, 0.0040051937103271484, 0.0019762516021728516, 0.0, 0.0009999275207519531, 0.0009105205535888672, 0.008513927459716797, 0.0, 0.0009992122650146484, 0.0, 1.0008811950683595e-06, 0.0, 4.001855850219727e-06, 3.08990478515625e-06]
decryption_times = [0.0, None, 0.0, 0.002998828887939453, 0.0, 0.0010006427764892578, 0.0009996891021728516, 0.008514642715454102, 0.0, 0.0036051273345947266, 0.0, 9.61780548095703e-07, 3.009319305419922e-06, 2.0008087158203124e-06, 9.121894836425781e-07]

# Removing None values from decryption_times
decryption_times = [time for time in decryption_times if time is not None]

# Plotting
plt.figure(figsize=(10, 6))

# Plotting each metric for each algorithm
for algo, enc, dec in zip(algorithms, encryption_times, decryption_times):
    plt.plot(['Encryption', 'Decryption'], [enc, dec], label=algo)

# Adding labels and title
plt.xlabel('Metrics')
plt.ylabel('Values')
plt.title('Encryption and Decryption Times for Various Algorithms')
plt.xticks(rotation=45)
plt.legend(loc="upper left")
plt.grid(True)

# Adjusting y-axis limits
plt.ylim(bottom=0, top=max(max(encryption_times), max(decryption_times)) * 1.1)

plt.tight_layout()
plt.show()
