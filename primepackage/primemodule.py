#!/usr/bin/python

'''Module primemodule.py is responsible for the computations of the Prime package.

'''

def isPrime(n):
    
    '''Takes a natural number and returns true if it
       is a prime number and false otherwise
    
       Parameters:
        n is the number being evaluated
        
       Returns:
        true if n is a prime number
        false if n is not a prime number
        
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
    
    '''Method for creating a list containing prime numbers length of num
    
       A blank list is created and while it's length is less than num then
       prime_num which is initiated at zero is sent to the previous method (isPrime)
       as a parameter to determine if it is a prime number. If that method returns
       true then the number is added to the list
    
       Parameters:
        num - length of list being created
        
       Returns
        prime_numbers_list - a list containing prime numbers in consectutive order 
        with a length that the user used as a parameter
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