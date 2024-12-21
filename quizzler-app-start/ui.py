from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.score = Label(text=f"Score {0}", bg=THEME_COLOR, highlightthickness=0)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125,width=280, text=f"{""}", font=("Arial", 20, "italic"),
                                                     fill="black",)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)

        self.false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




















