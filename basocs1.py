n=int(input())
for i in range(2,n):
    if n%i==0:
       flag=1
       break
    elif n%i!=0:
       flag=0
if flag==1:
    print("yes")
else:
    print("no")
       
       
