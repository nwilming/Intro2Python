%matplotlib inline
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from pylab import *

'''
No. 1: Curve fitting
'''

from scipy.optimize import *

def fitFunc(t, a, b, c):
    return a*np.exp(-b*t) + c
    
t = np.linspace(0,4,50)
temp = fitFunc(t, 5.0, 1.5, 0.5)
noisy = temp + 0.25*np.random.normal(size=len(temp))
fitParams, fitCovariances = curve_fit(fitFunc, t, noisy)
print ' fit coefficients:\n', fitParams
print ' Covariance matrix:\n', fitCovariances

figure()
errorbar(t, noisy, fmt = 'ro', yerr = 0.2) # plot the data as red circles with vertical errorbars
plot(t, fitFunc(t, fitParams[0], fitParams[1], fitParams[2])) # now plot the best fit curve
ylabel('Temperature (C)',)
xlabel('time (s)',)
xlim(0,4.1)


'''
No. 2: Interpolation
'''

from scipy.interpolate import *

def f(x):
    return sin(x)
    
n = arange(0, 10)  
x = linspace(0, 9, 100)

y_meas = f(n) + 0.1 * randn(len(n)) # simulate measurement with noise
y_real = f(x)

linear_interpolation = interp1d(n, y_meas)
y_interp1 = linear_interpolation(x)

cubic_interpolation = interp1d(n, y_meas, kind='cubic')
y_interp2 = cubic_interpolation(x)

figure()
plot(n, y_meas, 'bs', label='noisy data')
plot(x, y_real, 'k', lw=2, label='true function')
plot(x, y_interp1, 'r', label='linear interp')
plot(x, y_interp2, 'g', label='cubic interp')
legend(loc=3)


'''
No. 3: Fourier transform
'''

from scipy.fftpack import *

N = 300 # number of samplepoints
T = 1 / 1000.0 # sample spacing
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

figure()
plot(x,y)
title('Signal')
xlabel('Time (s)')
ylabel('Amplitude (a.u.)')

yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

figure()
plot(xf, 2.0/N * np.abs(yf[:N//2]))
title('Fourier transform')
xlabel('Frequency (s)')
ylabel('Amplitude (Hz)')

# Window functions:
from scipy.signal import blackman, hann
w = blackman(N)
yf_window = fft(w*y)
yf_hann = fft(hann(N)*y)

'''
No. 4: Statistics
'''

from scipy.stats import *

# T-TEST:

x1 = np.random.normal(loc=0, scale=1, size=100)
x2 = np.random.normal(loc=.5, scale=1, size=100)

figure()
hist(x1, bins=10, alpha=0.5, label='x1')
hist(x2, bins=10, alpha=0.5, label='x2')
legend()

t, p = ttest_ind(x1, x2)
print('x1 vs x2\nind. t-test: t = {}; p = {}'.format(round(t,4), round(p,4)))

t, p = ttest_rel(x1, x2)
print('x1 vs x2\npaired t-test: t = {}; p = {}'.format(round(t,4), round(p,4)))

t, p = ttest_1samp(x1, 0)
print('x1 vs 0\n1 sample t-test: t = {}; p = {}'.format(round(t,4), round(p,4)))

t, p = ttest_1samp(x2, 0)
print('x2 vs 0\n1 sample t-test: t = {}; p = {}'.format(round(t,4), round(p,4)))

# REGRESSION:

x = np.random.normal(loc=0, scale=1, size=50)
y = x + np.random.normal(loc=0, scale=2, size=50)

r, p = pearsonr(x, y)
print('correlation x and y\npearson r = {}; p = {}'.format(round(r,4), round(p,4)))

r, p = spearmanr(x, y)
print('correlation x and y\nspearman r = {}; p = {}'.format(round(r,4), round(p,4)))

figure()
plot(x,y,'o')
xlabel('x (a.u.)')
ylabel('y (a.u.)')

# calc the trendline
z = polyfit(x, y, 1)
p = poly1d(z)
plot(x,p(x),"r")
