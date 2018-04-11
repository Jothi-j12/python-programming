n,a=int(input()).split(" ")
count=0
if(a<n):
  for i in range(a,n):
    if(n%i==0):
      count=i+1
      if(count!=0):
        print("no")
      else:
        print("yes")
else(n<a):
  for i in range(n,a):
    if(n%i==0):
        count=i+1
        if(count!=0):
          print("no")
        else:
          print("yes")
