from tkinter import *
from quiz_brain import QuizBrain

TEXT_FONT = ("Times New Roman", 27, "italic")
ANSWER_FONT = ("Times New Roman", 50, "italic", "bold")
BUTTON_FONT = ("Times New Roman", 20, "bold")
THEME_COLOUR = "#c7faff"
RIGHT_ANSWER_COLOUR = "#02fa2c"
WRONG_ANSWER_COLOUR = "#fc0303"
BUTTON_COLOUR = "#b8ffc2"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        # Window
        self.window = Tk()
        self.window.title("Name Him")
        self.window.config(padx=20, pady=20, bg=THEME_COLOUR)

        # Frame
        self.frame = Frame(self.window)  # Here we are using to lift or lower the frame to make widgets visible or invis
        self.frame.config(bg=THEME_COLOUR)
        self.frame.grid()

        # Images
        background_image = PhotoImage(file="Images/background.png")
        Abraham_Lincoln_image = PhotoImage(file="images/leader images/Abraham Lincoln.png")
        Adolf_Hitler_image = PhotoImage(file="images/leader images/Adolf Hitler.png")
        Fidel_Castro_image = PhotoImage(file="images/leader images/Fidel Castro.png")
        Gautama_Buddha_image = PhotoImage(file="images/leader images/Gautama Buddha.png")
        Karl_Marx_image = PhotoImage(file="images/leader images/Karl Marx.png")
        Mahatma_Gandhi_image = PhotoImage(file="images/leader images/Mahatma Gandhi.png")
        Martin_Luther_King_Jr_image = PhotoImage(file="images/leader images/Martin Luther King, Jr..png")
        Napoleon_Bonaparte_image = PhotoImage(file="images/leader images/Napoleon Bonaparte.png")
        Nelson_Mandela_image = PhotoImage(file="images/leader images/Nelson Mandela.png")
        Winston_Churchil_image = PhotoImage(file="images/leader images/Winston Churchil.png")

        # Canvas
        self.canvas = Canvas(self.window, width=800, height=400)
        self.canvas.create_image(400, 200, image=background_image)
        self.canvas_text = self.canvas.create_text(400, 200,
                                                   width=800,
                                                   text="",
                                                   font=TEXT_FONT)
        self.canvas.grid(row=1, column=1, columnspan=3, rowspan=2, in_=self.frame)

        # Buttons

        self.button1 = Button(self.window, image=Abraham_Lincoln_image,
                              highlightthickness=0,
                              command=self.button1_pressed)
        self.button1.grid(row=0, column=1, in_=self.frame)

        self.button2 = Button(self.window, image=Adolf_Hitler_image,
                              highlightthickness=0,
                              command=self.button2_pressed)
        self.button2.grid(row=0, column=2, in_=self.frame)

        self.button3 = Button(self.window, image=Fidel_Castro_image,
                              highlightthickness=0,
                              command=self.button3_pressed)
        self.button3.grid(row=0, column=3, in_=self.frame)

        self.button4 = Button(self.window, image=Gautama_Buddha_image,
                              highlightthickness=0,
                              command=self.button4_pressed)
        self.button4.grid(row=1, column=4, in_=self.frame)

        self.button5 = Button(self.window, image=Karl_Marx_image,
                              highlightthickness=0,
                              command=self.button5_pressed)
        self.button5.grid(row=2, column=4, in_=self.frame)

        self.button6 = Button(self.window, image=Mahatma_Gandhi_image,
                              highlightthickness=0,
                              command=self.button6_pressed)
        self.button6.grid(row=3, column=3, in_=self.frame)

        self.button7 = Button(self.window, image=Martin_Luther_King_Jr_image,
                              highlightthickness=0,
                              command=self.button7_pressed)
        self.button7.grid(row=3, column=2, in_=self.frame)

        self.button8 = Button(self.window, image=Napoleon_Bonaparte_image,
                              highlightthickness=0,
                              command=self.button8_pressed)
        self.button8.grid(row=3, column=1, in_=self.frame)

        self.button9 = Button(self.window, image=Nelson_Mandela_image,
                              highlightthickness=0,
                              command=self.button9_pressed)
        self.button9.grid(row=2, column=0, in_=self.frame)

        self.button10 = Button(self.window, image=Winston_Churchil_image,
                               highlightthickness=0,
                               command=self.button10_pressed)
        self.button10.grid(row=1, column=0, in_=self.frame)

        # Once User guesses answer these buttons will be active
        self.see_answer_button = Button(self.window, text="PERSON", font=BUTTON_FONT,
                                        highlightthickness=0,
                                        bg=BUTTON_COLOUR,
                                        state="disabled",
                                        command=self.show_person)  # Show the person's name on canvas
        self.see_answer_button.grid(row=1, column=5, in_=self.frame)

        self.see_text_button = Button(self.window, text="WORK", font=BUTTON_FONT,
                                      highlightthickness=0,
                                      bg=BUTTON_COLOUR,
                                      state="disabled",
                                      command=self.show_work)  # Show the person's work on canvas
        self.see_text_button.grid(row=2, column=5, in_=self.frame)

        self.next_question_button = Button(self.window, text="Next Question",
                                           font=BUTTON_FONT,
                                           bg=BUTTON_COLOUR,
                                           state="disabled",
                                           command=self.get_next_question)
        self.next_question_button.grid(row=3, column=5,
                                       in_=self.frame)  # Moves to next ques by calling get_next_question

        # Dictionaries
        # These are to call a particular button's attributes according to the person's name given by user
        # for eg. the correct answer button picture of the person is shown rest are hidden and disabling buttons
        self.person_to_button = {
            "Abraham Lincoln": self.button1,
            "Adolf Hitler": self.button2,
            "Fidel Castro": self.button3,
            "Gautama Buddha": self.button4,
            "Karl Marx": self.button5,
            "Mahatma Gandhi": self.button6,
            "Martin Luther King, Jr.": self.button7,
            "Napoleon Bonaparte": self.button8,
            "Nelson Mandela": self.button9,
            "Winston Churchil": self.button10
        }
        # This is for reassigning commands to the resp. functions as when we are in answer mode all the commands are
        # deleted from each person's button since I don't wanna use the disabled method since it makes pics look dizzy
        self.person_to_command = {
            "Abraham Lincoln": self.button1_pressed,
            "Adolf Hitler": self.button2_pressed,
            "Fidel Castro": self.button3_pressed,
            "Gautama Buddha": self.button4_pressed,
            "Karl Marx": self.button5_pressed,
            "Mahatma Gandhi": self.button6_pressed,
            "Martin Luther King, Jr.": self.button7_pressed,
            "Napoleon Bonaparte": self.button8_pressed,
            "Nelson Mandela": self.button9_pressed,
            "Winston Churchil": self.button10_pressed
        }

        # Label
        self.score_label = Label(self.window, text="Score:0", font=TEXT_FONT, padx=20, pady=20, bg=THEME_COLOUR)
        self.score_label.grid(row=0, column=5, in_=self.frame)

        self.get_next_question()  # Calling to get the new question when object of this class is initialised
        self.window.mainloop()

    # These are the texts returned to answer checking mech when a button with a particular person's picture is clicked
    def button1_pressed(self):
        self.give_feedback("Abraham Lincoln")

    def button2_pressed(self):
        self.give_feedback("Adolf Hitler")

    def button3_pressed(self):
        self.give_feedback("Fidel Castro")

    def button4_pressed(self):
        self.give_feedback("Gautama Buddha")

    def button5_pressed(self):
        self.give_feedback("Karl Marx")

    def button6_pressed(self):
        self.give_feedback("Mahatma Gandhi")

    def button7_pressed(self):
        self.give_feedback("Martin Luther King, Jr.")

    def button8_pressed(self):
        self.give_feedback("Napoleon Bonaparte")

    def button9_pressed(self):
        self.give_feedback("Nelson Mandela")

    def button10_pressed(self):
        self.give_feedback("Winston Churchil")

    def show_work(self):
        """Show the question... i.e. work of the person on the canvas...
        gets the question text globally from get_next_question"""
        self.canvas.itemconfig(self.canvas_text, text=q_text, font=TEXT_FONT)

    def show_person(self):
        """Show the answer... i.e. name of the person on the canvas...
        gets the correct answer text globally from give_feedback"""
        self.canvas.itemconfig(self.canvas_text, text=f"Correct Answer: {correct_answer}", font=ANSWER_FONT)

    def get_next_question(self):
        """Changes the format of the screen to question mode and gets new question from quizbrain class if
         there are questions still left... at the end of quiz print the score on screen"""

        self.question_mode()
        self.enable_person_buttons()

        global q_text
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.show_work()
        else:
            q_text = f"You Have reached the end of the quiz \nYour Score :{self.quiz.score}"
            self.show_work()
            self.disable_person_buttons()  # Disbaling all the buttons at the end of the quiz

    def give_feedback(self, person_guess):
        """Changes the format of the screen to answer mode according to the answer after
         checking the question from the quizbrain class"""
        global correct_answer
        correct_answer = self.quiz.p_name
        self.disable_person_buttons(correct_answer=correct_answer)

        self.canvas.itemconfig(self.canvas_text, text=f"You chose: {person_guess}\n"
                                                      f"Correct Answer: {correct_answer}", font=ANSWER_FONT)
        is_right = self.quiz.check_answer(person_guess)
        self.answer_mode(is_right)

    def disable_person_buttons(self, correct_answer=None):
        """Deletes all the person's button;s commands ...
        Takes a correct answer string as an argument if entered otherwise None...
        Show the correct answer button picture rest hide in the answer mode"""
        for person in self.person_to_button:
            self.person_to_button[person]['command'] = 0
            self.person_to_button[person]['relief'] = 'sunken'
            if not correct_answer == None:
                if not person == correct_answer:
                    self.person_to_button[person].lower(self.frame)

    def enable_person_buttons(self):
        """Reassign the repective commands to each buttons ...
        And show all the buttons on the frame"""
        for person in self.person_to_button:
            self.person_to_button[person].lift(self.frame)
            self.person_to_button[person]['command'] = self.person_to_command[person]
            self.person_to_button[person]['relief'] = 'raised'

    def question_mode(self):
        """Sets the window,frame,score label colour to theme colour ...
        And disables the person,work and next_question buttons """
        self.window.config(bg=THEME_COLOUR)
        self.frame.config(bg=THEME_COLOUR)
        self.score_label.config(bg=THEME_COLOUR)
        self.see_text_button.config(state="disabled")
        self.see_answer_button.config(state="disabled")
        self.next_question_button.config(state="disabled")

    def answer_mode(self, is_right):
        """Sets the window,frame,score label colour to green if answer right otherwise red...
        Enables the person,work and next_question buttons
        Updates the Score label to the current score"""
        score = self.quiz.score
        if is_right:
            self.frame.config(bg=RIGHT_ANSWER_COLOUR)
            self.window.config(bg=RIGHT_ANSWER_COLOUR)
            self.score_label.config(bg=RIGHT_ANSWER_COLOUR)
        else:
            self.frame.config(bg=WRONG_ANSWER_COLOUR)
            self.window.config(bg=WRONG_ANSWER_COLOUR)
            self.score_label.config(bg=WRONG_ANSWER_COLOUR)
        self.score_label.config(text=f"Score:{score}")
        self.see_text_button.config(state="normal")
        self.see_answer_button.config(state="normal")
        self.next_question_button.config(state="normal")
