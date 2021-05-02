

import sys
import hashlib

'''
todo:
take input and verify if it matches an entry in a list of supported hash types
take input of a directory path for the program/file to be hashed
take input of a hash string to be use in verification

function that takes arguments:
hash type, path, hash string
and returns a boolean if the check passed/failed


'''
#guaranteed set of hash algorithms supported by this module on all platforms
#take the set from the module and return list for further use
def get_supported_algorithms():
    sup_alg = []
    hashes = hashlib.algorithms_guaranteed

    for i in hashes:
        sup_alg.append(i)
    
    return sup_alg

#print out the list of supported hash algorithms
def print_supported_algorithms(sup_alg):
    sup_alg = sorted(sup_alg)
    for i in sup_alg:
        print(i)

#print welcome message for the user
def welcome_message():
    print("\nWelcome to hash check")
    print("Here are the supported algorithms:")

#gathers user input on hash algorithm and path of file/program
#returns a two element list with the string values
def gather_input():   
    alg = input("Enter the hash algorithm to use: ")
    path = input("Enter the path of your file or program to check: ")
    reference_hash = input("Enter the reference hash to check against: ")
    user_input = [alg,path,reference_hash]
    return user_input

def hash_checker(user_input):
    sup_alg = get_supported_algorithms()
    user_alg = user_input[0]
    user_path = user_input[1]
    user_reference = user_input[2]

    user_specified_alg = False
    for i in sup_alg:
        if user_alg == i:
            user_specified_alg = True
            break
    
    if user_specified_alg is True:
        hash_obj = hashlib.new(user_alg)
        file_obj = open(user_path, mode='rb')
        file_obj = file_obj.read()
        hash_obj.update(file_obj)
        hash_value = hash_obj.hexdigest()

        if hash_value == user_reference:
            print("\nSuccess")
            print("Your supplied value " + user_reference + " MATCHES")
            print("the " + user_alg + " hash " + hash_value)
        else:
            print("\nFailure")
            print("Your supplied value DOES NOT MATCH the " + user_alg + "hash of the file or program " + user_path)
            print(hash_value)
        
        
    else:
        print("\nError, user supplied alg doesn't match system list")

def run_program():
    welcome_message()
    print_supported_algorithms(get_supported_algorithms())
    hash_checker(gather_input())

run_program()
