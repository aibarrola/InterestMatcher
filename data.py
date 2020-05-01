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

PBig = []
PLittle = [] 

#TAKES EACH VALUE OF THE DICTIONARY AND PUTS IT INTO A LIST
def SeperateObj():
    global PBig
    global PLittle  
    for i in range(len(interests)):                                             #Goes through each dictionary in the list 
        person = User( *([value for key, value in interests[i].items()][1:]))   #Takes each dictionary and takes the value and puts into each object named person
        if person.role == "Big":                                                #Categorize each user into a little or big list
            PBig.append(person)
        elif person.role == "Little":
            PLittle.append(person)
