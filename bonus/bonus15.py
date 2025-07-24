import json

with open("questions.json", "r") as file:
    content = file.read()
    
data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, option in enumerate(question["options"]):
        print(index + 1  , "-", option)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice    
    
score = 0
        
for index, question in enumerate(data):
    if question["user_choice"] == int(question["correct_answer"]):
        score = int(score + 1)
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
        
    message = f"{index + 1} {result} - Your answer: {question["user_choice"]}", \
        f"{index +1}  - Correct Answer: {question["correct_answer"]}"
    print(message)
             
print(score)