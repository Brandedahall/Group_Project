import Functions
# Index used to track the topic questions
topicIndexJob = len(Functions.t) - 2
topicIndexFam = len(Functions.t) - 8
topicIndexLove = len(Functions.t) - 14
topicIndexFnd = len(Functions.t) - 20

# Username of user
userName = ""
# string used to store users response
Name = ""
# Users real name
TrueName = []
# The user's name is stored here.

questionAnswer = ""
Answer = ""
# The user's answers will be stored here.


# Emotion is the emotional level of the instance
emotion = 0
# baseline is the users base emotional level
baseline = 0
# currentEmotion is used to track the emotional level through out the conversation
currentEmotion = 0
# instance
instanceEmotion = 0
FAIanswer = ""
numberOfChats = 0

word = []
index = 0
# List of keywords user has used
userKeywordsJob = []
userKeywordsFam = []
userKeywordsLove = []
userKeywordsFri = []
# Fais saved keywords
keywordsJob = ["teacher", "tv presenter", "unemployed", "student"]
keywordsFamily = ["mom", "dad", "brother", "sister"]
keywordsLove = ["wife", "husband", "girlfriend", "boyfriend"]
keywordsFriends = ["best friend", "close", "friend", "friends"]
keywordsHobbies = []
keywordsIssues = []
keywordsAchievements = []
# counts used to keep track with the number of keywords in users response. Once used to change
# the conversation the counts are assigned negative numbers to asure they do not trigger again
countJob = 0
countFamily = 0
countLove = 0
countFriends = 0
firstPart = ""
secondPart = ""
thirdPart = ""
fourthPart = ""

tempNextTopic = ""
topic = 0
topics = ["Job", "Family", "Love", "Friends", "Hobbies", "Issues", "Achievements"]

# counts used to compare string and represent index
keyCount = 0
userCount = -1