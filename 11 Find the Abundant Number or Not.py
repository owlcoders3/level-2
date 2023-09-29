n=int(input())
tg=0
for i in range(1,(int((n**(0.5))))+1):
    if n%i == 0:
        if i*i == n:
            tg+=i
        else:
            tg+=i
            if n//i != n:
                tg+=(n//i)
if tg>n:
    print(True)
else:
    print(False)
