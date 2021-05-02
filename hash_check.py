
import sys
import hashlib

#print welcome message for the user
def welcome_message():
    print("\nWelcome to hash check")
    print("Here are the supported algorithms:")

#guaranteed set of hash algorithms supported by this module on all platforms
#take the set from the module and return list for further use
def get_supported_algorithms():
    sup_alg = []
    hashes = hashlib.algorithms_guaranteed
    #don't include variable output shake algorithms
    for i in hashes:
        if i == 'shake_128':
            continue
        elif i == 'shake_256':
            continue
        #append any non shake algorithms to the supported list
        else:
            sup_alg.append(i)
    return sup_alg

#print out the list of supported hash algorithms
def print_supported_algorithms(sup_alg):
    sup_alg = sorted(sup_alg)
    for i in sup_alg:
        print(i)

#gathers user input on hash algorithm and path of file/program
#returns a two element list with the string values
def gather_input():   
    alg = input("Enter the hash algorithm to use: ")
    path = input("Enter the path of your file or program to check: ")
    reference_hash = input("Enter the reference hash to check against: ")
    user_input = [alg,path,reference_hash]
    return user_input

#computes the hash based on user input and verifies if it matches the reference value
def hash_checker(user_input):
    try:
        #guaranteed set of hash algorithms supported by this module on all platforms
        sup_alg = get_supported_algorithms()

        #user supplied algorithm type, path to file to be hashed, reference value to check against
        user_alg = user_input[0]
        user_path = user_input[1]
        user_reference = user_input[2]

        #check if user specified algorithm matches a module supported algorithm
        user_specified_alg = False
        for i in sup_alg:
            if user_alg == i:
                user_specified_alg = True
                break
        
        #user supplied algorithm is supported
        if user_specified_alg is True:
            #create a hashlib object and pass in the user supplied algorithm type
            hash_obj = hashlib.new(user_alg)
            #open up the user supplied file in read only and binary mode
            file_obj = open(user_path, mode='rb')
            #get a bytes like object from the open file
            file_obj = file_obj.read()
            #run the hash against the bytes like object
            hash_obj.update(file_obj)
            hash_value = hash_obj.hexdigest()

            #report output on hash check depending on success or failure
            if hash_value == user_reference:
                print("\nSuccess")
                print("Your supplied value " + user_reference + " MATCHES")
                print("\nthe " + user_alg + " hash " + hash_value)
            else:
                print("\nFailure")
                print("Your supplied value DOES NOT MATCH the " + user_alg + " hash of the file or program: " + user_path)
                print(hash_value)
        else:
            print("\nError, user supplied algorithm doesn't match system list")
        
    except IOError as err:
        print("OS error opening file {0}".format(err))
    except:
        raise

#encapsulating method for program logic
def run_program():
    try:
        welcome_message()
        print_supported_algorithms(get_supported_algorithms())
        hash_checker(gather_input())
    except:
        print("Unexpected error, closing program", sys.exc_info()[0])
        exit(1)

#run it
run_program()
