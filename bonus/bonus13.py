feet_inches = input("enter feet and inches: ")

def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return(feet, inches)

def convert(feet, inches):
    meters = feet * 0.30 + inches * 0.02
    return meters

feet_inches_tuple = parse(feet_inches)
print("fi", feet_inches_tuple)
result = convert(feet_inches_tuple[0], feet_inches_tuple[1])

if result < 1:
    print("small")
else:
    print("good")