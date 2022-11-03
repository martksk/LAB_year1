def Reduce_this_to_NestedListComprehension(N):
    primes = []
    for num in range(1,N):
        list_of_divisables = []
        for d in range(2,num):
            if num%d == 0: #divisable by some number
                list_of_divisables.append(d)
        if not list_of_divisables:
            primes.append(num)
    return primes        

def Problem2(N):
    primes = [i for i in range(1,N) if not [j for j in range(2,i) if i%j==0]]
    return primes