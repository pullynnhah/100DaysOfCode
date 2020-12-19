from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    FONT_Q = ("Letters for Learners", 24, "bold italic")
    FONT_SCORE = ("Letters for Learners", 16, "bold")
    THEME_COLOR = "#7A047A"
    GREEN = "#AEFF78"
    RED = "#FA7878"

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=self.THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas_text = self.canvas.create_text(
            150, 125,
            text="Question HERE",
            font=self.FONT_Q,
            fill=self.THEME_COLOR,
            width=280
        )
        
        self.score = Label(text=f"Score: {self.quiz.score}", fg="white",
                           bg=self.THEME_COLOR, font=self.FONT_SCORE)
        
        true = PhotoImage(file="./images/true.png")
        false = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true, highlightthickness=0, command=self.press_true)
        self.false_button = Button(image=false, highlightthickness=0, command=self.press_false)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score.grid(column=1, row=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self. get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=question)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg=self.GREEN)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg=self.RED)
        self.window.after(1000, self.get_next_question)

    def press_true(self):
        self.give_feedback(is_correct=self.quiz.check_answer("True"))

    def press_false(self):
        self.give_feedback(is_correct=self.quiz.check_answer("False"))
