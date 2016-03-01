import Variables
import User

def nexttopic(level, topic, baseline):
    if level > baseline:
        chatAI(topic, level, Variables.keywords, Variables.numberOfChats)
    else:
        return Variables.Topic + 1


def chatAI(topic, level, keywords, numberOfChats):
    numberOfChats = Variables.numberOfChats
    topic = Variables.Topics[Variables.Topic]
    numberOfChats -= 1
    if numberOfChats > 0:
        #  Variables.Answer = input(FaiAnswer(keywords, level, topic))
        User.analyse(Variables.Answer, Variables.Topics[Variables.Topic])

        #  Will have to enter keyword statements here!!

    else:
        Variables.Topic += 1
    return


#def FaiAnswer(keywords, level, topic):
