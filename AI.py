import string
import Dictionary
import Variables

def nexttopic(level, topic, baseline):
    if level > baseline:
        chatAI(topic, level, Variables.numberOfChats)
    else:
        return Variables.Topic  + 1


def chatAI():
    