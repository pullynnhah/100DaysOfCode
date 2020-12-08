def prime_checker(number):
    divisors = 0
    for div in range(1, number + 1):
        if number % div == 0:
            divisors += 1

    if divisors == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
