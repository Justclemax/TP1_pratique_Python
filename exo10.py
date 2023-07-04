def Fibonacci(n):
    if n== 0 or n==1:
        return 1
    else:
        return Fibonacci(n-1) +Fibonacci(n-2)
n = int( input('Entrer un nombre '))
res = Fibonacci(n)
print(res)