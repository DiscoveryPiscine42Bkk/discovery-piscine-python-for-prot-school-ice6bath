number_input = input("Give me a number: ")
float_input = float(number_input)
if float_input != int(float_input) :
    print("This number is a decimal.")
else :
    print("This number is an integer.")
