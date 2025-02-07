import pytest

#using pytest to verify expected datatype outputs
def testfunc():

    #setting var for testing
    green = 4
    orange = 9.6
    number = "lmao"
    real = True

    #testing output of integers and floats
    num = green + orange
    assert isinstance(num, float) == True

    #checking string value
    assert number == "lmao"

    #testing boolean logic, chnging to fals would create an error
    assert real == True
