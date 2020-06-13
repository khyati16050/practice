# In a list of number, check if the list is special ( always increasing and has 2 primes or always decreasing and has 1 prime)

def increasing(a):
    if len(a) < 2:
        return True
    else:
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                return False
    return True


def decreasing(a):
    if len(a) < 2:
        return True
    else:
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                return False
    return True


def check_special(a):
    check_bool = False
    if (increasing(a)):
        count = 0
        for i in range(len(a)):
            if (isPrime(a[i])):
                count += 1
        if (count == 2):
            check_bool = True
    if (decreasing(a)):
        count = 0
        for i in range(len(a)):
            if (isPrime(a[i])):
                count += 1
        if (count == 1):
            check_bool = True
    return check_bool


def isPrime(num):  # check if num is prime
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    # No number in the range (2,num) divide num
    # hence ,
    return True


a = [1, 2, 4, 5, 6]
print(check_special(a))
# print(increasing(a))
# print(decreasing(a))
