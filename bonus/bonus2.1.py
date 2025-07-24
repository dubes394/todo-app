password = input("enter the password: ")

while password != "pass123":
    password = input("enter the password again: ")

print("Password was correct")    
    
    
def calcu(a,b, operation):
    if operation == "multiply":
        return a * b
    if operation == "add":
        return a + b
    
result = calcu(5, 4, "add")
    