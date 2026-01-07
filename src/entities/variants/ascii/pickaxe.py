from .ascii import Ascii


class Pickaxe(Ascii):
    ''' Ascii abstract methods. '''
    def get_unicode() -> int:
        ''' Get the Unicode code point for this avatar. '''
        return 0xC6C3 