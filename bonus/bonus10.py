try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))
    
    if width == length:
        exit("Looks like square you mf!!!!")
        
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")

    