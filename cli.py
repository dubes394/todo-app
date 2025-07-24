# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%H:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
        
    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = functions.get_todos()  
                   
        todos.append(todo + '\n') 
               
        functions.write_todos(todos)         #*Nothing to return in function, therefore not stored in a variable., also argument changed because the parameter filepath is default parameter. So no need of file.txt
        
    elif  user_action.startswith("show") :
        
        todos = functions.get_todos()  
            
        for index, item in enumerate(todos):
            item = item.strip('\n')             #*We are removing extra line while 
            row = f"{index +1} - {item}"
            print(row)
            
    elif user_action.startswith("edit") :
        try:                                    #*Using try and except to catch the error 
            number = int(user_action[5:]) 
            print(number)
            
            number = number - 1             
            todos = functions.get_todos()           
            new_todo = input("Enter new your todo: ")        
            todos[number] = new_todo + '\n'         
            
            functions.write_todos("todos.txt", todos)
            
        except ValueError:
            print("Command not valid") 
            continue
        
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = functions.get_todos()
            index = number -1     
            todo_to_remove = todos[index].strip('\n')            
            todos.pop(number - 1)
            
            functions.write_todos("todos.txt", todos)     
                
            message = f'Todo {todo_to_remove} was completed from the list'  
            print(message)   
        except IndexError:
            print("There is no todo with that number")
            continue            
            
    elif user_action.startswith("exit"):
        break
        # case _:
        #     print("MF! you entered wrong input")
            
print("BYE!!!!!!!!")
 
