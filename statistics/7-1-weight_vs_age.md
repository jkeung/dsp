[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

Exercise 7.1 
Using data from the NSFG, make a scatter plot of birth weight versus mother's age. Plot percentiles of birth weight versus mother's age. Computer Pearson's and Spearman's correlations. How would you characterize the relationship between these variables?

'''
import nsfg
df = nsfg.ReadFemPreg()
age, weight = df.agepreg, df.totalwgt_lb
'''

Scatterplot for birth weight vs mother's age

'''
import thinkplot
thinkplot.Scatter(age, weight)
thinkplot.Show(xlabel = "Mother\'s age", ylabel = "Birth Weight")
'''

Plot percentile of births vs mother's age

'''
df = df.dropna(subset=['agepreg', 'totalwgt_lb'])
bins = np.arange(5, 50, 5)
indices = np.digitize(df.agepreg, bins)
groups = df.groupby(indices)

age = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' %percent
    thinkplot.Plot(age, weights, label = label) 
'''

Pearson and Spearman's correlations

'''
age.corr(weight, method = 'spearman')
'''

>> 0.094610041096582262

'''
age.corr(weight, method = 'pearson')
'''

>> 0.068833970354109111