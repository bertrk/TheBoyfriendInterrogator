from Question import Question
import pyplot as plt

'''
Welcome to the Boyfriend Interrogator! 
'''
def setup():
    print("Welcome! First, a few questions for the administrator:")
    adminName = input("What is your name?").strip().centertitle()
    print("Welcome, {}!".format(adminName))

    qtypes = ['personal', 'easy', 'medium', 'hard']
    questionObjects = []
    for level in qtypes:
        temp = input("File for {} questions? (hit enter if none)".format(level)).strip()
        if temp:
            questionObjects.append(Question(level, temp))

    return adminName, questionObjects

if __name__=='__main__':
    adminName, questions = setup()

    '''
    Personal Questions (name, age, etc)
    '''

    '''
    Easy Questions
    '''

    '''
    Medium Questions
    '''

    '''
    Hard Questions
    '''