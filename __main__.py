from operator import itemgetter
from fractions import Fraction
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
                    timetxt += "Days: {}, ".format(times)
                elif x == 1:
                    timetxt += "Hours: {}, ".format(times)
                elif x == 2:
                    timetxt += "Minutes: {}, ".format(times)
                else:
                    timetxt += "Seconds: {}".format(times)
                Timefound = True
            x += 1
        if not Timefound:
            return "Null"
        return timetxt
    @staticmethod
    def timeformat(time):
        if time[3] >= 60:
            time[2] += int(time[3]/60)
            time[3] %= 60
        if time[2] >= 60:
            time[1] += int(time[2]/60)
            time[2] %= 60
        if time[1] >= 24:
            time[0] += int(time[1]/24)
            time[1] %= 24
        return time

    def MaxTownHall(self,TownHallLvL):
        totaltime = [0,0,0,0]
        LaboratoryLvL = 0
        buildings2 = []
        with open("Data/buildingupgrades.txt", "r") as buildingsfile:
            for line in buildingsfile:
                line = line.strip()
                name,upgrades,numberaval,times = line.split("|")
                x = 0
                while x != int(upgrades.split(",")[TownHallLvL-1]):
                    time = times.split("/")[x].split(",")
                    y = 0
                    while y != 4:
                        totaltime[y] += int(time[y])*int(numberaval.split(",")[TownHallLvL-1])
                        y += 1
                    x += 1
                if numberaval.split(",")[TownHallLvL-1] != '0':
                    buildings2.append([name,int(upgrades.split(",")[TownHallLvL-1]),
                                       int(numberaval.split(",")[TownHallLvL-1])])
                if name == "Laboratory":
                    LaboratoryLvL = int(upgrades.split(',')[TownHallLvL-1])
        buildings2.sort(key=itemgetter(0))
        army = []
        with open("Data/armyupgrades.txt", "r") as armyfile:
            for line in armyfile:
                line = line.strip()
                name,threqir,labreqir,times = line.split("|")
                labreqir = [int(labreq) for labreq in labreqir.split(",")]
                if TownHallLvL >= int(threqir):
                    x = 0
                    while x != len(labreqir):
                        if labreqir[x] > LaboratoryLvL:
                            break
                        x += 1
                    army.append([name,x])
        return [buildings2,army,self.timeformat(totaltime)]

    def PercentageTH(self,TownHallLvL,mode='lvl'):
        if mode == 'lvl':
            Buildings2 = self.MaxTownHall(TownHallLvL)[0]
            Buildings = self.buildings
            x = 0
            avoidy = []
            overallpercentagelst = []
            for building2 in Buildings2:
                y = 0
                BuildingFound = False
                for building in Buildings:
                    if building[0] == building2[0] and [avoid for avoid in avoidy if avoid == y] == []:
                        overallpercentagelst.append((building[1]/building2[1]+building[2]/building2[2])/2)
                        avoidy.append(y)
                        BuildingFound = True
                    y += 1
                if not BuildingFound:
                    x = 0
                    while x != building2[2]:
                        overallpercentagelst.append(0)
                        x += 1
                x += 1
            Army2 = self.MaxTownHall(TownHallLvL)[1]
            Army = self.troops
            x = 0
            avoidy = []
            for troop2 in Army2:
                y = 0
                TroopFound = False
                for troop in Army:
                    if troop[0] == troop2[0] and [avoid for avoid in avoidy if avoid == y] == []:
                        overallpercentagelst.append(troop[1]/troop2[1])
                        avoidy.append(y)
                        TroopFound = True
                    y += 1
                if not TroopFound:
                    overallpercentagelst.append(0)
                x += 1
            overallpercentage = 0
            for percentage in overallpercentagelst:
                overallpercentage += percentage
            overallpercentage /= len(overallpercentagelst)
            return Fraction(overallpercentage).limit_denominator()





demo = Base([['Air Bomb', 5, 6],
  ['Air Defense', 10, 4],
  ['Air Sweeper', 7, 2],
  ['Archer Queen', 60, 1],
  ['Archer Tower', 16, 8],
  ['Army Camp', 10, 4],
  ['Barbarian King', 60, 1],
  ['Barracks', 13, 4],
  ['Bomb', 7, 6],
  ['Bomb Tower', 7, 2],
  ['Cannon', 16, 7],
  ['Clan Castle', 8, 1],
  ['Dark Barracks', 7, 2],
  ['Dark Elixir Drill', 6, 3],
  ['Dark Elixir Storage', 7, 1],
  ['Dark Spell Factory', 4, 1],
  ['Eagle Artillery', 3, 1],
  ['Elixir Collector', 12, 7],
  ['Elixir Storage', 13, 4],
  ['Giant Bomb', 5, 6],
  ['Giga Tesla', 5, 1],
  ['Gold Mine', 12, 7],
  ['Gold Storage', 13, 4],
  ['Grand Warden', 30, 1],
  ['Hidden Tesla', 10, 5],
  ['Inferno Tower', 6, 2],
  ['Laboratory', 10, 1],
  ['Mortar', 11, 4],
  ['Seeking Air Mine', 3, 6],
  ['Skeleton Trap', 4, 3],
  ['Spell Factory', 5, 1],
  ['Spring Trap', 5, 8],
  ['Wall', 13, 300],
  ['Wizard Tower', 11, 5],
  ['Workshop', 2, 1],
  ['X-Bow', 6, 4]],
  [['Barbarian', 8],
 ['Archer', 8],
 ['Giant', 9],
 ['Goblin', 7],
 ['Wall Breaker', 8],
 ['Ballon', 8],
 ['Wizard', 9],
 ['Healer', 5],
 ['Dragon', 7],
 ['Pekka', 7],
 ['Baby Dragon', 6],
 ['Miner', 6],
 ['Electro Dragon', 3],
 ['Minion', 8],
 ['Hog Rider', 8],
 ['Valkyrie', 7],
 ['Golem', 8],
 ['Witch', 4],
 ['Lava Hound', 5],
 ['Bowler', 4],
 ['Lightning Spell', 7],
 ['Healing Spell', 7],
 ['Rage Spell', 5],
 ['Jump Spell', 3],
 ['Freeze Spell', 7],
 ['Clone Spell', 5],
 ['Poison Spell', 5],
 ['Earthquake Spell', 4],
 ['Haste Spell', 4],
 ['Skeleton Spell', 5],
 ['Wall Wrecker', 3],
 ['Battle Blimp', 3]],2)
pprint.pprint(demo.PercentageTH(12))
