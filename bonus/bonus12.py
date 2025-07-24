feet_inches = input("enter feet and inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    
    meters = feet * 0.30 + inches * 0.02
    return meters

result = convert(feet_inches)

if result < 1:
    print("small")
else:
    print("good")