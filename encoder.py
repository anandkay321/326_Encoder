import string
import re
import argparse
import sys

ALPHABET = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]
            
class encod:
    def __init__(self,plain_text):
         self.plain_text = plain_text
         
    #Emily        
    @classmethod
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

   
def word_checker(self, user_input):
        
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
    #Anand 
    '''Anands function(cryp):is what encodes the strings. it allows the user to encode their own
    string or to encode a text file.
        Args:
            text: is for taking in the text
            shift: this is what determins how much the letter are shifted by
            alphabets: This get the letters from the english language
            user_input (string): The string that the user entered
        Returns:
            string: It will return the users encoded string based on how much they choose to shift
            the lettrs by
        Side effects:
            It will also determine how the much the deoder will have
            to shift the words back'''       
def cryp(self,text, shift, alphabets):
        def shift_alpha(alphabets):
            return alphabets[shift:] + alphabets[:shift]
        
        shifted_alpha = tuple(map(shift_alpha, alphabets))
        final_alpha = ''.join(alphabets)
        final_shift_alpha = ''.join(shifted_alpha)
        table = str.maketrans(final_alpha,final_shift_alpha)
        return text.translate(table)

    #Joe
def __repr__(self):
        return(f"encod('{self.plain_text}')")
     
class decode(encod):
    def cryp(self, text, shift, alphabets):
        return super().cryp(text, shift*-1, alphabets)

def file_encoder(path, shift, e_or_d):
    '''Joe's function
    Content: 
        with statements
    Description:
        In the case a file is specified to be edited, this method opens it,
        takes in the content, encodes it, and shifts it as shift describes
    Args:
        Path(str): Path to file to be encoded
        Shift(int): Amount to shift the letters in the file by
        e_or_d(char): 1 if encoding, 2 if decoding, indicates which to do
    Returns: 
        N/A
    Side Effects:
        Opens and edits file specified in path argument
        Creates encod object
    '''
    
    # Opens file and reads line into data list
    data = []
    f = open(path, 'r')
    data = f.readlines()
    
    f.close()
    #If encode selected, opens file, encodes line, and writes that to file
    if(e_or_d == "1"):
        with open(path, mode= 'w') as f: 
            for x in data:
                e = encod(x)
                f.write(e.cryp(e.plain_text, int(shift), ALPHABET))
    #If decode selected, opens file, decodes line, and writes that to file            
    else:
        with open(path, mode= 'w') as f:
            for x in data:
                e = decode(x)
                f.write(e.cryp(e.plain_text, int(shift), ALPHABET))

def main(e_or_d =  '-1' ,path = None):
    '''Joe's function
    Content: 
        Optional parameters
    Description: 
        Actually runs the program, giving the user options in how they
    want it to operate. 
    Args:
        e_or_d(char): Specifies whether to encode or decode
            '1' = endode
            '2' = decode
            Defaults to -1 to ensure trigger of selection prompt
        path(str): 
            optional arg to path to file to be edited
            Defaults to none so if not provided, will skip to raw input prompt
        If a .txt file is the only argument provided, the method will detect 
        that, switch that to the path, and prompt the user for a enocde or
        decode selection
    Returns: 
        N/A
    Side Effects:
        Prints input prompts to console
        Can alter e_or_d, a parameter
        Creates encod or decode objects
    '''
    # Detects if arg in wrong spot
    if(e_or_d.__contains__(".txt")):
        path = e_or_d
        e_or_d = '-1'
        
    if(path != None and path.__contains__(".txt") == False):
        while path.__contains__(".txt") == False:
            print("invalid file given, please put a .txt file in")
            path = input("Input .txt file:")
    #If invalid selection, prompts user for encode or decode selection
    if(e_or_d != '1' and e_or_d != '2'):
        while e_or_d != '1' and e_or_d != '2':
            e_or_d = input("Encode(1) or Decode(2):")
    #If no path given, reads in string to encode or decode
    if(path== None):
        if e_or_d == '1':            
            x = input("Enter string to encode: ")
            y = input("Enter shift to encode by:")
            e = encod(x)
            x = e.word_checker        
            z = e.cryp(e.plain_text, int(y), alphabets=[string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
            print(f"Encoded text: {z}")
                    
        elif(e_or_d == '2'):                  
            d = decode(input("Enter string to decode: "))
            y = int(input("Enter integer used to encode message:"))
            z = d.cryp(d.plain_text,y,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
            print(f"Decoded text: {z}")
    #Encode or decode .txt file 
    else: 
        if(e_or_d == "1"):
            shift = input("Enter shift for file encoding:")
        else:
            shift = input("Enter shift for file decoding:")
        file_encoder(path, shift, e_or_d)
        print("File successfully encoded")
    
    if(len(args)> 1):
        path = args[1]
    else: 
        path = None
    if(path== None):
        choose = 0
        while choose != '1' and choose != '2':
            choose = input("Encode(1) or Decode(2):")
            if choose == '1':            
                x = input("Enter string to encode: ")
                y = input("Enter shift to encode by:")
                e = encod(x)
                x = e.word_checker
                
                z = e.cryp(e.plain_text, int(y), alphabets=[string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
                print(f"Encoded text: {z}")
                    
            elif(choose == '2'):                  
                d = decode(input("Enter string to decode: "))
                y = int(input("Enter integer used to encode message:"))
                z = d.cryp(d.plain_text,y,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
                print(f"Decoded text: {z}")
    else: 
        #text file
        choose = 0
        while choose != "1" and choose != "2":
            choose = input("Encode(1) or Decode(2):")
        if(choose == "1"):
            shift = input("Enter shift for file encoding:")
        else:
            shift = input("Enter shift for file decoding:")
        file_encoder(path, shift, choose)
        print("File successfully encoded")
        
        


#Alex
"""
with open('encrypted.txt', 'w') as en:
    for e in eword:
        en.write("The word has been encrypted to" + str(e) + '\n')
"""    
def parse_args(arglist):
    """Parse and validate command line arguments.
    
    This function expects these required arguments.
        file: a file containing the words you want encrypted.
        word: a word you want to encrypt
        
    Args:
        arglist (list of str): list of command line arguments
        
    Returns:
        namespace: the parsed argument
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("shift", nargs='?', help ="the number of characters to be shifted")
    parser.add_argument("file", nargs= '?', help = "path to file containing \
                            words to be encrypted")
    return parser.parse_args(arglist)
if __name__ == "__main__":
    '''
    Joe 
    Parses arguments, checks how many there are, and initializes main with the
    requisite amount of args
    '''
    args = parse_args(sys.argv[1:])
    if(len(sys.argv) > 1):
        main(args.e_or_d, args.path)
    else:
        main(args.e_or_d)
