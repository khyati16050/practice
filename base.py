# for <var> in <iterable>

def getPrimeTill(n):
    # return a list containing prime numbers till n
    a = []
    for i in range(1, n + 1):
        if isPrime(i):
            a.append(i)
    return a


def isPrime(num):  # check if num is prime
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    # No number in the range (2,num) divide num
    # hence ,
    return True


print(getPrimeTill(100))

# In a list of number, check if the list is special ( always increasing and has 2 primes or always decreasing and has 1 prime)