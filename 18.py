#no
#ArmsTrongInTERval
a=input().split()
b=int(a[0])
c=int(a[1])
for num in range(b,c):
  temp=num
  sum=0
  while temp>0:
      digit=temp%10
      sum=sum+digit**3
      temp=temp//10
      if sum==num:
           print (num)
