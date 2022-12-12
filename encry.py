import string 
class encod:
    def __init__(self,plain_text):
        self.plain_text = plain_text
    def __cryp__(text, shift, alphabets):
        def shift_alpha(alphabet):
            return alphabet[shift:] + alphabet[:shift]
        
        shifted_alpha = tuple(map(shift_alpha, alphabets))
        final_alpha = ''.join(alphabets)
        final_shift_alpha = ''.join(shifted_alpha)
        table = str.maketrans(final_alpha,final_shift_alpha)
        return text.translate(table)

plain_text = "What up?"
coded_word = f' plain text, {plain_text} has been encrypted to {encod.__cryp__(plain_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])}'
print(coded_word)



