# Fourier Transform

The Fourier transform (FT) decomposes a function of time (a signal) into the frequencies that make it up, in a way similar to how a musical chord can be expressed as the frequencies (or pitches) of its constituent notes. In this sort repository I will be implementing a general Fourier Transform algorithm capable of decomposing a function $f(x)=\sin(a*2*\pi) + \sin(b*2*\pi) + \ldots$ in a, b, ... .

Here is an image of the man who came up with this idea.\
<img src="https://github.com/fotisk07/Fourier-Transform/blob/master/images/250px-Fourier2.jpg" height = "250"/>

## Prerequisites

The Code is written in Python 3.6.5 . If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.

To install pip run in the command Line
```
python -m ensurepip -- default-pip
```
to upgrade it
```
python -m pip install -- upgrade pip setuptools wheel
```
to upgrade Python
```
pip install python -- upgrade
```
Additional Packages that are required are: [Numpy](http://www.numpy.org/) and  [MatplotLib](https://matplotlib.org/)\

You can donwload them using [pip](https://pypi.org/project/pip/)
```
pip install numpy MatplotLib
```
or [conda](https://anaconda.org/anaconda/python)
```
conda install numpy MatplotLib
```

## Usage

* Create a fake signal and apply the fourier Transform with ```run.py```
  * Basic Usage : ```python run.py -s a b ... ```
  * Plots the signal, then the decomposition and saves the figures

## Examples

 ```python run.py -s 10 20``` \
 <img src="https://github.com/fotisk07/Fourier-Transform/blob/master/images/signal1.png" width="425"/> <img src="https://github.com/fotisk07/Fourier-Transform/blob/master/images/Decomposed_signal1.png" width="425"/>
 
 ```python run.py -s 50 200```\
 <img src="https://github.com/fotisk07/Fourier-Transform/blob/master/images/signa2.png" width="425"/> <img src="https://github.com/fotisk07/Fourier-Transform/blob/master/images/Decomposed_signal2.png" width="425"/>
 
 
 ```python run -s 100 20 30 50```\
 <img src="https://github.com/fotisk07/Fourier-Transform/blob/master/images/signa3.png" width="425"/> <img src="https://github.com/fotisk07/Fourier-Transform/blob/master/images/Decomposed_signal3.png" width="425"/>
 


## Contributing

Please read [CONTRIBUTING](https://github.com/fotisk07/Fourier-Transform/blob/master/CONTRIBUTING) for the process for submitting pull requests.

## Authors

* **Fotios Kapotos** - *Initial work*

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/fotisk07/fourier-Transform/blob/master/LICENSE) file for details
