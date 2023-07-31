def solve(a):
    if a%2==0:
        return a/2-1
    else:
        return int(a/2)

n=int(input(""))
l=[0]*n
for i in range(n):
    a=int(input(""))
    l[i]=int(solve(a))
print(*l,sep="\n")
    