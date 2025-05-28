#Factorial using function

def factorial(n):
    if n<2:
        return 1
    else:
        return n* (factorial(n-1))

result=factorial(6)
print(result)