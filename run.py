import argparse
import utils

ap=argparse.ArgumentParser(description="Arguments for running the visualisation script")

ap.add_argument('-s','--list',type=float,dest='s', nargs='+',help="The different sinuses to construct the signal", required=True)

pa = ap.parse_args()
sinuses = pa.s
print(sinuses)
s , t = utils.signal(sinuses)
utils.Fourier(s,t)
