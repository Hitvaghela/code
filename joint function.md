l=input().split()
l=[int(i) for i in l]
l.sort()
a=[0]*(len(l)-1)
for i in range(len(l)-1):
    a[i]=l[len(l)-1]-l[i]

print(' '.join(map(str,a)))


// first it convert list into string than they joint by ' ' 
