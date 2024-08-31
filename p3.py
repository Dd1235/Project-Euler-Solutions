import math


# not used in this solution
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    # the smallest prime factor of a number n is less than or equal to sqrt(n)
    # if smallest prime factor of this number is 5, then this number has to be greater than 25, else it is prime
    # all prime number are in the form of 6k +/- 1
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def largest_prime_factor(n):
    largest = None
    # Check for number of 2s that divide n
    while n % 2 == 0:
        largest = 2
        n //= 2
    # Check for odd factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest = i
            n //= i
    # If n is a prime number greater than 2
    if n > 2:
        largest = n
    return largest


if __name__ == "__main__":
    number = 600851475143
    print(largest_prime_factor(number))
