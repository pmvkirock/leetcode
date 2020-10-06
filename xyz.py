def sss(m,n,quries):
    a = []
    ans = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append((i+1) * (j+1))
        a.append(b)
    
    for x in quries:
        if x[0] == 0:
            ans.append(min([min(r) for r in a]))
        elif x[0]== 1:
            for i in range(len(a[x[1]-1])):
                a[x[1]-1][i] = (n+n)*(m+m)
        elif x[0] == 2:
            for i in range(len(a)):
                a[i][x[1]-1] = (n+n)*(m+m)
    
    return ans


print(sss(6,1,[[1,1],[1,4],[0],[1,5],[1,2],[0]]))