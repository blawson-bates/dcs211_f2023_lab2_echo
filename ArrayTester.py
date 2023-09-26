from char import char

import BoolArray
import CharArray
import FloatArray
import IntegerArray

################################################################################
def printTest(test_string: str, result: int | float | char | bool | str | None,
              expected: int | float | char | bool | str | None,
              is_exception: bool = False) -> None:
    ''' function to wrap up prints for testing
    Args:
        test_string: a string version of the method call / test being made
        result:      the result (whether int or float or char or bool or None) of the test
        expected:    the expected result
        is_exception: True if passing in exception result
    Returns:
        nothing -- just prints
    '''
    print(f"Testing {test_string}:")
    add_on = "" if is_exception else f"\t of type {type(result)}"
    if isinstance(result, str) and '[' in result:
        print(f"\t result   : {repr(str(result).replace(', ',','))}{add_on}")
    else:
        print(f"\t result   : {repr(result)}{add_on}")
    print(f"\t expected : {repr(expected)}{add_on}")

################################################################################
def main() -> None:
    '''  # uncomment when ready to test CharArray class
    # test CharArray
    char_array1 = CharArray.CharArray()

    for i in range(8): char_array1.append(chr(ord('A') + i))
    char_array1[0] = char('a')   # wrap the str as a char type
    char_array1.append(char('^'))
    char_array1.putAt(char('%'), 8)

    result = len(char_array1);  expected = 10
    printTest("len(char_array1)", result = result, expected = expected)

    expecteds = ['a', '%', '^']
    for i in [0, len(char_array1) - 2, len(char_array1) - 1]:
        result = char_array1[i];  expected = expecteds.pop(0)
        printTest(f"char_array1[{i}]", result = result, expected = char(expected))

    # MAKE SURE TO CHANGE THE EXPECTED RESULT HERE!!
    result = char_array1.__str__(); expected = "!!CHANGE ME!!"
    printTest(f"char_array1.__str__()", result = result, expected = expected)

    try:
        index = 100
        char_array1[index]
    except IndexError as err:
        printTest(f"char_array1[{index}]", str(err), 'Array index out of range', True)
    except Exception as err:
        printTest(f"char_array1[{index}]", str(err), 'INCORRECT EXCEPTION: EXPECTED INDEX ERROR', True)

    try:
        value = '#'; index = 33
        char_array1.putAt(char(value), index)
    except IndexError as err:
        printTest(f"char_array1.putAt({repr(value)}, {index})", str(err), 'Array index out of range', True)
    except Exception as err:
        printTest(f"char_array1.putAt({repr(value)}, {index})", str(err), 'INCORRECT EXCEPTION: EXPECTED INDEX ERROR', True)

    try:
        value = '#'; index = 2
        char_array1.putAt(ord(value), index)
    except ValueError as err:
        printTest(f"char_array1.putAt({ord(value)}, {index})", str(err), 'Invalid type', True)
    except Exception as err:
        printTest(f"char_array1.putAt({ord(value)}, {index})", str(err), 'INCORRECT EXCEPTION: EXPECTED VALUE ERROR', True)


    print('-' * 70)
    '''

    #################################################################

    '''  # uncomment when ready to test IntegerArray class
    # test IntegerArray
    int_array1 = IntegerArray.IntegerArray()

    for i in range(8): int_array1.append(ord('a') + i)
    int_array1[0] = ord('A')
    int_array1.append(ord('^'))
    int_array1.putAt(ord('@'), 8)

    result = len(int_array1);  expected = 10
    printTest("len(int_array1)", result = result, expected = expected)

    expecteds = [ord('A'), ord('@'), ord('^')]
    for i in [0, len(int_array1) - 2, len(int_array1) - 1]:
        result = int_array1[i];  expected = expecteds.pop(0)
        printTest(f"int_array1[{i}]", result = result, expected = expected)

    result = int_array1.__str__()
    # MAKE SURE TO CHANGE THE EXPECTED RESULT HERE!!
    expected = "!!CHANGE ME!!"
    printTest(f"int_array1.__str__()", result = result, expected = expected)

    try:
        index = 100
        int_array1[index]
    except IndexError as err:
        printTest(f"int_array1[{index}]", str(err), 'Array index out of range', True)
    except Exception as err:
        printTest(f"int_array1[{index}]", str(err), 'INCORRECT EXCEPTION: EXPECTED INDEX ERROR', True)

    try:
        value = '#'; index = 33
        int_array1.putAt(float(ord(value)), index)
    except IndexError as err:
        printTest(f"int_array1.putAt({repr(value)}, {index})", str(err), 'Array index out of range', True)
    except Exception as err:
        printTest(f"int_array1.putAt({repr(value)}, {index})", str(err), 'INCORRECT EXCEPTION: EXPECTED INDEX ERROR', True)

    try:
        value = '#'; index = 2
        int_array1.putAt(value, index)
    except ValueError as err:
        printTest(f"int_array1.putAt({repr(value)}, {index})", str(err), 'Invalid type', True)
    except Exception as err:
        printTest(f"int_array1.putAt({repr(value)}, {index})", str(err), 'INCORRECT EXCEPTION: EXPECTED VALUE ERROR', True)

    print('-' * 70)
    '''

    #################################################################

    '''  # uncomment when ready to test FloatArray class
    # test FloatArray
    float_array1 = FloatArray.FloatArray()

    for i in range(8): float_array1.append(float(ord('a') + i) + 0.25)
    float_array1[0]   = float(ord('A')) + 0.25
    float_array1.append(ord('^') + 0.25)
    float_array1.putAt(ord('!') + 0.25, 8)

    result = len(float_array1);  expected = 10
    printTest("len(float_array1)", result = result, expected = expected)

    expecteds = [float(ord('A')) + 0.25, float(ord('^')) + 0.25, float(ord('!')) + 0.25]
    for i in [0, len(float_array1) - 2, len(float_array1) - 1]:
        result = float_array1[i];  expected = expecteds.pop(0)
        printTest(f"float_array1[{i}]", result = result, expected = expected)

    result = float_array1.__str__()
    # MAKE SURE TO CHANGE THE EXPECTED RESULT HERE!!
    expected = "!!CHANGE ME!!"
    printTest(f"float_array1.__str__()", result = result, expected = expected)

    try:
        index = 100
        float_array1[index]
    except IndexError as err:
        printTest(f"float_array1[{index}]", str(err), 'Array index out of range', True)
    except Exception as err:
        printTest(f"float_array1[{index}]", str(err), 'INCORRECT EXCEPTION: EXPECTED INDEX ERROR', True)

    try:
        value = float(ord('#') + 0.25); index = 33
        float_array1.putAt(value, index)
    except IndexError as err:
        printTest(f"float_array1.putAt({repr(value)}, {index})", str(err), 'Array index out of range', True)
    except Exception as err:
        printTest(f"float_array1.putAt({repr(value)}, {index})", str(err), 'INCORRECT EXCEPTION: EXPECTED INDEX ERROR', True)

    try:
        value = '#'; index = 2
        float_array1.putAt(value, index)
    except ValueError as err:
        printTest(f"float_array1.putAt({repr(value)}, {index})", str(err), 'Invalid type', True)
    except Exception as err:
        printTest(f"float_array1.putAt({repr(value)}, {index})", str(err), 'INCORRECT EXCEPTION: EXPECTED VALUE ERROR', True)

    print('-' * 70)
    '''

    #################################################################

    '''  # uncomment when ready to test BoolArray class
    # test BoolArray
    bool_array1 = BoolArray.BoolArray()

    for i in range(8): bool_array1.append(bool(True * (i % 2)))  # either T or F
    bool_array1[0]   = True
    bool_array1.append(True)
    bool_array1.putAt(False, 8)

    result = len(bool_array1);  expected = 10
    printTest("len(bool_array1)", result = result, expected = expected)

    expecteds = [True, False, True]
    for i in [0, len(bool_array1) - 2, len(bool_array1) - 1]:
        result = bool_array1[i];  expected = expecteds.pop(0)
        printTest(f"bool_array1[{i}]", result = result, expected = expected)

    result = bool_array1.__str__()
    # MAKE SURE TO CHANGE THE EXPECTED RESULT HERE!!
    expected = "!!CHANGE ME!!"
    printTest(f"bool_array1.__str__()", result = result, expected = expected)

    try:
        index = 100
        bool_array1[index]
    except IndexError as err:
        printTest(f"bool_array1[{index}]", str(err), 'Array index out of range', True)
    except Exception as err:
        printTest(f"bool_array1[{index}]", str(err), 'INCORRECT EXCEPTION: EXPECTED INDEX ERROR', True)

    try:
        value = False; index = 33
        bool_array1.putAt(value, index)
    except IndexError as err:
        printTest(f"bool_array1.putAt({repr(value)}, {index})", str(err), 'Array index out of range', True)
    except Exception as err:
        printTest(f"bool_array1.putAt({repr(value)}, {index})", str(err), 'INCORRECT EXCEPTION: EXPECTED INDEX ERROR', True)

    try:
        value = '#'; index = 2
        bool_array1.putAt(value, index)
    except ValueError as err:
        printTest(f"bool_array1.putAt({repr(value)}, {index})", str(err), 'Invalid type', True)
    except Exception as err:
        printTest(f"bool_array1.putAt({repr(value)}, {index})", str(err), 'INCORRECT EXCEPTION: EXPECTED VALUE ERROR', True)

    print('-' * 70)
    '''

    #################################################################

    '''
    ## test appends for CharArray
    ## UNCOMMENT THIS AFTER .append* methods implemented
    char_array2 = CharArray.CharArray()
    char_array2.append(int_array1)
    result = char_array2.__str__()
    expected = str([chr(int_array1[i]) for i in range(len(int_array1))]).replace(' ', '')
    printTest(f"char_array2.append(int_array1)", result, expected)

    char_array3 = CharArray.CharArray()
    char_array3.append(float_array1)
    result = char_array3.__str__()
    expected = str([chr(int(float_array1[i])) for i in range(len(float_array1))]).replace(' ', '')
    printTest(f"char_array3.append(float_array1)", result, expected)

    ###################################################
    # add a test for appending bool array, if team of 4
    ###################################################

    print()
    '''

    '''
    ## test appends for IntegerArray
    ## UNCOMMENT THIS AFTER .append* methods implemented
    int_array2 = IntegerArray.IntegerArray()
    int_array2.append(char_array1)
    result = int_array2.__str__()
    expected = str([char_array1[i].ord() for i in range(len(char_array1))]).replace(' ', '')
    printTest(f"int_array2.append(char_array1)", result, expected)

    int_array3 = IntegerArray.IntegerArray()
    int_array3.append(float_array1)
    result = int_array3.__str__()
    expected = str([int(float_array1[i]) for i in range(len(float_array1))]).replace(' ', '')
    printTest(f"int_array3.append(float_array1)", result, expected)

    ###################################################
    # add a test for appending bool array, if team of 4
    ###################################################

    print()
    '''

    '''
    ## test appends for FloatArray
    ## UNCOMMENT THIS AFTER .append* methods implemented
    float_array2 = FloatArray.FloatArray()
    float_array2.append(char_array1)
    result = float_array2.__str__()
    expected = str([float(char_array1[i].ord()) for i in range(len(char_array1))]).replace(' ', '')
    printTest(f"float_array2.append(char_array1)", result, expected)

    float_array3 = FloatArray.FloatArray()
    float_array3.append(int_array1)
    result = float_array3.__str__()
    expected = str([float(int_array1[i]) for i in range(len(int_array1))]).replace(' ', '')
    printTest(f"float_array3.append(int_array1)", result, expected)

    ###################################################
    # add a test for appending bool array, if team of 4
    ###################################################
    '''

    '''
    ## test appends for BoolArray
    ## UNCOMMENT THIS AFTER .append* methods implemented
    bool_array2 = BoolArray.BoolArray()
    bool_array2.append(char_array1)
    result = bool_array2.__str__()
    expected = str([bool(char_array1[i].ord()) for i in range(len(char_array1))]).replace(' ', '')
    printTest(f"bool_array2.append(char_array1)", result, expected)

    bool_array3 = BoolArray.BoolArray()
    bool_array3.append(int_array1)
    result = bool_array3.__str__()
    expected = str([bool(int_array1[i]) for i in range(len(int_array1))]).replace(' ', '')
    printTest(f"bool_array3.append(int_array1)", result, expected)

    bool_array4 = BoolArray.BoolArray()
    bool_array4.append(float_array1)
    result = bool_array4.__str__()
    expected = str([bool(float_array1[i]) for i in range(len(float_array1))]).replace(' ', '')
    printTest(f"bool_array4.append(float_array1)", result, expected)

    '''

if __name__ == "__main__":
    main()

