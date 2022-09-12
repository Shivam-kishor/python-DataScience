def primes(start=2,stop=10):
    for num in range(start,stop):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            yield num

for p in primes(stop=100):
    print(p)