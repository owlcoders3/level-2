def isprime(n):
    if n<2:
        return False
    for i in range(2,(int(n**(0.5)))+1):
        if n%i==0:
            return False
    return True
n=int(input())
if isprime(n):
    print(n)
else:
    l=[]
    for i in range(1,(int(n**(0.5)))+1):
        if n%i==0:
            if i*i==n:
                l.append(i)
            else:
                l.append(i)
                l.append(n//i)
    l.sort()
    for i in range(len(l)-1,-1,-1):
        if isprime(l[i]):
            print(l[i])
            break
