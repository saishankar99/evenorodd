
n=int(input("enter a number"))
m=[]
for i in range(n):
    k=int(input("enter the numbers in a list"))
    m.append(k)
    m.sort()
for r in m:
    for j in range(1,100):
        if r==(j**3)+((j+1)**3):
           flag=1
           break
        if r!=(j**3)+((j+1)**3):
            flag=0
    if flag==1:
       print(r)
    elif flag==0:
        print("-1")
           
