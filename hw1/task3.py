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
def primetest():
    test = 2
    num = 0
    while num < 10:
        for i in range(2, int(test**0.5) + 1):
            if test % i != 0:
                print("{test}\n")
                num += 1   
        test += 1
            
        

primetest()