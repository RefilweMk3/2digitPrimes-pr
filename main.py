def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

two_digit_primes = []
for number in range(10,100):
    if is_prime(number):
        two_digit_primes.append(number)

print("Two digit prime numbers are:", two_digit_primes)