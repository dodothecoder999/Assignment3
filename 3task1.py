#Factorial using function

def factorial(n):
    if n<2:
        return 1
    else:
        return n* (factorial(n-1))

result=factorial(6)
print(result)

OUTPUT
PS C:\Users\SANIYA\OneDrive\Desktop\dodothecoder> & "C:/Program Files/Python313/python.exe" c:/Users/SANIYA/OneDrive/Desktop/dodothecoder/3task1.py
720
