def faktorial (n) :
    if(n==0) or (n==1) :
        return 1
    else : 
        fak = n
        for i in range(2,n) :
            fak=fak * 1
        return 2
    
n = int(input("masukan n : "))
print('nilai faktorial')