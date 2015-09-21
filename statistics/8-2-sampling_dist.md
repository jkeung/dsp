[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

Exercise 8.2

Suppose you draw a sample with size $n=10$ from a population 
with an exponential disrtribution with $\lambda=2$.  Simulate
this experiment 1000 times and plot the sampling distribution of
the estimate L.  Compute the standard error of the estimate
and the 90\% confidence interval.

Repeat the experiment with a few different values of $n$ and make
a plot of standard error versus $n$.

```
L = []
n = 10
lam = 2
times = 1000
for x in range(times):
    xs = np.random.exponential(1.0/lam, n)
    lamhat = 1.0 / np.mean(xs)
    L.append(lamhat)
cdf = thinkstats2.Cdf(L)
thinkplot.Cdf(cdf)
```

Compute the standard error

```
from estimation import RMSE, MeanError
stderr = RMSE(estimates, lam)
stderr
```

>> 0.8173442114393894

Compute 90% Confidence Interval

```
ci = cdf.Percentile(5), cdf.Percentile(95)
print('confidence interval', ci)
```

>> ('confidence interval', (1.2828718233973802, 3.7511282393274685))

