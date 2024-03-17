import sys
if len(sys.argv) == 2:
    if (sys.argv[1].isdigit()):
        if(int(sys.argv[1]) % 2 == 0):
            print(" I'm Even")
        else:
            print("I'm Odd")
    else:
        try:
            assert (isinstance(sys.argv[1], int))
        except AssertionError:
            print("Not a number")
else:
    raise AssertionError("Number of args more than 2")