'''
This class represents a single question parsed from a txt file. 
'''
class Question(object):
    '''
    This function initializes an instance of the question class.
    @params 
        l: String, represents level of difficulty (ex. 'easy')
        q: String, question
        n: String, notes
    @modifies
        self.label: String
        self.question: String
        self.notes: String
        self.score: Int
    '''
    def __init__(self, l, q, n):
        self.label = l.lower()
        self.question = q
        self.notes = n
        self.score = 0
    '''
    This function returns a string displaying variables in Question object.
    @returns
        s: String containing level and questions
    '''
    def __str__(self):
        return '{} Level:\n{}'.format(self.label, self.question)