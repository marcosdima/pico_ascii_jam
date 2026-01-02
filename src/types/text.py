class Text(str):
    '''Custom Text class that inverts case (lowercase to uppercase and vice versa)'''
    def __new__(cls, content):
        '''Invert case of the input string.'''
        inverted = content.swapcase()
        return super().__new__(cls, inverted)

