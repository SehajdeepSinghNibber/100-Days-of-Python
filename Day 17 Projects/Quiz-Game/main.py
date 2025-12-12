from data import Question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_bank = []

for question in Question_data:
    question_text = question["text"]
    answer_text = question["answer"]
    new_question = Question(question_text, answer_text)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")