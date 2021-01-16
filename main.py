from Level import *
'''
Welcome to the Boyfriend Interrogator! 
'''

def setup():
    print("First, a few questions for the administrator:")
    adminName = input("What is your name? ").strip().title()
    print("Hello, {}!".format(adminName))

    qtypes = ['personal', 'easy', 'medium', 'hard']
    levelObjects = []
    default = input("Do you want to use default settings (y/n)? ").strip().lower()
    if default=="y":
        for level in qtypes:
            levelObjects.append(Level(level, 1, level+".txt")) 
    else:
        for level in qtypes:
            temp = input("File for {} questions? ".format(level)).strip()
            w = float(input("What weight should {} questions be (decimal 0.0-1.0)? ".format(level)))
            levelObjects.append(Level(level, w, temp))        
    return adminName, levelObjects

if __name__=='__main__':
    rules = "Welcome! Before we begin, here are the rules and instructions for usage:\n"
    rules += "1. You, the administrator of the test, will be responsible for relaying the " 
    rules += "questions to the partner being questioned. You will be responsible for assesing "
    rules += "answers and entering a point value 0-10. \n2. Some questions will have notes "
    rules += "with them. When these are displayed, you should take note of them before "
    rules += "determining a score. \n3. There are up to four sections: personal, easy, medium, "
    rules += "and hard. These must be provided as separate txt files. \n4. Results will be "
    rules += "displayed once all questions have been answered."
    print(rules)
    adminName, questions = setup()
    print("\nAlright, {}, let's start!\n".format(adminName))

    '''
    Questions
    '''
    for level in questions:
        count = 0
        print((level.label.upper()).center(50, "-"))
        for q in level.questions:
            print("\nQuestion {}:".format(count))
            print("Notes: {}".format(q.notes), sep="")
            q.score = int(input(q.question + " [SCORE]: "))    
    
    '''
    Results & Customization
    '''
    graphs = input("Calculating results...do you want to see graphs? (y/n)").strip().lower()
    print("RESULTS".center(50, "-"))
    totalScore = 0
    for level in questions:
        totalScore += level.statistics()
    print("Your total score: {}/10".format(totalScore/4))
    