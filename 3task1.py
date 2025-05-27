#Factorial using function

def factorial(n):
    if n==0 or n==1:
        return
    else:
        return n*Factorial(n-1)
num=int(input("Enter a number:"))
print(F"Factorial of {num}is {factorial(num)}")