# Question 5
import csv

outfile = open( "emails.csv", "wb" )

thelist = ['bellamys@mail.med.upenn.edu',
 'warren@upenn.edu',
 'bryanma@upenn.edu',
 'jinboche@upenn.edu',
 'sellenbe@upenn.edu',
 'jellenbe@mail.med.upenn.edu',
 'ruifeng@upenn.edu',
 'bcfrench@mail.med.upenn.edu',
 'pgimotty@upenn.edu',
 'wguo@mail.med.upenn.edu',
 'hsu9@mail.med.upenn.edu',
 'rhubb@mail.med.upenn.edu',
 'whwang@mail.med.upenn.edu',
 'mjoffe@mail.med.upenn.edu',
 'jrlandis@mail.med.upenn.edu',
 'liy3@email.chop.edu',
 'mingyao@mail.med.upenn.edu',
 'hongzhe@upenn.edu',
 'rlocalio@upenn.edu',
 'nanditam@mail.med.upenn.edu',
 'knashawn@mail.med.upenn.edu',
 'propert@mail.med.upenn.edu',
 'mputt@mail.med.upenn.edu',
 'sratclif@upenn.edu',
 'michross@upenn.edu',
 'jaroy@mail.med.upenn.edu',
 'msammel@cceb.med.upenn.edu',
 'shawp@upenn.edu',
 'rshi@mail.med.upenn.edu',
 'hshou@mail.med.upenn.edu',
 'jshults@mail.med.upenn.edu',
 'alisaste@mail.med.upenn.edu',
 'atroxel@mail.med.upenn.edu',
 'rxiao@mail.med.upenn.edu',
 'sxie@mail.med.upenn.edu',
 'dxie@upenn.edu',
 'weiyang@mail.med.upenn.edu']

for item in thelist:
  outfile.write("%s\n" % item)

outfile.close()

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