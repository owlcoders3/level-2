s=input()
sub=input()
if s==sub:
    print(1)
else:
    l=len(sub)
    flag=0
    for i in range(len(s)-l+1):
        if s[i:i+l]==sub:
            flag=1
            print(flag)
            break
    if flag==0:
        print(0)
