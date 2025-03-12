array = [2, 8, 9, 48, 8, 22, -12, 2]
new = [number + 2 for number in array if number > 5]
print("Original array" , array)
print("New array:" , new)