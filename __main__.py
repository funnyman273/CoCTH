from operator import itemgetter
import pprint


class Base(object):

    def __init__(self,buildings,troopslvls,townhalllvl):
        self.buildings = buildings
        self.troops = troopslvls
        self.thlvl = townhalllvl

    @staticmethod
    def timetext(time):
        timetxt = ''
        x = 0
        Timefound = False
        for times in time:
            if times != "0":
                if x == 0:
                    timetxt += "Days: {},".format(times)
                elif x == 1:
                    timetxt += "Hours: {},".format(times)
                elif x == 2:
                    timetxt += "Minutes: {},".format(times)
                else:
                    timetxt += "Seconds: {}".format(times)
                Timefound = True
            x += 1
        if not Timefound:
            return "Null"
        return timetxt

    @staticmethod
    def MaxTownHall(TownHallLvL):
        buildings2 = []
        with open("Data/buildingupgrades.txt", "r") as buildingsfile:
            for line in buildingsfile:
                line = line.strip()
                name,upgrades,numberaval,times = line.split("|")
                if numberaval.split(",")[TownHallLvL-1] != '0':
                    buildings2.append([name,upgrades.split(",")[TownHallLvL-1],
                                       numberaval.split(",")[TownHallLvL-1]])
        buildings2.sort(key=itemgetter(0))
        return [buildings2,0]

    @staticmethod
    def PercentageTH(Buildings,Troops,TownHallLvl):
        Buildings2 = self.MaxTownHall(TownHallLvL)[0]
        x = 0
        avoidy = []
        overallpercentage = 0
        for building2 in Buildings2:
            y = 0
            for building in Buildings:
                if building[0] == building2[0] and [avoid for avoid in avoidy if avoid == y] == []:
                    avoidy.append(y)
                    building2[]
                    break
                y += 1
            x += 1


demo = Base(1,1,2)
pprint.pprint(demo.MaxTownHall(6))
