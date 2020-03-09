#!/usr/bin/python

def isPrime(n):
    
    '''Takes a natural number and returns true if it
       is a prime number and false otherwise
    '''
    
    if(n > 1):
        for i in range(2, n):
            if(n % i) == 0:
                return False
        else:
            return True
    else:
        return False

def getNPrime(num):
    
    '''Takes an integer and creates and returns a
       a list of that same length of the first consecutive
       prime numbers up to
    '''
    
    prime_numbers_list = []
    prime_num = 0
    while(len(prime_numbers_list) < num):
        if(isPrime(prime_num)):
            prime_numbers_list.append(prime_num)
        else:
            pass
        prime_num = prime_num + 1
    return prime_numbers_list