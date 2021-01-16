from parse import parse

def visualize(q):
    print(q.question)
    chart = ("*"*q.score).ljust(10, ".")
    print("{}".format(chart))

class Level(object):
    def __init__(self, l, w, f):
        self.label = l
        self.weight = w
        self.questions = parse(f, self.label)
    def __str__(self):
        return "Level {} with {} questions and weight {}".format(self.label, len(self.questions), self.weight)
    def statistics(self):
        print("Statistics for {} questions:".format(self.label.upper()))
        if len(self.questions)==0:
            print("No questions found")
            return 0
        else:
            totAvg = 0
            for q in self.questions:
                visualize(q)
                totAvg += q.score
            print("Total average: {}".format(totAvg/len(self.questions)))
            return totAvg/len(self.questions)

if __name__=='__main__':
    l1 = Level("personal", 0.5, "personal.txt")
    print(l1)
    for q in l1.questions:
        print(q)
        visualize(q)
    