def prime():
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                prime = ("This is not a prime number")
                return prime
                break
        else:
            prime = ("This is a prime number")
            return prime
    else:
        prime = ("This is not a prime number")
        return prime

num = int(input("Enter a number to test:"))
print(prime())