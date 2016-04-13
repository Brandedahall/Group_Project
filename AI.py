import Variables
import User
import time


# determines if the topic needs to be incremented
def NextTopic(level, topic, baseline):
    # if the user has said keywords for a particular topic then Fai will change the conversation to that topic
    # an if statement for job is not needed as its the first topic Fai will talk about
    # however it is still important we record the job keywords is we need them when generating the fortune
    if Variables.countFamily >= 1 and Variables.currentEmotion >= Variables.baseline and len(Variables.questionsFam) == 3:
        time.sleep(Variables.topicRND)
        print("I sense that your family is very important to your fate, Let us explore this more")
        if topic == 1:
            Variables.numberOfChats += 1
        else:
            Variables.numberOfChats = 0
        topic = 1
        Variables.countFamily = -100
        # because the topic is changing we store the emotional level of the current topic
        if topic == 0:
            Variables.emotionJob = Variables.currentEmotion
        elif topic == 1:
            Variables.emotionFamily = Variables.currentEmotion
        elif topic == 2:
            Variables.emotionLove = Variables.currentEmotion
        elif topic == 3:
            Variables.emotionFriend = Variables.currentEmotion
        # current emotion has o be reset to prevent one negative response ruining the entire conversation
        Variables.currentEmotion = Variables.baseline
        return topic
    elif Variables.countLove >= 1 and Variables.currentEmotion >= Variables.baseline and len(Variables.questionsLove) == 3:
        time.sleep(Variables.topicRND)
        print("I can feel that love has great impact on your life, Lets explore this")
        if topic == 2:
            Variables.numberOfChats += 1
        else:
            Variables.numberOfChats = 0
        topic = 2
        Variables.countLove = -100
         # because the topic is changing we store the emotional level of the current topic
        if topic == 0:
            Variables.emotionJob = Variables.currentEmotion
        elif topic == 1:
            Variables.emotionFamily = Variables.currentEmotion
        elif topic == 2:
            Variables.emotionLove = Variables.currentEmotion
        elif topic == 3:
            Variables.emotionFriend = Variables.currentEmotion
        # current emotion has o be reset to prevent one negative response ruining the entire conversation
        Variables.currentEmotion = Variables.baseline
        return topic
    elif Variables.countFriends >= 1 and Variables.currentEmotion >= Variables.baseline and len(Variables.questionsFri) == 3:
        time.sleep(Variables.topicRND)
        print("I can see clearly that friendship means a great deal to you, Let me ask you some questions about this")
        if topic == 3:
            Variables.numberOfChats += 1
        else:
            Variables.numberOfChats = 0
        topic = 3
        Variables.countFriends = -100

         # because the topic is changing we store the emotional level of the current topic
        if topic == 0:
            Variables.emotionJob = Variables.currentEmotion
        elif topic == 1:
            Variables.emotionFamily = Variables.currentEmotion
        elif topic == 2:
            Variables.emotionLove = Variables.currentEmotion
        elif topic == 3:
            Variables.emotionFriend = Variables.currentEmotion
        # current emotion has to be reset to prevent one negative response ruining the entire conversation
        Variables.currentEmotion = Variables.baseline
        return topic

    # Increase the number of chats by one
    Variables.numberOfChats += 1
    # if the emotional level has gone below the baseline or if topic questions below three then return same topic
    if level >= baseline and Variables.numberOfChats < 3:
            return topic
    # else increase the topic by one and change number of topics to zero as its a new topic
    else:
         # because the topic is changing we store the emotional level of the current topic
        if topic == 0:
            Variables.emotionJob = Variables.currentEmotion
        elif topic == 1:
            Variables.emotionFamily = Variables.currentEmotion
        elif topic == 2:
            Variables.emotionLove = Variables.currentEmotion
        elif topic == 3:
            Variables.emotionFriend = Variables.currentEmotion
        # current emotion has o be reset to prevent one negative response ruining the entire conversation
        Variables.currentEmotion = Variables.baseline
        Variables.numberOfChats = 0
        topic += 1
        print(Variables.movingOn.pop())
        return topic

