'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
n=int(input(""))
a=input("")
a=a.upper()
b=[str(a[i]) for i in range(len(a))]
if len(set(b))==26:
    print("YES")
else:
    print("NO")

