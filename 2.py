N=7
a = [[0 for i in range(N)]for j in range(N-1)]
for j in range(N-1):
    for i in range(N):
        if i >= j:
            a[j][i] = (N-i+j)
        else:
            a[j][i] = (N-j+i)
for r in a:
    print(*r)