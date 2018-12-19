#code to find gcd of 2 numbers
def gcd(a,b):
    if b==0:
       return a
    elif a==0:
        return b
    else:
        return gcd(b,a%b)
print("enter first number:")
a=int(input())
print("enter second number:")
b=int(input())
print("gcd of the two numbers you entered is:",gcd(a,b))
