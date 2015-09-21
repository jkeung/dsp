[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

###Exercise 2.4 
Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen's d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

'''

df = nsfg.ReadFemPreg()
df
first = df[df.pregordr==1]
others = df[df.pregordr>1]

'''

Define Cohen Effect Size Function

'''

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

'''

Cohen's d for total weight in pounds

'''

CohenEffectSize(first['totalwgt_lb'], others['totalwgt_lb'])

'''

>> -0.06911825348820934

Cohen's d for pregnancy length

'''

CohenEffectSize(first['prglngth'], others['prglngth'])

'''

>> -0.03131178583370273


