def parse(f):
    cleanQs = []
    try:
        for question in f.open():
            question = question.strip()
            if not question.find("?"):
                print("Error, {} is not a question! Skipped.".format(question))
            else:
                cleanQs.append(question)
        return cleanQs
    except(IOError):
        print("Could not find file {}".format(f))