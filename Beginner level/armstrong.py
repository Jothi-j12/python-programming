n=int(input())
store=n
resut=0
count=0
while(n>0):
  count=count+1
  n=n//10
while(store>0):
digit=store%10
result=resut+digit**count
store=store//10
if(store==result):
    print("palindrome")
else:
    print("not a palindrome")
