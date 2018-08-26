import numpy as np
import matplotlib.pyplot as plt

def signal(sinuses):
    ''' This function creates a function f(x) = sin(a*pi*2)+sin(b*p*2)+...
     plots the graph of f(x) and saves it

    Args:
        sinuses(Float) : The list of constants a,b,c,...

    Returns:
        t (numpy array): X axis
        s (numpy array): Y axis
    '''
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

def Fourier(s, t, alg = "False"):
    '''This function performs the FFT in the function f(x) defined in signal function, plots and saves the figure

    Args:
        t (numpy array): X axis
        s (numpy array): Y axis
        alg (string): Variable to determine whether to use my FFT or numpy's
    '''

    #Perform the Fourier Transform
<<<<<<< HEAD
    if alg == "True":
        fft = FFT(s)
    else:
        fft = np.fft.fft(s)

||||||| merged common ancestors
    fft = np.fft.fft(s)
    fft = np.fft.fft(s)
=======
    fft = np.fft.fft(s)
>>>>>>> 052df911b6ac2efbbafd525dfdcc9d0a5a45b9ac
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

def FFT(x):
    """Compute the discrete Fourier Transform of the signal x

    Args:
        x (numpy array): The function f(x)

    Returns:
        M (numpy array): The FFT
    """

    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)
