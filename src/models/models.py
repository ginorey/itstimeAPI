from json import JSONEncoder


class Fighter:
        def __init__(self, id, name, record, nickname, height, weight, reach,
                stance, dateOfBirth, significantStrikesLandedPerMinute, 
                significantStrikingAccuracy, significantStrikesAbsorbedPerMinute,
                significantStrikeDefence, averageTakedownsLandedPer15Minutes,
                takedownAccuracy, takedownDefense, averageSubmissionsAttemptedPer15Minutes, fights):
                self.id       = id
                self.name     = name
                self.record   = record
                self.nickname = nickname
                self.height   = height
                self.weight   = weight
                self.reach    = reach
                self.stance   = stance
                self.dateOfBirth = dateOfBirth
                self.significantStrikesLandedPerMinute = significantStrikesLandedPerMinute
                self.significantStrikingAccuracy = significantStrikingAccuracy
                self.significantStrikesAbsorbedPerMinute = significantStrikesAbsorbedPerMinute
                self.significantStrikeDefence = significantStrikeDefence
                self.averageTakedownsLandedPer15Minutes = averageTakedownsLandedPer15Minutes
                self.takedownAccuracy = takedownAccuracy
                self.takedownDefense = takedownDefense
                self.averageSubmissionsAttemptedPer15Minutes = averageSubmissionsAttemptedPer15Minutes
                self.fights = fights
        def __repr__(self):
                return "id: " + str(self.id), "name: " + str(self.name), "record: " + str(self.record), "nickname: " + str(self.nickname)

class Event:
        def __init__(self, id, res, fighter1, fighter2, fighter1KD, fighter2KD, fighter1STR, fighter2STR, 
                fighter1TD, fighter2TD, fighter1SUB, fighter2SUB, event, date, method, round, time):
                self.id = id 
                self.res = res 
                self.fighter1 = fighter1 
                self.fighter2 = fighter2 
                self.fighter1KD = fighter1KD 
                self.fighter2KD = fighter2KD 
                self.fighter1STR = fighter1STR 
                self.fighter2STR = fighter2STR 
                self.fighter1TD = fighter1TD 
                self.fighter2TD = fighter2TD 
                self.fighter1SUB = fighter1SUB 
                self.fighter2SUB = fighter2SUB 
                self.event = event 
                self.date = date 
                self.method = method 
                self.round = round 
                self.time = time
        def __repr__(self):
                return "id: " + str(self.id), "fighter1: " + str(self.fighter1), "fighter2: " + str(self.fighter2)

class FighterJSONENCODER(JSONEncoder):
        def default(self, obj):
                return obj.__dict__ 








