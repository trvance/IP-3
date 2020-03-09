#!/usr/bin/python

from primemodule import *

def write_primes(prime_list, file_name):
    
    """function to create a file of your choice and inserts the list 
        created from getNPrime function in the primemodule.py module
    """
    
    with open(file_name, "w") as prime_file:
        for prime in prime_list:
            prime_file.write(str(prime)+ " ")

def read_primes(file_name):
    
    """Function to read and return the list from the same file that
        was created in the function above
    """

    with open(file_name, "r") as prime_file:
        temp = []
        for prime in prime_file:
            temp.append(prime)
    return temp