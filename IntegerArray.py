# allows us to use other class types in type hints
from __future__ import annotations

from char import char

import BoolArray   # then use BoolArray.BoolArray to reference
import CharArray
import FloatArray

class IntegerArray:
    __slots__ = ('_integer_array')

    ############################################################
    def __init__(self) -> None:
        self._integer_array : list[int] = []

    ############################################################
    def __str__(self) -> str:
        ''' overrides the __str__ method to provide a str representation of the
            IntegerArray
        Returns:
            a string representing the array
        '''
        return repr(self._integer_array)

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
            IntegerArray object
        Returns:
            number of items in the internal integer array
        '''
        count = 0
        for i in range(len(self._integer_array)):
            count +=1
        return count
            
        


    ############################################################
    def __getitem__(self, index: int) -> int:
        ''' overrides the default __getitem__ function for use of [] item access
            on a IntegerArray object
        Parameters:
            index: integer index into the IntegerArray from which to retrieve
        Returns:
            the integer present at the given index
        Raises:
            IndexError exception if the index is invalid
        '''
        # updated code goes below;
        # make sure to use the "private" _checkBounds method defined above
        # (see putAt method for an example, paying attention to the 2nd parameter)
        # before fetching and returning
        self._checkBounds(index)
        return self._integer_array[index]

    ############################################################
    def append(self, item: int | FloatArray | CharArray | BoolArray) -> None:
        ''' method to allow appending to an IntegerArray 
        Parameters:
            item: either an individual int to append; or an object of
                  FloatArray or CharArray or BoolArray, whose items each
                  of which will be appended
        Raises:
            ValueError exception if the given item is not one of int,
                FloatArray, CharArray, or BoolArray
        '''
        if isinstance(item, int):
            # updated code goes below
            self._integer_array.append(item)

        else:
            # item is one of FloatArray, CharArray, or BoolArray
            array = item
            if isinstance(array, FloatArray.FloatArray):
                # updated code goes below -- iterate the float array, converting
                # each to an integer and then append
               for i in array:
                   self._integer_array.append(int(i))
                    
            elif isinstance(array, CharArray.CharArray):
                # updated code goes below -- iterate the char array, converting
                # each to an integer using the char class .ord() method,
                # and then append
                for i in array:
                    self._integer_array.append(ord(i))
            elif isinstance(array, BoolArray.BoolArray):
                # updated code goes below -- iterate the bool array, converting
                # each to an integer and then append
                for i in array:
                    self._integer_array.append(int(i))
            
            else:
                raise ValueError(f"invalid type {type(array)} to append")

    ############################################################
    def __setitem__(self, index: int, value: int) -> None:
        ''' if index is size-legitimate, put the int value at that index;
            otherwise, append the int value to the end of the list 
        Parameters:
            index: the integer index passed to [], i.e., where to put the value
            value: a int
        Raises:
            ValueError if value is not int
        '''
        if not isinstance(value, int ):
            raise ValueError(f"invalid type {type(value)} to putAt")

        # updated code goes below;
        # use the private _checkBounds method (paying attention to the 2nd
        # parameter), and handle both possible cases discussed in the docstring
        # (a try/except is a good choice here...)
        try:
            self._checkBounds(index, False)  # Check bounds for setting an item

       # If _checkBounds didn't raise an exception, the index is valid
            self._integer_array[index] = value  # Put the value at the specified index
        except IndexError:
       # Index is out of bounds, so append the value to the end
            self._integer_array.append(value)

    ############################################################
    def putAt(self, value: int, index: int) -> None:
        ''' Method to allow putting a single int item into an IntegerArray
            at a given index.  If the index is equal to the size of the
            array, putAt is equivalent to an append; otherwise, the
            value is inserted and all subsequent values shifted to the
            right.
        Parameters:
            value: an integer
            index: integer index indicating where to put the item into the
                   IntegerArray 
        Raises:
            IndexError if the given index is invalid
            ValueError exception if the given value is not int
        '''
        self._checkBounds(index, False)
        if not isinstance(value, int):
            raise ValueError(f"invalid type {type(value)} to putAt")

        # updated code goes below -- can be done in one line using slicing
        self._integer_array = self._integer_array[:index] + [value] + self._integer_array[index:]


