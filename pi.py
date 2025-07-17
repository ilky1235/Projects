# Using the Chudnovsky Algorithm to derive Pi
# Author: Ian Lee Kim Yen
# Date: 17/7/2025

from decimal import *
import math


iteration_divider = 14.18

def factorial(n):
    '''
    Function to calculate the factorial (trying out recursion)
    '''
    if n == 0:
        return Decimal(1)
    
    return n * factorial(n-1)


    
def calc_pi(number):
    '''
    Function to calculate pi
    '''
    getcontext().prec = number
    # Each term of the Chudnovsky Algorithm adds ~14.18 decimal digits to pi

    iterations = math.ceil(number / iteration_divider)
    if iterations < 1:
        iterations = 1

    sum = 0
    
    for i in range(iterations):
        a = Decimal(-1)** Decimal(i)
        b = factorial(Decimal(6) * Decimal(i))
        c = Decimal(13591409) + (Decimal(545140134) * Decimal(i))
        d = factorial(Decimal(3) * Decimal(i))
        e = factorial(Decimal(i)) ** 3
        ff = (Decimal(3) * Decimal(i)) + (Decimal(3) / Decimal(2))
        f = Decimal(640320)**ff

        
        sum += (a * b * c) / (d* e * f)
        

    sum = sum * 12
    pi = 1/sum
    return pi


def main():
    num = int(input("Please input the number of decimals you want for pi: "))
    pi_dec = calc_pi(num)
    print(pi_dec)


if __name__ == "__main__":
    main()






