def correct(s):
    mistakes = {
        '0' : 'O',
        '5' : 'S',
        '1' : 'I'
    }
    return ''.join(mistakes.get(char, char) for char in s)
