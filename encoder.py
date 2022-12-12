import argpars
import math

class encode:
    __init__():
    ''' '''   
    def word_checker(self, user_input):
        '''Emily's function: conditional expressions. Checks user
            input string to see if the string only contains letters and spaces
            If it doesn't, it will loop back and ask for user input

        Args:
            user_input (string): The string that the user entered

        Returns:
            string: if the user's string meets the criteria,
            it will return user_input

        Side effects:
            Prints a string: If the user's string does not meet the criteria,
            it will print "Can't encode" '''
    
            invalid = False
        
            for s in user_input:
                if (s.isalpha() == False and s!=" "):
                    print("Can't encode")
                    invalid = True
        
            while invalid == True:
                user_input = input("Enter string: ")
                invalid = False
                for s in user_input:
                    if (s.isalpha() == False and s!=" "):
                        print("Can't encode")
                        invalid = True
            
            return user_input
    
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
