# -*- coding: utf-8 -*-
"""d3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HWY8zQZS-pKkZ66tYq_ORCZ9J8NcRlgB
"""

with open('inputd{}.txt'.format(3), 'r') as f:
    lines = f.readlines()

import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

t1 = dict(zip(lower+upper, list(range(1,53))))

s=0
s2=0
c3=0
tmp=[]

for line in lines:
  ll = list(line)[:-1]

  # part one
  half = int(len(ll)/2)
  com = set(ll[:half]).intersection(set(ll[half:]))
  s += t1[str(list(com)[0])]

  # part two
  tmp.append(set(ll))
  c3+=1
  if(c3==3):
    c3=0
    com3 = set.intersection(*map(set,tmp))
    s2 += t1[str(list(com3)[0])]
    tmp=[]

print('Part one:')
print(s)

print('*-'*30)


print('Part Two:')
print(s2)