import Variables
import User
import random
import Functions

# determines if the topic needs to be incremented
def NextTopic(level, topic, baseline):
    # if the user has said keywords for a particular topic then Fai will change the conversation to that topic
    # an if statement for job is not needed as its the first topic Fai will talk about
    # however it is still important we record the job keywords is we need them when generating the fortune
    if Variables.countFamily >= 1:
        print("I sense that your family is very important to your fate, Let us explore this more")
        topic = 1
        Variables.countFamily = -100
        # current emotion has o be reset to prevent one negative response ruining the entire conversation
        Variables.currentEmotion = Variables.baseline
        return topic
    elif Variables.countLove >= 1:
        print("I can feel that love has great impact on your life, Lets explore this")
        topic = 2
        Variables.countLove = -100
        # current emotion has o be reset to prevent one negative response ruining the entire conversation
        Variables.currentEmotion = Variables.baseline
        return topic
    elif Variables.countFriends >= 1:
        print("I can see clearly that friendship means a great deal to you, Let me ask you some questions about this")
        topic = 3
        Variables.countFriends = -100
        # current emotion has o be reset to prevent one negative response ruining the entire conversation
        Variables.currentEmotion = Variables.baseline
        return topic

    # Increase the number of chats by one
    Variables.numberOfChats += 1
    # if the emotional level has gone below the baseline or if topic questions below three then return same topic
    if level >= baseline and Variables.numberOfChats < 3:
            return topic
    # else increase the topic by one and change number of topics to zero as its a new topic
    else:
        # current emotion has o be reset to prevent one negative response ruining the entire conversation
        Variables.currentEmotion = Variables.baseline
        Variables.numberOfChats = 0
        topic += 1
        print("Lets move one to another topic shall we")
        return topic

# recursive function that cycles through the topic questions while also appneding key words user has used
def TopicQuestions(topic):
    if topic == 0:
        # break user response into a list of words so the keywords can be appended and counts can be incremented
        Variables.questionAnswer = input(Functions.t.pop(Variables.topicIndexJob))
        Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
        Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
        # checks users statement for key words regarding this topic and appends them to a user list
        for x in Variables.keywordsJob:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsJob.append(y)
                    Variables.countJob += 1
        for x in Variables.keywordsFamily:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFam.append(y)
                    Variables.countFamily += 1
        for x in Variables.keywordsLove:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsLove.append(y)
                    Variables.countLove += 1
        for x in Variables.keywordsFriends:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFri.append(y)
                    Variables.countFriends += 1
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexJob -= 2
        TopicQuestions(Variables.topic)
    if topic == 1:
        Variables.questionAnswer = input(Functions.t.pop(Variables.topicIndexFam))
        Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
        Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
        # checks users statement for key words regarding this topic and appends them to a user list
        for x in Variables.keywordsJob:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsJob.append(y)
                    Variables.countJob += 1
        for x in Variables.keywordsFamily:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFam.append(y)
                    Variables.countFamily += 1
        for x in Variables.keywordsLove:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsLove.append(y)
                    Variables.countLove += 1
        for x in Variables.keywordsFriends:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFri.append(y)
                    Variables.countFriends += 1
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexFam -= 2
        TopicQuestions(Variables.topic)
    if topic == 2:
        Variables.questionAnswer = input(Functions.t.pop(Variables.topicIndexLove))
        Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
        Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
        # checks users statement for key words regarding this topic and appends them to a user list
        for x in Variables.keywordsJob:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsJob.append(y)
                    Variables.countJob += 1
        for x in Variables.keywordsFamily:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFam.append(y)
                    Variables.countFamily += 1
        for x in Variables.keywordsLove:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsLove.append(y)
                    Variables.countLove += 1
        for x in Variables.keywordsFriends:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFri.append(y)
                    Variables.countFriends += 1
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexLove -= 2
        TopicQuestions(Variables.topic)
    if topic == 3:
        Variables.questionAnswer = input(Functions.t.pop(Variables.topicIndexFnd))
        Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
        Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
        # checks users statement for key words regarding this topic and appends them to a user list
        for x in Variables.keywordsJob:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsJob.append(y)
                    Variables.countJob += 1
        for x in Variables.keywordsFamily:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFam.append(y)
                    Variables.countFamily += 1
        for x in Variables.keywordsLove:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsLove.append(y)
                    Variables.countLove += 1
        for x in Variables.keywordsFriends:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFri.append(y)
                    Variables.countFriends += 1
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexFnd -= 2
        TopicQuestions(Variables.topic)

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