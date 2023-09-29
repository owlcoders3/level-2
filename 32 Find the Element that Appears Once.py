n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    try:
        d[i]+=1
    except KeyError:
        d[i]=1
for i in l:
    if d[i]==1:
        print(i)
        break
