FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):        #*We make filepath a default parameter by assigning the value.
    """ Read a text file and return the list 
    of to-do items"""
    with open(filepath, 'r') as file_local:    #*You're opening the file in read mode ('r') to get the existing todos.
        todos_local = file_local.readlines()                #*This reads all lines from the file into a list.            
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH): #*The order of non-default parameter and default parameter changed, because when we call the function we have to pass argument and that argument should go to the non-default first rather than default one.
    """ Write the to-do items list in the text files."""
    with open(filepath, "w") as file:           #*This re-opens the file in write mode ('w'), which, Erases everything in the file, Prepares to write a new version
        file.writelines(todos_arg)              #*This writes all the lines (including the newly added one) back to the file