def prime():
    prime_num=[2]
    ungerade=3
    while ungerade<100:
        is_prime = True
        for primezahl in prime_num:
            if ungerade/primezahl == ungerade//primezahl:
               is_prime=False
               break
        if is_prime:
            prime_num.append(ungerade)
        ungerade+=2
    return prime_num


def prime_factorization(num):
    factors=[]
    #zahl=input('Give me a number:')
    #if not str(num).isnumeric():
        #prime_factorization()
    #zahl=int(zahl)
    is_factorization=False
    while not is_factorization:
        for teiler in prime():
            if is_factorization:
                break
            while num/teiler==num//teiler:
                factors.append(teiler)
                num = num/teiler
                if num==1:
                    is_factorization=True
                    break
    if is_factorization:
        print(factors)
    return factors

#prime_factorization()

def Kgv():
    zahlen=input("Give me two numbers and put a komma between them:")
    (num1) = zahlen.split(',')[0]
    (num2) = zahlen.split(',')[1]
    num1=prime_factorization(int(num1))
    num2=prime_factorization(int(num2))
    kgv=1
    for prime_num in num1:
        if prime_num in num2:
            kgv*=prime_num
            num1.remove(prime_num)
            num2.remove(prime_num)
    num1 += num2
    for factor in num1:
        kgv*=factor
    print(kgv)
Kgv()