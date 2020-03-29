#!/usr/bin/python

'''This module (primeio.py) is responsible for reading and writing to csv files

'''

from primemodule import *

def write_primes(prime_list, file_name):
    
    '''Function to create a file of your choice name and inserts the list 
       created from getNPrime function in the primemodule.py module
        
       Arguments:
        prime_list = the list created from getNPrime in primemodule.py
        file_name = the name of the file chosen by the user

       Returns:
        Nothing but it does creat a file of said name (file_name)
        
       Exceptions:
        Exception will be raised if file can't be made 
        
   '''

    try:
        with open(file_name, "w") as prime_file:
            for prime in prime_list:
                prime_file.write(str(prime)+ " ")
    except IOError as argument:
        print("Error: Can\'t write the data", argument)

def read_primes(file_name):
    
    '''Function to read and return the list from the same file that
       was created in the function above
        
       Arguments:
       file_name = the file name that you want to read
    
       Exceptions:
        Exception will be raised if file can't be found
         
    '''

    try:
        with open(file_name, "r") as prime_file:
            temp = []
            for prime in prime_file:
                temp.append(prime)
    except IOError as argument:
        print("Error: Can\'t find or read file", argument)
    else:
        return temp