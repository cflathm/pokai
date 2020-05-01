import math
import pickle 
import random 
pok_dict = pickle.load(open("pokemon_dict.pkl", "rb"))
#random.seed()
class pokemon():
    def __init__(self, seed, pid, moves = None, ev=None, level=5):
        random.seed(seed)
        self.stat_names = ["Health", "Attack", "Defense", "Special", "Speed"]
        self.Pid = pid         
        self.Current_HP = 0
        self.XP = 0 #Get XP
        self.Level = level
        self.Moves = moves if moves else []
        self.Status = None
        self.evasion = 100
        self.Stats = {"Health": 0, "Attack": 0, "Defense": 0, 
                      "Special": 0, "Speed": 0}
        self.Ivs = {"Health": 7, "Attack": 7, "Defense": 7, 
                    "Special": 7, "Speed": 7}
        self.Evs = {"Health": 0, "Attack": 0, "Defense": 0, 
                    "Special": 0, "Speed": 0}
        self.Base = {"Health": 0, "Attack": 0, "Defense": 0, 
                    "Special": 0, "Speed": 0}
        self.Battle_Stats = self.Stats
        
        ###################################
        # Get base Stats 
        ###################################
        poke = pok_dict[pid]
        #print(poke)
        self.Base = {"Health": poke["Health"],
                     "Attack": poke["Attack"],
                     "Defense": poke["Defense"],
                     "Special": poke["Special"],
                     "Speed": poke["Speed"]}


        avail_moves = []
        for key in poke["Learnset_Level"]:
            if (poke["Learnset_Level"][key]["Level"] <= self.Level) and (poke["Learnset_Level"][key]["Power"] > 0):
                avail_moves.append(poke["Learnset_Level"][key])
        for key in poke["Learnset_Machine"]:
            if poke["Learnset_Machine"][key]["Power"] > 0:
                avail_moves.append(poke["Learnset_Machine"][key])
        #print(self.avail_moves) 
        if not self.Moves:
            if len(avail_moves) > 1:
                num = min(random.randint(1,len(avail_moves)), 4)
            else:
                num = len(avail_moves)
            moves = random.sample(avail_moves, num)
            for move in moves:
                move.update({"Current_PP": move["PP"]})
            for move in moves:
                self.Moves.append(move)
            for i in range(num, 4):
                self.Moves.append({})
            #print(self.Moves)
                
        self.set_stats()
        self.Current_HP = self.Stats["Health"]



    ############################################################################
    # Change the stats of the pokemon, used when leveling up or place          #
    #   in a box, probably will never be called with box                       #
    #                                                                          #
    #          /                   / sqrt(EV) \ \                              #
    #       / | (Base + IV) * 2 + | ---------- | | * Level \                   #
    #      |   \                   \     4    / /           |                  #
    # HP = |------------------------------------------------| + Level + 10     #
    #      |                     100                        |                  #
    #       \                                              /                   #
    #                                                                          #
    #             /                   / sqrt(EV) \ \                           #
    #          / | (Base + IV) * 2 + | ---------- | | * Level \                #
    #         |   \                   \     4    / /           |               #
    # Other = |------------------------------------------------| + 10          #
    #         |                     100                        |               #
    #          \                                              /                #
    ############################################################################
    def set_stats(self):
        #Set HP
        Base_HP = self.Base["Health"]
        Health_IV = self.Ivs["Health"]
        Health_EV = self.Evs["Health"]
        Level = self.Level
        Par = ((Base_HP + Health_IV) * 2 + (math.sqrt(Health_EV)/4) * Level)/100
        self.Stats["Health"] = int(Par + Level + 10)

        #Set other stats
        for stat in self.stat_names[1:]:
            Base_S = self.Base[stat]
            Stat_IV = self.Ivs[stat]
            Stat_EV = self.Evs[stat]
            Level = self.Level
            Par = ((Base_S + Stat_IV) * 2 + (math.sqrt(Stat_EV)/4) * Level)/100
            self.Stats[stat] = int(Par + 10)

#pok = pokemon()
#print(pok.Pid)
#print(pok.Base)
#print(pok.Stats)
