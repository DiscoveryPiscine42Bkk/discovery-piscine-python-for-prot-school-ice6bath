import sys
if len(sys.argv) != {} :
    for arg in sys.argv[1:]:
        print(arg.lower(), end=" ")
else :
    print("None")
