from spreadsheet import *
from dataclasses import dataclass


@dataclass
class User:
    fname: str
    lname: str
    role: str
    sports: str
    hiking: str
    fashion: str 
    gaming: str
    singing: str
    dancing: str
    makeup: str
    religion_faith: str
    traveling: str
    thrifting: str
    photography: str
    concerts: str
    leadership: str
    volunteering: str
    staying_at_home: str
    foodie: str
    memes: str
    cooking_baking: str 
    family_time: str
    playing_instruments: str
    vlogging_making_videos: str
    working_out: str



#TAKES EACH VALUE OF THE DICTIONARY AND PUTS IT INTO A LIST
PBig = []
PLittle = []   
for i in range(len(interests)):                                             #Goes through each dictionary in the list 
    person = User( *([value for key, value in interests[i].items()][1:]))   #Takes each dictionary and takes the value and puts into each object named person
    if person.role == "Big":                                                #Categorize each user into a little or big list
        PBig.append(person)
    elif person.role == "Little":
        PLittle.append(person)


#FUNCTION TO ADD POINTS BASED ON LITTLE AND BIG INPUT (REFER TO POINT SYSTEM)
def eachScoreCompatibility(littleInput, bigInput):
    points = 0
    if littleInput == "Love" and bigInput == "Love":
        points += 30
    elif littleInput == "Love" and bigInput == "Like":
        points += 20
    elif littleInput == "Love" and bigInput == "Want to get into":
        points += 10
    elif littleInput == "Like" and bigInput == "Love":
        points += 20
    elif littleInput == "Like" and bigInput == "Like":
        points += 20
    elif littleInput == "Like" and bigInput == "Want to get into":
        points += 10
    elif littleInput == "Want to get into" and bigInput == "Love":
        points += 40
    elif littleInput == "Want to get into" and bigInput == "Like":
        points += 30
    elif littleInput == "Want to get into" and bigInput == "Want to get into":
        points += 30
    elif littleInput =="N/A" and bigInput =="N/A":
        points += 30
    elif littleInput =="N/A" and bigInput =="Love":
        points += 2
    elif littleInput =="N/A" and bigInput =="Like":
        points += 4
    elif littleInput =="N/A" and bigInput =="Want to get into":
        points += 8
    return points
   

#TEST eachScoreComptability Function     
#print(eachScoreCompatibility(PLittle[0].sports, PBig[0].sports))
 

#FUNCTION TO FIND COMPATIBILITY SCORE BETWEEN A LITTLE AND BIG
def ScoreCompatibility(little,big):
    totalScore = 0
    totalScore += eachScoreCompatibility(little.sports, big.sports)
    totalScore += eachScoreCompatibility(little.hiking, big.hiking)
    totalScore += eachScoreCompatibility(little.fashion, big.fashion)
    totalScore += eachScoreCompatibility(little.gaming, big.gaming)
    totalScore += eachScoreCompatibility(little.singing, big.singing)
    totalScore += eachScoreCompatibility(little.dancing, big.dancing)
    totalScore += eachScoreCompatibility(little.makeup, big.makeup)
    totalScore += eachScoreCompatibility(little.religion_faith, big.religion_faith)
    totalScore += eachScoreCompatibility(little.traveling, big.traveling)
    totalScore += eachScoreCompatibility(little.thrifting, big.thrifting)
    totalScore += eachScoreCompatibility(little.photography, big.photography)
    totalScore += eachScoreCompatibility(little.concerts, big.concerts)
    totalScore += eachScoreCompatibility(little.leadership, big.leadership)
    totalScore += eachScoreCompatibility(little.volunteering, big.volunteering)
    totalScore += eachScoreCompatibility(little.staying_at_home, big.staying_at_home)
    totalScore += eachScoreCompatibility(little.foodie, big.foodie)
    totalScore += eachScoreCompatibility(little.memes, big.memes)
    totalScore += eachScoreCompatibility(little.cooking_baking, big.cooking_baking)
    totalScore += eachScoreCompatibility(little.family_time, big.family_time)
    totalScore += eachScoreCompatibility(little.playing_instruments, big.playing_instruments)
    totalScore += eachScoreCompatibility(little.vlogging_making_videos, big.vlogging_making_videos)
    totalScore += eachScoreCompatibility(little.working_out, big.working_out)
    return totalScore

#GET PERCENTAGE 
def getPercentage(scoreCompatibility):
    return ("%.2f%%" % (100 * scoreCompatibility/88))


#THE PERFECT COMPATIBILITY PAIR: LITTLE-WANT TO GET INTO, BIG-LOVE
print("Little name is " + PLittle[0].fname + PLittle[0].lname)
print("Big name is " + PBig[0].fname + PBig[0].lname)
print("The Compatibility Score between " + PLittle[0].fname + " and " + PBig[0].fname + "is " + str(ScoreCompatibility(PLittle[0], PBig[0])))
print(getPercentage(ScoreCompatibility(PLittle[0],PBig[0])))
print("-----")


print("Little name is " + PLittle[5].fname + PLittle[5].lname)
print("Big name is " + PBig[2].fname + PBig[2].lname)
print("The Compatibility Score between " + PLittle[5].fname + " and " + PBig[2].fname + " is " + str(ScoreCompatibility(PLittle[5], PBig[2])))
print(getPercentage(ScoreCompatibility(PLittle[5],PBig[2])))
print("-----")


# print(PLittle)
# print()
# print(PBig)
