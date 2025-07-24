wait_list = ["sam", "raju", "jon"]
wait_list.sort()

for index, item in enumerate(wait_list):
    row = f"{index +1 }.{item.capitalize()}"
    print(row)