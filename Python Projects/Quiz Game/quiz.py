from quiz_data import data
import random

def play():
    score = 0
    questions = data.copy()
    random.shuffle(questions)

    for question in questions:
        options = question["options"].copy()
        random.shuffle(options)
        print("Question:", question["question"])
        print("Options:")
        for i, option in enumerate(options, 1):
            print(f"   {i}. {option}")

        answer_index = int(input("Enter the option number (1-4): "))
        selected_option = options[answer_index - 1]

        if selected_option == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")

    print(f"\nQuiz Over! Your total score = {score}/{len(data)}")

    while True:
        answer_sheet=input("Do you want the correct Answer Sheet to all Questions? (\"Y\" or \"N\")")
        if answer_sheet.upper()=="Y":
            print("Correct Answers Sheet:")
            for q in data:
                print(f"Question: {q['question']}")
                print(f"Answer: {q['answer']}")
        elif answer_sheet.upper() == "N":
            exit()
        else:
            print("Enter Valid input!")
play()
