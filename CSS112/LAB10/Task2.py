N=100
primes = [(i,j,k) for i in range(1,N) if not k for j in range(2,num) if i%j ==0]
# for num in range(1,N):
#     list_of_divisables = []
#     for d in range(2,num):
#         if num%d == 0: #divisable by some number
#             list_of_divisables.append(d)
#     if not list_of_divisables:
#         primes.append(num)
        
print(primes)