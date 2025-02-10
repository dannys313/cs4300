import pytest

test = 9
assert test == 9
#function to utilize if stmts to determine positive an negative numbers
def test_num():

    num = input("Input number\n")

    if int(num) <  0:
        print("negative number\n")
        assert int(num) < 0
    elif int(num) > 0:
        print("positive number\n")
        assert int(num) > 0
    elif int(num) == 0:
        print("number is 0\n")
        assert int(num) == 0
    else:
        print("number not entered\n")

#functions to print out first 10 prime numbers (w/ help from chatgpt)
def prime_test(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

#prime numbers function continued (with help from chatgpt)
def test_calc_primes():
    count = 0
    number = 2
    prime_numbers = []

    while count < 10:
        if prime_test(number):
            prime_numbers.append(number)
            count += 1
        number += 1
            
    assert prime_numbers == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]