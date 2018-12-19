def fibonacci(n):
    if n<=1:
       return n
    else:
       return fibonacci(n-1)+fibonacci(n-2)
print("enter the number of terms you want in your fibonacci series:")
n=int(input())
if n<=0:
   print("please enter a valid number!!")
else:
    print("the series is:")
    for i in range(1,n+1,1):
        print(fibonacci(i))
