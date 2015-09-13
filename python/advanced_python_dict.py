import csv
import pandas as pd
from pprint import pprint

# Question 6
df = pd.read_csv('faculty.csv', header = 0)
df['name'] = df['name'].map(lambda x:x.split()[-1])
df.columns = ['name', 'degree', 'title', 'email']
df2 = df.set_index('name')
# print df2
faculty_dict = df2.T.to_dict('list')
pprint(faculty_dict.items()[:3])

# Question 7
df = pd.read_csv('faculty.csv', header = 0)
df['name'] = df['name'].map(lambda x:(x.split()[-1], x.split()[0]))
df.columns = ['name', 'degree', 'title', 'email']
df2 = df.set_index('name')
faculty_dict = df2.T.to_dict('list')
pprint(faculty_dict.items()[:3])

# Question 8
df = pd.read_csv('faculty.csv', header = 0)
df['name'] = df['name'].map(lambda x:(x.split()[-1], x.split()[0]))
df.columns = ['name', 'degree', 'title', 'email']
df2 = df.set_index('name')
faculty_dict = df2.T.to_dict('list')
pprint([(key, faculty_dict[key]) for key in sorted(faculty_dict.keys())[:3]])