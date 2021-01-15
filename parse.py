def parse(f):
    cleanQs = {}
    try:
        for line in f.open():
            question = line.strip().split("|")
            if not question[0].find("?"):
                print("Error, {} is not a question! Skipped.".format(question[0]))
            elif len(question) > 1:
                cleanQs[question[0].strip()] = question[1:]
            else:
                cleanQs[question[0].strip()] = []
        return cleanQs
    except(IOError):
        print("Could not find file {}".format(f))