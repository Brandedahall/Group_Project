import string
import Variables
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
    return Variables.Name


def analyse(response, topic):
    exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.

    Variables.QuestionAnswer = response
    Variables.QuestionAnswer = ''.join(ch for ch in Variables.QuestionAnswer if ch not in exclude)
    Variables.QuestionAnswer = Variables.QuestionAnswer.lower()  # This turns all uppercase characters into lower.
    Variables.QuestionAnswer = Variables.QuestionAnswer.split(" ")  # This splits the string into a list of words.
    for x in Variables.QuestionAnswer:
        if x in Variables.Words:
            Variables.Index = Variables.Words.index(x)
            Variables.Emotion += int(Variables.Words.pop(Variables.Index + 1))
        if x not in Variables.Words:
            Variables.Emotion += 0

    Variables.Topic = AI.nexttopic(Variables.Emotion, topic, Variables.baseline)

    return Variables.Emotion, Variables.Topic
