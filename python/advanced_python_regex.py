import pandas as pd

df = pd.read_csv('faculty.csv', header = 0)
df[' degree'] = df[' degree'].map(lambda x: x.replace('.','') )

# Question 1
array = list(df[' degree'])

collection = dict()
for items in array:
    for item in items.strip().split():
        if item in collection:
            collection[item] += 1
        else:
            collection[item] = 1

print collection

# Question 2
array2 = list(df[' title'])

collection2 = dict()
for items in array2:
    if items in collection2:
        collection2[items] += 1
    else:
        collection2[items] = 1

print collection2

# Question 3
emails = list(df[' email'])

print emails

# Question 4
domains = []
for email in emails:
    domains.append(email[email.index('@'):])

print set(domains)