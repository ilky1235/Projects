# Author: Ian Lee Kim Yen
# Prime Factorisation
# Date: 14/8/2025


def is_prime(num):
    '''
    Checks to see if the number given is a prime number or not
    '''
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True
    

def prime_factorisation(num):   
    prime_factors = []
    for i in range(2, num + 1):
        if num == 1:
            break

        else:
            if is_prime(i):
                if num % i == 0:
                    while num % i == 0:
                        if num == 1:
                            break
                        num = num / i
                        prime_factors.append(i)

                else:
                    continue


                


    return prime_factors
            


def main():
    num = int(input("Please enter your number: "))

    test = prime_factorisation(num)
    print(test)


if __name__ == "__main__":
    main()

    