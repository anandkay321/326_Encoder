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
#Joe
    def __repr__(self):
        return(f"encod('{self.plain_text}')")
    
class decode(encod):
    def __decryp__(text, shift*-1, alphabets):
        return super().__cryp__(text, shift*-1, alphabets)
    
choose = 0
while choose != 1 and choose != 0:
    choose = input("Encode(1) or Decode(2):")
    if choose == 1:
        x = encod(input("Enter string: "))
        plain_text = x.word_checker(x.plain_text)
        coded_word = f' plain text, {plain_text} has been encrypted to {encod.__cryp__(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])}'
        print(coded_word) 
    elif choose == 2:
        y = decode(input("Enter string: "))
        encoded_text = y.word_checker(y.plain_text)
        print(f' encoded text, {encoded_text} has been decrypted to {decode.__decryp__(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])}')

    
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
