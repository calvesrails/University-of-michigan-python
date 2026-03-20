
# l1 = [1, 2 ,2 , 2, 3, 3, 4, 4, 5]
# s1 = set(l1)
# l2 = list(s1)

s1 = set()

s1.add('luiz')
s1.update(('olá mundo', 1, 2345))

# s1.clear()

s1.discard('luiz')
print(s1)