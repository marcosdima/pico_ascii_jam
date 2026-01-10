class Text:
    '''Helper class that automatically swaps uppercase and lowercase.
    
    This is useful for fonts where uppercase and lowercase are inverted.
    '''
    
    def __init__(self, text: str):
        '''Initialize Text with automatic case swap.
        
        Args:
            text (str): The text to swap case.
        '''
        self.value = text.swapcase()
    
    
    def __str__(self) -> str:
        '''Return the swapped-case text as a string.'''
        return self.value
    
    
    def __repr__(self) -> str:
        '''Return the representation of the swapped-case text.'''
        return self.value

