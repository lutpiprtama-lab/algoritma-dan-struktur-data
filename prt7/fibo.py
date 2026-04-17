n = int(input('masukan n : '))

s1=0
s2=0
fibo=1
i=1
while (i<=n) :
    print (fibo, end=' ')
    s1 = s2 
    s2 = fibo
    fibo = s1 + s2 
    i = 1 + 1 