''' Class to represent a piece of character data.

    When constructing a char object:
        - If argument is int, float, or bool, the argument
            will first be converted to int, and then to
            character using chr, and then stored as str.
        - If argument is str and an empty string, raises a TypeError.
        - If argument is str and not empty, only the first character
            from the given argument is stored as str.
        - If argument is char, the single character arguement is
            converted to str and stored.

    Examples:
        x = char('x')     # stores the character 'x'
        y = char('yyy')   # stores the character 'y'
        z = char(64.25)   # stores the character '@', whose ASCII value is 64
        a = char(True)    # stores the non-printable character w/ ASCII value 1

        # note: cannot use ord(x) as ord expects type str but x is type char
        x_val = x.ord()   # stores the ASCII integer value of 'x'
        y_val = y.ord()   # stores the ASCII integer value of 'y'
'''

class char:
    __slots__ = ('_data')

    def __init__(self, c: int | float | str | bool) -> None:
        if isinstance(c, char):
            self._data : str = str(c)
        elif isinstance(c, (int, float, bool)):
            # convert int (or float-to-int) to its ASCII character equivalent
            self._data : str = chr(int(c))
        elif isinstance(c, str):
            if len(c) == 0:
                raise TypeError(f"invalid empty string given to char")
            self._data : str = c[0]
        else:
            raise TypeError(f"invalid type {type(c)} given to char")

    def ord(self) -> int:
        ''' method to return the underlying ASCII integer representation of
            this char
        Returns:
            the ASCII ord value of the underlying characters
        '''
        return ord(self._data[0])

    def __repr__(self) -> str:
        return repr(self._data)

    def __str__(self) -> str:
        return str(self._data)
