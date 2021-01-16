from Question import Question

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
    rules = "Welcome! Before we begin, here are the rules and instructions for usage:\n \
        1. You, the administrator of the test, will be responsible for relaying the questions to the partner being questioned.\
            You will be responsible for assesing answers and entering a point value 0-10. \n \
        2. Some questions will have notes with them. When these are displayed, you should take note of them before determining a score. \n \
        3. There are up to four sections: personal, easy, medium, and hard. These must be provided as separate txt files. \n \
        4. Results will be displayed once all questions have been answered."
    print(rules)
    adminName, questions = setup()
    cumScore = 0
    print("Alright, {}, let's start!".format(adminName))

    '''
    Personal Questions (name, age, etc)
    '''
    if personal in questions:
        print("-"*25 + "PERSONAL" + "-"*25)
        count = 

    '''
    Easy Questions
    '''
    print("-"*25 + "EASY" + "-"*25)

    '''
    Medium Questions
    '''
    print("-"*25 + "MEDIUM" + "-"*25)

    '''
    Hard Questions
    '''
    print("-"*25 + "HARD" + "-"*25)

    '''
    Results & Customization
    '''
    graphs = input("Calculating results...do you want to see graphs? (y/n)").strip().lower()