n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=l1+l2
l.sort()
ln=n*2
print(l[ln//2]+l[(ln//2)-1])
