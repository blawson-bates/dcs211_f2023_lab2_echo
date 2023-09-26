# allows us to use other class types in type hints
from __future__ import annotations

from char import char

import BoolArray   # then use BoolArray.BoolArray to reference
import CharArray
import IntegerArray

class FloatArray:
    __slots__ = ('_float_array')

    ############################################################
    def __init__(self) -> None:
        self._float_array : list[float] = []

    ############################################################
    def __str__(self) -> str:
        ''' overrides the __str__ method to provide a str representation of the
            FloatArray
        Returns:
            a string representing the array
        '''
        return repr(self._float_array)

    ############################################################
    def _checkBounds(self, index: int, using_get: bool = True) -> None:
        ''' private method to encapsulate checking index bounds
        Parameters:
            index: integer index (into list) that is being checked
            using_get: if True, index corresponds to fetching an item;
                       if False, index corresponds to setting an item
        Raises:
            IndexError exception if the given index is invalid
        '''
        size = len(self)
        opt = "get" if using_get else "put"
        msg = f"invalid {opt} index {index} for array of size {size}"
        # https://docs.python.org/3/library/exceptions.html
        if using_get:
            # for gets, must be a non-empty list and index must be in
            # the bounds of a valid list index
            if size == 0 or not (0 <= index < size):
                raise IndexError(msg)
        else:
            # for puts, index must be between 0 and list size (both
            # inclusive), as list size corresponds to an append (see specs)
            if index < 0 or index > size:
                raise IndexError(msg)

    ###########################################################################
    #  You need to modify the bodies of the methods below and then test...
    ###########################################################################

    ############################################################
    def __len__(self) -> int:
        ''' overrides the default __len__ function for use of len on a
            FloatArray object
        Returns:
            number of items in the internal float array
        '''
        # updated code goes below
        pass

    ############################################################
    def __getitem__(self, index: int) -> float:
        ''' overrides the default __getitem__ function for use of [] item access
            on a FloatArray object
        Parameters:
            index: integer index into the FloatArray from which to retrieve
        Returns:
            the float present at the given index
        Raises:
            IndexError exception if the index is invalid
        '''
        # updated code goes below;
        # make sure to use the "private" _checkBounds method defined above
        # (see putAt method for an example, paying attention to the 2nd parameter)
        # before fetching and returning
        pass

    ############################################################
    def append(self, item: float | IntegerArray | CharArray | BoolArray) -> None:
        ''' method to allow appending to a FloatArray
        Parameters:
            item: either an individual float to append; or an object of
                  IntegerArray or BoolArray or CharArray, whose items each
                  of which will be appended
        Raises:
            ValueError exception if the given item is not one of float,
                IntegerArray, BoolArray, or CharArray
        '''
        if isinstance(item, float):
            # updated code goes below
            pass
        else:
            # item is one of IntegerArray, CharArray, or BoolArray
            array = item
            if isinstance(array, IntegerArray.IntegerArray):
                # updated code goes below -- iterate the integer array, converting
                # each to a bool and then append
                pass
            elif isinstance(array, CharArray.CharArray):
                # updated code goes below -- iterate the char array, converting
                # each to an integer using the char class .ord() method,
                # and then append
                pass
            elif isinstance(array, BoolArray.BoolArray):
                # updated code goes below -- iterate the bool array, converting
                # each to an integer and then append
                pass
            else:
                raise ValueError(f"invalid type {type(array)} to append")

    ############################################################
    def __setitem__(self, index: int, value: float) -> None:
        ''' if index is size-legitimate, put the float value at that index;
            otherwise, append the float value to the end of the list 
        Parameters:
            index: the integer index passed to [], i.e., where to put the value
            value: a float
        Raises:
            ValueError if value is not float
        '''
        if not isinstance(value, float ):
            raise ValueError(f"invalid type {type(value)} to putAt")

        # updated code goes below;
        # use the private _checkBounds method (paying attention to the 2nd
        # parameter), and handle both possible cases discussed in the docstring
        # (a try/except is a good choice here...)
        pass

    ############################################################
    def putAt(self, value: float, index: int) -> None:
        ''' Method to allow putting a single float item into a FloatArray
            at a given index.  If the index is equal to the size of the
            array, putAt is equivalent to an append; otherwise, the
            value is inserted and all subsequent values shifted to the
            right.
        Parameters:
            value: a float 
            index: integer index indicating where to put the item into the
                   FloatArray 
        Raises:
            IndexError if the given index is invalid
            ValueError exception if the given value is not float
        '''
        self._checkBounds(index, False)
        if not isinstance(value, float):
            raise ValueError(f"invalid type {type(value)} to putAt")

        # updated code goes below -- can be done in one line using slicing
        pass


