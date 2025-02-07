import pytest

#function to utilize if stmts to determine positive an negative numbers
def numtest():
    num = input("Input number\n")

    if int(num) <  0:
        print("negative number\n")
    elif int(num) > 0:
        print("positive number\n")
    elif int(num) == 0:
        print("number is 0\n")
    else:
        print("number not entered\n")

#function to print out first 10 prime numbers
def prime_test(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def calc_primes():
    count = 0
    number = 2
    prime_numbers = []

    while count < 10:
        if prime_test(number):
            prime_numbers.append(number)
            count += 1
        number += 1
            
    print(prime_numbers)

calc_primes()