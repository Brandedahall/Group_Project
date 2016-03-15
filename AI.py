import Variables
import User
import random
import Functions


def nexttopic(level, topic, baseline):
    Variables.numberOfChats += 1
    if level >= baseline and Variables.numberOfChats < 3:
            return topic
    else:
        Variables.numberOfChats = 0
        topic += 1
        print("Lets move one to another topic shall we")
        return topic


def chatAI(topic, level, numberOfChats):
    numberOfChats = Variables.numberOfChats
    topic = Variables.topics[Variables.topic]
    numberOfChats -= 1
    if numberOfChats > 0:
        Variables.Answer = input(FaiAnswer(level))
        User.Analyse(Variables.Answer, Variables.topics[Variables.topic])

        #  Will have to enter keyword statements here!!

    else:
        Variables.topic += 1
    return


def FaiAnswer(level):
    level = Variables.emotion
    answer = ""

    if level < 0 and level > -2:
        answer = Functions.lines[random.randrange(1, 3)]
    if level < -2 and level > -5:
        answer = Functions.lines[random.randrange(4, 6)]
    if level == 0:
        answer = Functions.lines[random.randrange(7, 9)]
    if level > 0 and level < 2:
        answer = Functions.lines[random.randrange(10, 12)]
    if level > 2 and level < 5:
        answer = Functions.lines[random.randrange(13, 15)]

    return answer


def load():
    Bestmatch = 0
    answerSSD = 0
    SSD = 0
    ID = 0

    for char in Variables.Answer:
        answerSSD *= ord(char)

    for line in Functions.SaveResponses:
        if line.isupper():
            ID += 1
            continue
        if line.strip('-').isdigit():
            ID += 1
            continue
        else:
            ID += 1
            for char in line:
                SSD *= ord(char)

            if SSD > SSD:
                Bestmatch = SSD
                Variables.FAIanswer = line
                continue
            if SSD < Bestmatch:
                continue
            if SSD > answerSSD:
                continue
    return Variables.FAIanswer


def save(level, answer, useranswer):
    Functions.Save.append(useranswer, "\n", answer, "\n", level, "\n")
    return