'''
This class represents a list of questions parsed from a txt file. 
'''
from parse import parse
class Question(object):
    '''
    This function initializes an instance of the question class.
    @params 
        l: String, represents level of difficulty (ex. 'easy')
        filename: String, name of file from which to extract questions (ex. 'easy.txt')
    @modifies
        self.level: String
        self.questions: calls parse from parse.py, returns list of strings representing questions
    '''
    def __init__(self, l, filename):
        self.level = l.lower()
        self.questions = parse(filename)
    
    '''
    This function returns a string displaying variables in Question object.
    @returns
        s: String containing level and questions
    '''
    def __str__(self):
        s = '{} Questions:\n'.format(self.level)
        for q in self.questions:
            s += q
            s += '\n'
        return s