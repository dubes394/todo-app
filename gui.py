import functions
import FreeSimpleGUI as sg 

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                         enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button], 
                           [exit_button]],
                   font=("Helvetica", 18))

while True:
    event, values  = window.read()      #*event tells you what happened (e.g., "Add" or "Edit"), values holds what the user typed or selected
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()         # Load current todos
            new_todo = values["todo"] + "\n"      # Get user input
            todos.append(new_todo)                # Add to the list
            functions.write_todos(todos)          # Save updated list
            window["todos"].update(values=todos)
        case "Edit":
            todos_to_edit = values["todos"][0]           # List of selected todos (always a list)
            new_todo = values["todo"]               # Get new value from input
            
            todos = functions.get_todos()               # Load all todos again            
            index = todos.index(todos_to_edit)                  # Find selected item in the list
            todos[index] = new_todo                       # Replace it
            functions.write_todos(todos)                  # Save back to file
            window["todos"].update(values=todos)          # Refresh listbox in UI
        case "Complete":
            todos_to_complete = values["todos"][0]  #List down the current todos we have
            todos = functions.get_todos()
            todos.remove(todos_to_complete)     #using remove method we remove todos we have completed
            functions.write_todos(todos)        #and using write functions we write the todos
            window["todos"].update(values=todos) #update the todos in the window
            window["todo"].update(value=" ")
        case "Exit":
            break            
        case "todos" :
            window['todo'].Update(value=values['todos'][0])
        case sg.WIN_CLOSED: 
            break
    
window.close() 
