import argpars
import math

class encode:
    __init__():
    ''' '''   
    word_checker():
    '''This funtion's purpose is to check if the user inputed word can be encoded
    if it reads the string and it contains anything other than letter it will return
    'word can not be encoded' '''
    word_input():
    '''This funtion's purpose is what the user will use to input their words that they
    choose to encode'''   
    
    file_encoding():
    ''' This function will take the user's chosen words and encode it '''
    encode():
    ''' This function will take the user's chosen words and encode it using our algorithm
    based on an ASCII table, where the algorithm converts each character into its ascii 
    value, increments it by the chosen start value + its index in the string'''
    
    e_words = []
class decode(encode):
    
    __init__():
        
    decode():
    '''This function overwrites and is based on the encode function, where this
    will take a presumably encoded string and reverse the encoding'''
    def decode(text, shift, alphabets):
        return super().__cryp__(text, shift*-1, alphabets)
    
    
    
    
def parse_args():
    """Parse and validate command line arguments.
    
    This function expects these required arguments.
        file: a file containing the words you want encrypted.
        word: a word you want to encrypt
        
    Args:
        arglist (list of str): list of command line arguments
        
    Returns:
        namespace: the parsed argument
    """
