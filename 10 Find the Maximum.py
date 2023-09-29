n=int(input())
k=int(input())
l=list(map(int,input().split()))
for i in range(n-k+1):
    print(max(l[i:i+k]),end=" ")
