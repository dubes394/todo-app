date = input("Enter today's date : ")
mood = input("How would you rate your mood on 1-10 : ")
thoughts = input("Let your thoughts flow: \n")

    
with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood)
    file.write(thoughts)