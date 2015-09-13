# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

* Lists and tuples are similar because they both hold an array of values. 
* They differ because tuples are immutable, they cannot be changed or edited, only recreated. 
* Tuples are used as keys in dictionaries because the keys in dictionaries are immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

* Python lists and sets are similar because they are both a collection of elements. 
* They differ because lists can contain duplicates and are ordered, whereas sets only contain unique values and are unordered. 
* Sets are faster in terms of finding if an element exists, but is slower when it comes to iterating over its contents. This is because sets are unordered.

* List Example:
['a','b','c','a','b']

* Set Example:
['a','b','c']

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

* Lambda is an anonymous function that is used to create functions "on-the-fly". Here is an example:
g = lambda x:x*2
g(3)
6

* x = [2,4,6,1,3,5]
f = lambda x:sorted(x)
f(x)
[1,2,3,4,5,6]

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

* A list comprehension is a concise way to create a list.
Ex. 1
INPUT: arr = [1,2,3]
[x + 1 for x in arr if x >= 2]
OUTPUT: [3, 4]

* 'map' equivalent example:
INPUT:def add_one(x):
    return x+1
map(add_one, arr)
OUTPUT: [2, 3, 4]

* 'filter' equivalent example:
INPUT: filter(lambda x: x>=2, x)
OUTPUT: [2, 3]

* Set comprehension example:
INPUT: a = {x for x in 'abcdefghijk' if x not in 'abc'}
a
OUTPUT: set(['e', 'd', 'g', 'f', 'i', 'h', 'k', 'j'])

* Dictionary comprehension example:
INPUT: d = {n: n**2 for n in range(5)}
d
OUTPUT: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  
```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937


b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





