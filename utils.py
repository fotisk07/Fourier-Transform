import numpy as np
import matplotlib.pyplot as plt

def signal(sinuses):
    # Create the singal as a sum of different sinuses
    t = np.linspace(0, 0.5, 800)
    s=0
    for i in range(len(sinuses)):
        s += np.sin(sinuses[i] * 2 * np.pi * t)

    # Plot the signal
    plt.style.use('seaborn')
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(1,1,1)

    ax.plot(t, s, label = r'$y=f(x)$')

    ax.set_title(" Signal ", fontsize = 20)
    ax.set_ylabel("Amplitude")
    ax.set_xlabel("Time [s]")

    ax.legend(loc='best')
    ax.grid(True)
    plt.show()
    fig.savefig('signal.png')
    return s, t

def Fourier(s, t):
    #Perform the Fourier Transform
    fft = np.fft.fft(s)
    T = t[1] - t[0]  # sample rate
    N = s.size

    # 1/T = frequency
    f = np.linspace(0, 1 / T, N)

    # Plot the signal Decomposition
    plt.style.use('seaborn')
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(1,1,1)

    ax.set_title(" Decomposed Signal ", fontsize = 20)
    ax.set_ylabel("Amplitude")
    ax.set_xlabel("Frequency [Hz]")

    ax.bar(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N, width=1.5)  # 1 / N is a normalization factor
    ax.grid(False)
    plt.show()
    fig.savefig("Decomposed_signal.png")
