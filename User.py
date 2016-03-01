import string
import Variables
import Dictionary
import AI


def username(username):
    Variables.Name = Variables.UserName.split(" ")
    if 'I' in Variables.Name:
        Variables.Name.remove('I')

    if len(Variables.Name) > 2:
        for x in Variables.Name:
            if x.istitle():
                Variables.TrueName.append(x)
        Variables.Name.clear()
        Variables.Name = Variables.TrueName.pop()
    if len(Variables.Name) == 1 and 2:
        Variables.Name = Variables.Name.pop()
    if len(Variables.Name) == 0:
        print("I see... well, since you didn't enter a name, I'll call you Anonymous!")
        Variables.Name = "Anonymous"
    return username


def analyse(response, topic):
    exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.

    Variables.QuestionAnswerOne = response
    Variables.QuestionAnswerOne = ''.join(ch for ch in Variables.QuestionAnswerOne if ch not in exclude)
    Variables.QuestionAnswerOne = Variables.QuestionAnswerOne.lower()  # This turns all uppercase characters into lower.
    Variables.QuestionAnswerOne = Variables.QuestionAnswerOne.split(" ")  # This splits the string into a list of words.
    for x in Variables.QuestionAnswerOne:
        if x in Dictionary.Words:
            Variables.Index = Dictionary.Words.index(x)
            Variables.Emotion += int(Dictionary.Words.pop(Variables.Index + 1))
        if x not in Dictionary.Words:
            Variables.Emotion += 0
    Variables.baseline = Variables.baseline + Variables.Emotion

    Variables.Tempnexttopic = AI.nexttopic(Variables.Emotion, topic, Variables.baseline)

    return Variables.Emotion, Variables.Tempnexttopic
