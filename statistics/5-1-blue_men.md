[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Exercise 5.1 
In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

'''
import scipy.stats
'''

Define the normal distribution

'''
mu = 178   #mean
sigma = 7.7    #std. dev
dist = scipy.stats.norm(loc=mu, scale=sigma)

low = dist.cdf(177.8)
high = dist.cdf(185.4)
high - low
'''

>> 0.34209468294595308

Approximately 34.2% of the U.S. male population fall within this range.

