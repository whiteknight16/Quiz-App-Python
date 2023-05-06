from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank=[]
for i in range (len(question_data)):
    """Appending text and answer"""
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))

quiz=QuizBrain(question_bank)
quiz_ui=QuizInterface(quiz)
