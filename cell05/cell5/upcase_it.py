import sys
if len(sys.argv) != {} :
    for arg in sys.argv[1:]:
        print(arg.upper(), end=" ")
else :
    print("None")