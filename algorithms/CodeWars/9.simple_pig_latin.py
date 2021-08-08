# Problem
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

import string


def pig_it(text):
    words = text.split()
    result = ''
    for word in words:
        if word not in string.punctuation:
            result += (word[1:] + word[0] + 'ay ')
        else:
            result += (word + ' ')
    return result[:-1]
