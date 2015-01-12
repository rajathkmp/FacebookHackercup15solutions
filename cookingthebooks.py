__author__ = 'RK'
for _ in range(int(input())):
    a = list(input())
    r = a[:]
    b = a.index(max(a))
    c = a[0]
    a[0] = max(a)
    a[b] = c
    b = ''.join(a)
    if min(r) < '1':
        h = min(n for n in r if n != min(r))
        x = int(r.index(h))
    else:
        x = r.index(min(r))
    y = r[0]
    r[0] = r[x]
    r[x] = y
    z = ''.join(r)
    i = 1
    print('Case #', i, ':', ' ', z, ' ', b)
    i += 1