# recursive function that cycles through the topic questions while also appneding key words user has used
def TopicQuestions(topic):

    time.sleep(Variables.topicRND)
    if topic == 0:
        if len(Variables.questionsJob) == 0:
            topic += 1
        else:
            # break user response into a list of words so the keywords can be appended and counts can be incremented
            errorAppend = Variables.questionsJob.pop(Variables.topicIndexJob)
            Variables.questionAnswer = input(errorAppend)
            # error detection
            if (len(Variables.questionAnswer) == 0):
                Variables.questionsJob.insert(0, errorAppend)
                print("You're going to have to answer my question to hear your fortune! So, I will ask again")
                Variables.questionAnswer = "filler"
                TopicQuestions(topic)
            # removes punctuation
            Variables.questionAnswer = ''.join(ch for ch in Variables.questionAnswer if ch not in Variables.exclude)
            Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
            Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
            # checks users statement for key words regarding this topic and appends them to a user list
            # this is used to check if a user has mentioned a topic so Fai can change the level of conversation
            for x in Variables.keywordsJob:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countJob += 1
            for x in Variables.keywordsFamily:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countFamily += 1
            for x in Variables.keywordsLove:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countLove += 1
            for x in Variables.keywordsFriends:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countFriends += 1
            # these loops are used to check for keywords that can be used in the end fortune
            for x in Variables.keywordsJobQ1:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.userKeywordsJobQ1.append(y)
            for x in Variables.keywordsJobQ2:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.userKeywordsJobQ2.append(y)
            User.Analyse(Variables.questionAnswer, Variables.topic)
        # calls this function again with same / updated topic
        TopicQuestions(Variables.topic)
    if topic == 1:
        # if there are no more questions in the list increase topic by one
        if len(Variables.questionsFam) == 0:
            topic += 1
        else:
            # break user response into a list of words so the keywords can be appended and counts can be incremented
            errorAppend = Variables.questionsFam.pop(Variables.topicIndexJob)
            Variables.questionAnswer = input(errorAppend)
            # error detection
            if (len(Variables.questionAnswer) == 0):
                Variables.questionsFam.insert(0, errorAppend)
                print("You're going to have to answer my question to hear your fortune! So, I will ask again")
                Variables.questionAnswer = "filler"
                TopicQuestions(topic)
            # removes punctuation
            Variables.questionAnswer = ''.join(ch for ch in Variables.questionAnswer if ch not in Variables.exclude)
            Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
            Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
            # checks users statement for key words regarding this topic and appends them to a user list
            for x in Variables.keywordsJob:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countJob += 1
            for x in Variables.keywordsFamily:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countFamily += 1
            for x in Variables.keywordsLove:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countLove += 1
            for x in Variables.keywordsFriends:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countFriends += 1
            # these loops are used to check for keywords that can be used in the end fortune
            for x in Variables.keywordsFamilyQ1:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.userKeywordsFamQ1.append(y)
            for x in Variables.keywordsFamilyQ2:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.userKeywordsFamQ2.append(y)
            User.Analyse(Variables.questionAnswer, Variables.topic)
        TopicQuestions(Variables.topic)
    if topic == 2:
        if len(Variables.questionsLove) == 0:
            topic += 1
        else:
            # break user response into a list of words so the keywords can be appended and counts can be incremented
            errorAppend = Variables.questionsLove.pop(Variables.topicIndexJob)
            Variables.questionAnswer = input(errorAppend)
            # error detection
            if (len(Variables.questionAnswer) == 0):
                Variables.questionsLove.insert(0, errorAppend)
                print("You're going to have to answer my question to hear your fortune! So, I will ask again")
                Variables.questionAnswer = "filler"
                TopicQuestions(topic)
            # removes punctuation
            Variables.questionAnswer = ''.join(ch for ch in Variables.questionAnswer if ch not in Variables.exclude)
            Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
            Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
            # checks users statement for key words regarding this topic and appends them to a user list
            for x in Variables.keywordsJob:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countJob += 1
            for x in Variables.keywordsFamily:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countFamily += 1
            for x in Variables.keywordsLove:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countLove += 1
            for x in Variables.keywordsFriends:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countFriends += 1
            # these loops are used to check for keywords that can be used in the end fortune
            for x in Variables.keywordsLoveQ1:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.userKeywordsLoveQ1.append(y)
            for x in Variables.keywordsLoveQ2:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.userKeywordsLoveQ2.append(y)
            User.Analyse(Variables.questionAnswer, Variables.topic)
        TopicQuestions(Variables.topic)
    if topic == 3:
        if len(Variables.questionsFri) == 0:
            topic += 1
        else:
            # break user response into a list of words so the keywords can be appended and counts can be incremented
            errorAppend = Variables.questionsFri.pop(Variables.topicIndexJob)
            Variables.questionAnswer = input(errorAppend)
            # error detection
            if (len(Variables.questionAnswer) == 0):
                Variables.questionsFri.insert(0, errorAppend)
                print("You're going to have to answer my question to hear your fortune! So, I will ask again")
                Variables.questionAnswer = "filler"
                TopicQuestions(topic)
            # removes punctuation
            Variables.questionAnswer = ''.join(ch for ch in Variables.questionAnswer if ch not in Variables.exclude)
            Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
            Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
            # checks users statement for key words regarding this topic and appends them to a user list
            for x in Variables.keywordsJob:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countJob += 1
            for x in Variables.keywordsFamily:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countFamily += 1
            for x in Variables.keywordsLove:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countLove += 1
            for x in Variables.keywordsFriends:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.countFriends += 1
            # these loops are used to check for keywords that can be used in the end fortune
            for x in Variables.keywordsFriendsQ1:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.userKeywordsFriQ1.append(y)
            for x in Variables.keywordsFriendsQ2:
                for y in Variables.questionAnswer:
                    if y == x:
                        Variables.userKeywordsFriQ2.append(y)
            User.Analyse(Variables.questionAnswer, Variables.topic)
        TopicQuestions(Variables.topic)
    if topic >= 4:
            MissedTopics()
