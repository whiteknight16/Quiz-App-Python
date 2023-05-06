
class QuizBrain():
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
        self.current_question = None


    def next_question(self):
        self.current_question=self.question_list[self.question_number]
        self.question_number+=1
        return f"Q.{self.question_number}:{self.current_question.text}"

    def still_has_questions(self):
        if (self.question_number<len(self.question_list)):
            return True
        
    def check_answer(self,user_a):
        correct_a=self.current_question.answer
        if user_a.capitalize() ==correct_a:
            self.score+=1
            return True
        else:
            return False


