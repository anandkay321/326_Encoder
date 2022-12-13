import string
import re
import argparse
import sys

ALPHABET = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

def file_encoder(path, shift, e_or_d):
    print(path)

    data = []
    f = open(path, 'r')
    data = f.readlines()
    print(data)
    f.close()
    if(e_or_d == "1"):
        with open(path, mode= 'w') as f:
            count = 1
            for x in data:
                e = encod(x)
                f.write(e.cryp(e.plain_text, int(shift), ALPHABET))
                count+=1
            
    else:
        with open(path, mode= 'w') as f:
            count = 1
            for x in data:
                e = decode(x)
                f.write(e.cryp(e.plain_text, int(shift), ALPHABET))
                count+=1

                
            
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
    def __repr__(self):
        return(f"decode('{self.plain_text}")
    
def main():
    args = sys.argv[0:]
    
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
    parser.add_argument("shift", help ="the number of characters to be shifted")
    parser.add_argument("dfile", help = "path to file containing \
                            words to be encrypted")
    parser.add_argument("efile", help = "path to file containing the \
                            encrypted words.")
    return parser.parse_args(arglist)
if __name__ == "__main__":
    
    main()

#encoding = print("Beginning encoding: ", encod(text_file))



#intro_text = input("Welcome to the Encoder. Please input a .txt file to encrypt: ")
#text_file = open(intro_text, "r") 
#print("Now opening: ", intro_text)

