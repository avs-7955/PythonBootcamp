def prime_checker(number):
    is_prime = False
    for num in range(2, int(number/2)):
        if(number % num == 0):
            print(f"{number} is not a prime number.")
            is_prime = True
            break
    if(is_prime == False):
        print(f"{number} is a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
