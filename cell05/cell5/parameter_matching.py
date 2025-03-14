import sys
if len(sys.argv) > 1:
    firstparameter = sys.argv[1]
    parameter = input("What was the parameter? ")
    if parameter == firstparameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")


