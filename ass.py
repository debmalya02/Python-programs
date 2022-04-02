def remdup(l):
  n = []
  for i in l:
    if i not in n:
      n.append(i)
  return n


def sumsquare(l):
  n = []
  e = 0
  o = 0
  for i in l:
    if (i%2 == 0):
      e += i**2
    else:
      o += i**2
  n.append(o)
  n.append(e)
  return n


def transpose(m):
  result = [[[m[j][i] for j in range (len(m))] for i in range (len(m[0]))]]
  for r in result:
    print(r)