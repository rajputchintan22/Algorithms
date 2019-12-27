def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def sum_of_primes(num):
    isPrime = 1
    for i in range(2, int(num / 2), 1):
        if num % i == 0:
            isPrime = 0
            break
    return isPrime


for t in range(0, int(input())):
    size_of_arrays = int(input())
    array = list(map(int, input().split()))
    prime_pos = []
    primes = []
    for i in range(0, size_of_arrays):
        if is_prime(array[i]):
            prime_pos.append(i)
            primes.append(array[i])
    special_prime_pos = []
    special_prime = []
    if len(primes) > 0:
        for i in range(0, len(primes)):
            if sum_of_primes(primes[i]):
                special_prime_pos.append(prime_pos[i])
                special_prime.append(primes[i])
        special_prime.sort()
        for i in range(0, len(special_prime_pos)):
            array[special_prime_pos[i]] = special_prime[i]
    print(*array)
