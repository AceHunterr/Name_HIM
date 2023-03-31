from ui import QuizInterface
from data import persons_data
from question_model import Question
from quiz_brain import  QuizBrain


persons_list = [] # List of all the persons and their work as an object of Class Question Model

for person in persons_data:
    person_name = person
    person_work = persons_data[person]
    new_person = Question(person_name,person_work)
    persons_list.append(new_person)

quiz = QuizBrain(persons_list) # Adding all the functionality of our quizbrain to each object in the list
quiz_interface = QuizInterface(quiz) # Passing over the quiz to our UI window

