def Problem3(N):
  primes = [i for i in range(1,N) if not [j for j in range(2,i) if i%j==0]]
  odd_dict_of_primes =  {k:v for (k,v) in dict(zip(range(len(primes)),primes)).items() if k%2!=0}  
  return odd_dict_of_primes