# goes through any topic that hasnt been used as a result of keywords changing the conversation
# during this function fai can only collect keywords. She cannot  change topic depending on the key words
def MissedTopics():
    time.sleep(Variables.topicRND)
    if len(Variables.questionsFam) == 3:
       while(len(Variables.questionsFam) > 0):
        Variables.questionAnswer = input(Variables.questionsFam.pop(Variables.topicIndexFam))
        Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
        Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
        # checks users statement for key words regarding this topic and appends them to a user list
        for x in Variables.keywordsJob:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsJob.append(y)
        for x in Variables.keywordsFamily:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFam.append(y)
        for x in Variables.keywordsLove:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsLove.append(y)
        for x in Variables.keywordsFriends:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFri.append(y)
                    Variables.countFriends += 1
        User.Analyse(Variables.questionAnswer, Variables.topic)
    if len(Variables.questionsLove) == 3:
       while(len(Variables.questionsLove) > 0):
        Variables.questionAnswer = input(Variables.questionsLove.pop(Variables.topicIndexLove))
        Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
        Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
        # checks users statement for key words regarding this topic and appends them to a user list
        for x in Variables.keywordsJob:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsJob.append(y)
        for x in Variables.keywordsFamily:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFam.append(y)
        for x in Variables.keywordsLove:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsLove.append(y)
        for x in Variables.keywordsFriends:
            for y in Variables.questionAnswer:
                if y == x:
                    Variables.userKeywordsFri.append(y)
                    Variables.countFriends += 1
        User.Analyse(Variables.questionAnswer, Variables.topic)

