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
        points += 30
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

#CALCULATES MAXIMUM DENOMINATOR FOR EACH LITTLE
def eachDenominator(LittleInput):
    denominator = 0
    if LittleInput == "Love":
        denominator += 40
    elif LittleInput == "Like":
        denominator +=30
    elif LittleInput == "Want to get into":
        denominator +=40
    elif LittleInput == "N/A":
        denominator += 30
    return denominator
    
#ADDS THE DENOMINATOR FOR EACH INTEREST
def TotalDenominator(little):
    totalDenominator = 0
    totalDenominator += eachDenominator(little.sports)
    totalDenominator += eachDenominator(little.hiking)
    totalDenominator += eachDenominator(little.fashion)
    totalDenominator += eachDenominator(little.gaming)
    totalDenominator += eachDenominator(little.singing)
    totalDenominator += eachDenominator(little.dancing)
    totalDenominator += eachDenominator(little.makeup)
    totalDenominator += eachDenominator(little.religion_faith)
    totalDenominator += eachDenominator(little.traveling)
    totalDenominator += eachDenominator(little.thrifting)
    totalDenominator += eachDenominator(little.photography)
    totalDenominator += eachDenominator(little.concerts)
    totalDenominator += eachDenominator(little.leadership)
    totalDenominator += eachDenominator(little.volunteering)
    totalDenominator += eachDenominator(little.staying_at_home)
    totalDenominator += eachDenominator(little.foodie)
    totalDenominator += eachDenominator(little.memes)
    totalDenominator += eachDenominator(little.cooking_baking)
    totalDenominator += eachDenominator(little.family_time)
    totalDenominator += eachDenominator(little.playing_instruments)
    totalDenominator += eachDenominator(little.vlogging_making_videos)
    totalDenominator += eachDenominator(little.working_out)
    return totalDenominator
