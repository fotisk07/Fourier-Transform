import argparse
import utils

# Initialize the Parser and add the argument
ap=argparse.ArgumentParser(description="Arguments for running the visualisation script")
ap.add_argument('-s','--list',type=float,dest='s', nargs='+',help="The different sinuses to construct the signal", required=True)

# Get the different sinuses
pa = ap.parse_args()
sinuses = pa.s


s , t = utils.signal(sinuses) # Create, plot and save the signal
utils.Fourier(s,t) # Decompose it, plot it and save it
