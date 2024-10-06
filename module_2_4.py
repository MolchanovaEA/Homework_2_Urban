numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes=[]
not_primes=[]
is_prime=True
for i in range (len (numbers)):       # i - это индексы
    if numbers[i]==1:
        is_prime=True
        continue
    elif numbers[i]==2:
        is_prime = True
        primes.append(numbers[i])
    for j in range (2, numbers[i]):   # j - это делители
        if j == i and is_prime==True:
            primes.append(numbers[i])
        if numbers[i] % j == 0:
            is_prime=False
            not_primes.append(numbers[i])
            break
        else:
            is_prime=True
            continue
print('Primes: ', primes)
print('Not primes: ', not_primes)
