from Question import Question

def parse(f, label):
    cleanQs = []
    try:
        for line in open(f):
            question = line.strip().split("|")
            if not question[0].find("?"):
                print("Error, {} is not a question! Skipped.".format(question[0]))
            elif len(question) > 1:
                cleanQs.append(Question(label, question[0], question[1] ))
            else:
                cleanQs.append(Question(label, question[0], 'N/A'))
        return cleanQs
    except(IOError):
        print("Could not find file {}".format(f))