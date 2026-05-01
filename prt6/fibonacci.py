def fibonacci (n) :
    if n <=1:
        return n
    else :
        return fibonacci(n-2) + fibonacci (n-1)
    
n = int(input("masukan n : "))

for i in range (1, n+1):
    print(fibonacci(i),end=' ')