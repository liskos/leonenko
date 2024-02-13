def alg(n):
  j=list()
  while ('52' in n) or ('2222' in n) or ('1111' in n):
    if '52' in n:
      n=n.replace('52','11',1)
      n=n.replace('2222', '5',1)
    else:
      n=n.replace('1112','2',1)
  j=[int(i) for i in n]
  return sum(j)

for i in range(4,10000):
  n='5'+('2'*i)
  print(alg(n))
