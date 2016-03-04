import Variables
import User
import random
import math


def nexttopic(level, topic, baseline):
    if level != baseline and level < baseline:
        chatAI(topic, level, Variables.numberOfChats)
    else:
        return Variables.Topic + 1


def chatAI(topic, level, numberOfChats):
    numberOfChats -= 1
    if numberOfChats > 0:
        Variables.Answer = input(FaiAnswer(level))
        User.analyse(Variables.Answer, Variables.Topics[Variables.Topic])
        load(Variables.Answer, Variables.FAIanswer)
    else:
        Variables.Topic += 1
    return


def FaiAnswer(level):
    Variables.FAIreply = ""

    if level < 0 and level > -2:
        Variables.FAIanswer = Variables.lines[random.randrange(0, 2)]
    if level < -2 and level > -5:
        Variables.FAIanswer = Variables.lines[random.randrange(3, 5)]
    if level == 0:
        Variables.FAIanswer = Variables.lines[random.randrange(6, 8)]
    if level > 0 and level < 2:
        Variables.FAIanswer = Variables.lines[random.randrange(9, 11)]
    if level > 2 and level < 5:
        Variables.FAIanswer = Variables.lines[random.randrange(12, 14)]

    return Variables.FAIanswer


def load(Answer, FaiAnswer):
    Bestmatch = 0
    answerSSD = 0
    SSD = 0
    ID = 0

    for char in Answer:
        answerSSD += ord(char)

    for line in Variables.SaveResponses:
        if line.isupper():
            ID += 1
            continue
        if line.strip('-').isdigit():
            ID += 1
            continue
        else:
            ID += 1
            for char in line:
                SSD += ord(char)

            if SSD > SSD:
                Bestmatch = SSD
                Variables.FAIanswer = line
                continue
            if SSD < Bestmatch:
                continue
            if SSD > answerSSD:
                continue
    save(Answer, FaiAnswer)
    print("SSD:", SSD)
    print("AnswerSSD:", answerSSD)
    print("ID:", ID)
    return Variables.FAIanswer


def save(useranswer, answer):
    Variables.SaveResponses.write(useranswer)
    Variables.SaveResponses.write("\n")
    Variables.SaveResponses.write(answer)
    Variables.SaveResponses.write("\n")
    return
