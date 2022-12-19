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