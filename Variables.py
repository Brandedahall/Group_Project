import string
import Dictionary
#import files

UserName = ""
# The user's name is stored here.

exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.

#QuestionAnswerOne = ""
# The user's answers will be stored here.

Word_General = ""

# We want some variables relating to a 3d graph here. The graph will need to store the plotted points for each question.

#classImplementation
class usrAns():
    print("*******")
    def __init__(self, quesNo, quesAns):
        self.quesNo = quesNo
        self.quesAns = quesAns

        #does the same as where they used to be, just in a function
        quesAns = ''.join(ch for ch in quesAns if ch not in exclude)
        quesAns = quesAns.lower()  # This turns all uppercase characters into lower case
        quesAns = quesAns.split(" ")  # This splits the string into a list of words.

        print(quesAns)  # Prints the list of the words from the user's reply.

        for Word in quesAns:
            if Word in Dictionary.ThingsList_General:
                Word_General = Word

    def printAns():
        print(Word_General)
        print("This is a test")
