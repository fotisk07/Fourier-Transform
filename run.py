import argparse
import utils

# Initialize the Parser and add the argument
ap=argparse.ArgumentParser(description="Arguments for running the visualisation script")
ap.add_argument('-s','--list',type=float,dest='s', nargs='+',help="The different sinuses to construct the signal", required=True)
ap.add_argument("--n", type=str, dest="n",help="A boolean value to sepcify whether to use my own implementation of the FFT(True) or the numpy command(False)", default = "False")

# Get the different sinuses
pa = ap.parse_args()
sinuses = pa.s
n = pa.n


s , t = utils.signal(sinuses) # Create, plot and save the signal
utils.Fourier(s, t, n) # Decompose it, plot it and save it
