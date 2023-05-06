from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank=[]
for i in range (len(question_data)):
    """Appending text and answer"""
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))

quiz=QuizBrain(question_bank)
# quiz.next_question()
quiz_ui=QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You have completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
