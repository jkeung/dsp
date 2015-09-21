[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Exercise 3.1: Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.

```
%matplotlib inline

import chap01soln
import thinkstats2
resp = chap01soln.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh)
pmf
```

>> Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})

Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household

Define BiasPmf

```
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
```

Make a the biased Pmf of children in the household, as observed if you surveyed the children instead of the respondents.

```
biased = BiasPmf(pmf, label = 'biased')
```

Display the actual Pmf and the biased Pmf on the same axes.

import thinkplot
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,biased])
thinkplot.Show()

Compute the means of the two Pmfs.

```
pmf.Mean()
```

>> 1.0242051550438309

```
biased.Mean()
```

>> 2.4036791006642821


