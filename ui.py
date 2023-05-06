THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
 
class QuizInterface():
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        
        self.window=Tk()
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.title("Quizzler")
        
        self.score_label=Label(text=f"Score:0",fg="white",bg=THEME_COLOR,font=("Arial",15,"bold"))
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,text="Hi!",width=200,font=("Arial",15,"italic"),fill=THEME_COLOR)
        
        self.tick=PhotoImage(file="./images/true.png")
        self.cross=PhotoImage(file="./images/false.png")
        
        self.tick_button=Button(image=self.tick, highlightthickness=0,command=self.hit_true)
        self.cross_button=Button(image=self.cross, highlightthickness=0,command=self.hit_false)
        
        self.score_label.grid(row=0,column=1)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.tick_button.grid(row=2,column=0)
        self.cross_button.grid(row=2,column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            next_question=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=next_question)
        else:
            self.canvas.itemconfig(self.question_text,text=f"Thanks for taking the quiz your score is:\n{self.quiz.score}/{self.quiz.question_number} ")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")    


    def hit_true(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

        self.update_score()

    def hit_false(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.update_score()



    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")    
        self.window.after(1000,self.get_next_question)

