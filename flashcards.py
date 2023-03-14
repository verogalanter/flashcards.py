import random
def quiz(correct):
    #make correct and incorrect empty lists
    #global correct
    #correct = []
    #global incorrect
    incorrect = []

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

    #give correct/incorrect value of 0
    for i in range(len(flashcards)):
        correct.append (0)
        incorrect.append (0)

    #create a list of flashcard questions
    questions = list(flashcards.keys())

    #shuffle the list of questions
    random.shuffle(questions)

    #initialize i
    i = 0

    #loops through each question and ask the answer
    global question
    for question in questions:
        if not_answered_correctly (i, correct):
            print(question)
            answer = input("Enter your answer:")
            if answer.lower() == flashcards[question].lower():
                print("Correct")
                correct [i] += 1
            else:
                print(f"Incorrect. The answer is {flashcards[question]}")
                incorrect [i] += 1
        i += 1

    return correct
    

def not_answered_correctly(i, correct):
    return correct[i] == 0

c = []
c = quiz(c)
print (c)
print ("Completed 1 quiz")
quiz(c)


#if correct == 0:
#   print (question)