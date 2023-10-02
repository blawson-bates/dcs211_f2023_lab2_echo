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

    ############################################################ MODIFIED & TESTED
    def __len__(self) -> int:
        ''' overrides the default __len__ function for use of len on a
            FloatArray object
        Returns:
            number of items in the internal float array
        '''
        # updated code goes below
        length = len(self._float_array)
        return length

    ############################################################ MODIFIED, TESTED
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
        
        #Check that index is in bounds
        self._checkBounds(index= index)
        
        return self._float_array[index]

    ############################################################ MODIFIED, TESTED
    def append(self, item: float | IntegerArray.IntegerArray | CharArray.CharArray | BoolArray.BoolArray ) -> None:
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
            self._float_array.append(item)
            # updated code goes below
            pass
        else:
            # item is one of IntegerArray, CharArray, or BoolArray
            array = item
            if isinstance(array, IntegerArray.IntegerArray):
                # updated code goes below -- iterate the integer or bool array, converting
                # each to a float* and then append
                for item in array._integer_array: self._float_array.append(float(item))
                pass
            elif isinstance(array, CharArray.CharArray):
                # updated code goes below -- iterate the char array, converting
                # each to a float*  using the char class .ord() method,
                # and then append
                for item in array._char_array: self._float_array.append(float(item.ord()))
                pass
            elif isinstance(array, BoolArray.BoolArray):
                for item in array._bool_array: self._float_array.append(float(item))
            else:
                raise ValueError(f"invalid type {type(array)} to append")

    ############################################################ MODIFIED, TESTED
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
        
        try:
            self._checkBounds(index = index, using_get = False)
            self._float_array[index] = value

        except IndexError:
            self.append(value)
            
        
        pass

    ############################################################ MODIFIED, TESTED
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
        
        self._float_array.insert(index, value)       #Source: https://www.digitalocean.com/community/tutorials/python-add-to-list
        
        #Hi Barry! I know you can also splice to modify lists, but I believe this to be the slightly faster way to do it? I did do it regardless in main to show I know how to do it.
        
        pass

def tester(act, exp) -> Str:
    ''' Method used to test expected value and actual value
    
    Parameters:
        act: Actual value of any type
        exp: Expected value of any type
    Return:
        String with test results

    
    '''
    if act == exp:
        return(f"Passed with value: {act}")
    elif type(act) != type(exp):
        return(f"WARNING: Test Failed. Data type mismatch.\n   Expected value: {exp}; is of type: {type(exp)}.\n   Actual value: {act}; is of type: {type(act)} ")
    else:
        return(f"WARNING: Test Failed. Data value mismatch.\n   Expected value: {exp}. \n Actual value: {act}")
        

def main() -> None:
    ############################### Testing ###############################
    ## For length zero array ##
    print("########## Testing Float Array ##########")
    
    ######################## Testing Len Function ###########################
    
    print("### Testing Len Function ###")
    
    print("Test 1.1: Array length 0")
    test_zero_array = FloatArray()
    test_zero_actual = len(test_zero_array)
    test_zero_expected = 0
    print(tester(act = test_zero_actual, exp = test_zero_expected))   
    
    print("Test 1.2: Array Non-Zero")
    test_non_zero_array = FloatArray()
    test_non_zero_array._float_array = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
    test_non_zero_actual = len(test_non_zero_array)
    
    test_non_zero_expected = 10
    print(tester(act = test_non_zero_actual, exp = test_non_zero_expected))

    ######################## Testing _getitem_ Function ###########################    

    print("### Testing _getitem_ Function ###")
    
    print("Test 2.1: Out of bounds index")
    try:
        test_zero_array[2]
    except IndexError:
        print("Test Passed")
    test_zero_expected = 0
    
    print("Test 2.2: In bounds index")
    print(tester(act = test_non_zero_array[1], exp = 2))
    
    ######################## Testing append Function ###########################

    print("### Testing append Function ###")
    
    print("Test 3.1: Append Float Integer")
    test_non_zero_array.append(100.0)
    print(tester(test_non_zero_array[10], 100.0))
    
    print("Test 3.2: Append IntArray len 3")
    int_array = IntegerArray.IntegerArray()
    int_array._integer_array = [1,2,3]
    test_non_zero_array.append(int_array)
    tester_int_array = [test_non_zero_array[11], test_non_zero_array[12], test_non_zero_array[13]]
    print(tester(tester_int_array, [1.0,2.0,3.0]))    

    print("Test 3.3: Append BoolArray len 2")
    bool_array = BoolArray.BoolArray()
    bool_array._bool_array = [True, False]
    test_non_zero_array.append(bool_array)
    tester_bool_array = [test_non_zero_array[14], test_non_zero_array[15]]
    print(tester(tester_bool_array, [1.0,0.0]))   
    
    print("Test 3.4: Append CharArray len 4")
    char_array = CharArray.CharArray()
    char_array._char_array = [char('a'),char('b'), char('c'), char('d')]
    test_non_zero_array.append(char_array)
    tester_char_array = [test_non_zero_array[16], test_non_zero_array[17], test_non_zero_array[18], test_non_zero_array[19]]
    print(tester(tester_char_array, [97.0,98.0,99.0,100.0]))
    
    ######################## Testing _setitem_ Function ###########################
    
    print("### Testing _setitem_ Function ###")
    
    print("Test 4.1: setitem within bounds")
    test_non_zero_array[1] = 42.0
    print(tester(test_non_zero_array[1], 42.0))
    
    print("Test 4.2: setitem outside bounds")
    test_non_zero_array[100] = 27.0
    print(tester(test_non_zero_array[20], 27.0))
    
    ######################## Testing putAt Function ###########################
    
    print("### Testing putAt Function ###")
    
    print("Test 5.1: setitem at the beginning of the list")
    old_array = test_non_zero_array
    test_non_zero_array.putAt(value= 33.0, index= 0)
    print(tester(act = test_non_zero_array._float_array, exp = [33.0] +  old_array._float_array[1:]))       #Here is an example of splicing to modify lists
    
    print("Test 5.2: setitem in middle of the list")
    old_array = test_non_zero_array
    test_non_zero_array.putAt(value= 123.0, index= 3)
    print(tester(act = test_non_zero_array._float_array, exp = old_array._float_array[0:3] + [123.0] +  old_array._float_array[4:]))       #Here is another example of splicing to modify lists 
    
    pass

if __name__ == "__main__":
    main()