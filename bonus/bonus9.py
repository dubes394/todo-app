password = input("Enter your password:  ")

result = []

if len(password) >=8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)                
 
upper = False        
for j in password:
    if j.isupper():
        upper = True
result.append(upper)
      
if all(result) == True:
    print("Strong Password")
else:
    print("weak password")