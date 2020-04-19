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



#for row in range(1,23):
#     Big_Angelo_Ibarrola = User(sheet.cell(2,row).value)

# Big_Angelo_Ibarrola = User('Angelo')
# People = [None for __ in range(9)]
# for y in range(len(People)):
# 	People[y] = User( *[sheet.cell(y+2,x).value for x in range(2,27)] )




#TAKES EACH VALUE OF THE DICTIONARY AND PUTS IT INTO A LIST
PBig = []
PLittle = []   
for i in range(len(interests)): 
    person = User( *([value for key, value in interests[i].items()][1:]))
    if person.role == "Big":
        PBig.append(person)
    elif person.role == "Little":
        PLittle.append(person)


#FUNCTION TO ADD POINTS BASED ON LITTLE AND BIG INPUT (REFER TO POINT SYSTEM)
def eachScoreCompatibility(littleInput, bigInput):
    points = 0
    if littleInput == "Love" and bigInput == "Love":
        points += 3
    elif littleInput == "Love" and bigInput == "Like":
        points += 2
    elif littleInput == "Love" and bigInput == "Want to get into":
        points += 1
    elif littleInput == "Like" and bigInput == "Love":
        points += 2
    elif littleInput == "Like" and bigInput == "Like":
        points += 2
    elif littleInput == "Like" and bigInput == "Want to get into":
        points += 1
    elif littleInput == "Want to get into" and bigInput == "Love":
        points += 4
    elif littleInput == "Want to get into" and bigInput == "Like":
        points += 3
    elif littleInput == "Want to get into" and bigInput == "Want to get into":
        points += 3
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




print("Little name is " + PLittle[0].fname)
print("-----")
print("Big name is " + PBig[0].fname)
print("-----")
print("The Compatibility Score between " + PLittle[0].fname + " and " + PBig[0].fname + " is " + str(ScoreCompatibility(PLittle[0], PBig[0])))
    


# print(PLittle)
# print()
# print(PBig)