def GenerateFortune():
    time.sleep(Variables.fortuneRND)
    if Variables.emotionJob >= Variables.emotionFamily and Variables.emotionJob >= Variables.emotionLove and \
            Variables.emotionJob >= Variables.emotionFriend:
        # if statement used to see if user has used any of the keyword for their fortune
        # if they have not then they will be given an generic keyword
        if len(Variables.userKeywordsJobQ1) > 1:
            q1 = Variables.userKeywordsJobQ1[1]
        else:
            q1 = Variables.userKeywordsJobQ1[0]
        if len(Variables.userKeywordsJobQ2) > 1:
            q2 = Variables.userKeywordsJobQ2[1]
        else:
            q2 = Variables.userKeywordsJobQ2[0]
        print(User.Username(Variables.userName),
              ", from the answers you have given, and the aura I sense from you. I can foresee, "
              "that there is going to be great success within your role as a", q1, ". I am channeling with the "
              "mother of the earth to see further. Hmmm, you might feel ", q2,
              "now but the earth’s spirits "
              "within me are pulsating ... They reveal to me that there is still much of a journey down the path"
              " you have chosen for your career. If you work hard others will see your dedication and you will be "
              "duly rewarded for this in good time.")
    if Variables.emotionFamily > Variables.emotionJob and Variables.emotionFamily > Variables.emotionLove and\
            Variables.emotionFamily > Variables.emotionFriend:
        # if statement used to see if user has used any of the keyword for their fortune
        # if they have not then they will be given an generic keyword
        if len(Variables.userKeywordsFamQ1) > 1:
            q1 = Variables.userKeywordsFamQ1[1]
        else:
            q1 = Variables.userKeywordsFamQ1[0]
        if len(Variables.userKeywordsFamQ2) > 1:
            q2 = Variables.userKeywordsFamQ2[1]
        else:
            q2 = Variables.userKeywordsFamQ2[0]
        print(User.Username(Variables.userName),", from the answers you have given, and the aura I sense from you."
              " I can tell that there"
              " is a deep connection between yourself and your", q1, ". I can see that the time spent with your "
              "family during the ", q2, " has brought you closer together with your family. If you continue to commune "
              "with each other this way I sense great things for you and your loved ones. The strength you have as a "
              "family will only grow stronger")
    if Variables.emotionLove > Variables.emotionJob and Variables.emotionLove > Variables.emotionFamily and \
            Variables.emotionLove > Variables.emotionFriend:
        # if statement used to see if user has used any of the keyword for their fortune
        # if they have not then they will be given an generic keyword
        if len(Variables.userKeywordsLoveQ1) > 1:
            q1 = Variables.userKeywordsLoveQ1[1]
        else:
            q1 = Variables.userKeywordsLoveQ1[0]
        if len(Variables.userKeywordsLoveQ2) > 1:
            q2 = Variables.userKeywordsLoveQ2[1]
        else:
            q2 = Variables.userKeywordsLoveQ2[0]
        print(User.Username(Variables.userName), ", From the answers you have given, and the aura I sense from you."
              "I can foresee"
              " that your heart and"
              " soul is intertwined with another and the relationship between you and your ", q1, " is powerful and the"
              " passion you share for one another is like no other i have ever come across in this world. The month of"
              , q2," is strong for you and is where most of your power as two souls comes from, hold"
              " onto this power and keep it close to you as this will clear obstacles for you in the future and will"
              " only bring you greater happiness.")
    if Variables.emotionFriend > Variables.emotionJob and Variables.emotionFriend > Variables.emotionFamily and\
            Variables.emotionFriend > Variables.emotionLove:
        # if statement used to see if user has used any of the keyword for their fortune
        # if they have not then they will be given an generic keyword
        if len(Variables.userKeywordsFriQ1) > 1:
            q1 = Variables.userKeywordsFriQ1[1]
        else:
            q1 = Variables.userKeywordsFriQ1[0]
        if len(Variables.userKeywordsFriQ2) > 1:
            q2 = Variables.userKeywordsFriQ2[1]
        else:
            q2 = Variables.userKeywordsFriQ2[0]
        print(User.Username(Variables.userName), ", From the answers you have given, and the aura I sense from I can "
              "foresee"
              " a strong powerful"
              "bond between yourself and someone who you may not be of the same blood, but you share the same mind "
              "and spirit with ", q1, ".  The relationship between you and", q1," is strong, and has "
              "lastesd ", q2, " years, this will continue to be reflected within the friendship you two share and holds"
              "true value for you")
