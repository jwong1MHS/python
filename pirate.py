def pirate(s):
    words = s.split()
    new_words = []
    for word in words:
        if word == 'you':
            word = 'ye'
        elif word == 'your':
            word = 'yer'
        elif word == 'the':
            word = "t'"
        elif word in ['i', 'my', 'mine']:
            word = 'me'
        elif word in ['am', 'is', 'are']:
            word = 'be'
        elif word == 'myself':
            word = 'meself'
        elif word == 'for':
            word = 'fer'
        new_words.append(word)
    return ' '.join(new_words)

s = """
may i introduce myself i am quite pleased to make your aquaintence.
my aim is for us to have a mutually beneficial arrangement.
you are encouraged to be clear about your terms, as I will be about mine own.

"""
print (pirate(s))
    