import pytest



def testwordcount():
    #opening file to read
    file = open("/home/student/cs2300/cs4300/hw1/task6_read_me.txt", "r")
    text = file.read()

    count = text.split()

    #removing periods and commas in text
    for item in count:
        if item == ".":
            count.remove(item)
        if item == ",":
            count.remove(item)

    words = len(count)
    assert words == 104