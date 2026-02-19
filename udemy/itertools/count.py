#count é um iterador sem fim (itertools)

from itertools import count

c1 = count()
r1 = range(10)

print('c1', hasattr(c1, '__iter__')) # true
print('c1', hasattr(c1, '__next__')) # true
print('r1', hasattr(r1, '__iter__')) # true
print('r1', hasattr(r1, '__next__')) # false

for i in c1:
  if i > 100:
    break
  print(i)
