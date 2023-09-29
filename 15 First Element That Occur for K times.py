n,k=map(int,input().split())
l=list(map(int,input().split()))
d={}
ng=-1
for i in l:
    try:
        d[i]+=1
    except KeyError:
        d[i]=1
    if d[i]==k:
        ng=1
        print(i)
        break
if ng!=1:
    print(ng)
