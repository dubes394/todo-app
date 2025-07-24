def get_average():
    with open("files/data.txt", 'r') as file:
        data =file.readlines()
        
    values = data[1:]
    values = [float(i) for i in values]
    
    average_local = sum(values) / len(values)
    return average_local

    
average = get_average()
print(average)

# def num_checker(n):
#     if n%2 == 0:
#         return "Even"
#     else:
#         return "odd"

# print(num_checker(68))