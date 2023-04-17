import random
import json
import os


#define dictionary of fashcards with questions and answers 
flashcards = {
        "What is red in Spanish": "rojo", "What is orange in Spanish": "anaranjado", "What is yellow in Spanish": "amarillo", 
        "What is green in Spanish": "verde", "What is blue in Spanish": "azul", "What is purple in Spanish": "morado",
        "What is white in Spanish": "blanco", "What is black in Spanish": "negro", "What is brown in Spanish": "marrón",   
        "What is pink in Spanish": "rosado", "What is grey in Spanish": "gris", "What is violet in Spanish": "violeta", 
        "What is indigo in Spanish": "índigo", "What is turquoise in Spanish": "turquesa", "What is magenta in Spanish": "magenta",  
        "What is gold in Spanish": "oro","What is silver in Spanish": "plata","What is bronze in Spanish": "bronce",
        "What is lilac in Spanish": "lila", "What is scarlet in Spanish": "escarlata"   
    }   

correct = {}
incorrect = {}

#give correct/incorrect value of 0
for key in flashcards:
    correct[key]= 0
    incorrect[key]= 0

if os.path.exists ("flashcards.txt"):
    with open ("flashcards.txt", "r") as f:
        correct = json.load(f)

def quiz(correct):
    #make correct and incorrect empty lists
    # global correct 
    # correct = {}
    # global incorrect


    #create a list of flashcard questions
    questions = list(flashcards.keys())

    #shuffle the list of questions
    random.shuffle(questions)

    #initialize i
    i = 0

    #loops through each question and ask the answer
    for question in questions:
        if not_answered_correctly (question, correct):
            print(question)
            answer = input("Enter your answer:")
            if answer.lower() == flashcards[question].lower():
                print("Correct")
                correct [question] += 1
            else:
                print(f"Incorrect. The answer is {flashcards[question]}")
                incorrect [question] += 1
        i += 1

    return correct
    

def not_answered_correctly(key, correct):
    return correct[key] == 0

while True:
    correct = quiz(correct)
    print (correct)
    print ("Completed Quiz!")
    ask = input ("Would you like to continue? ")
    if ask == "no":
        break
    
with open ("flashcards.txt", "w") as f:
    json.dump(correct, f)


#if correct == 0:
#  print (question)