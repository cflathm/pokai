import math

class pokemon(object):
    def __init__(self, pid, moves=[], ev=[], level=5):
        
        self.stat_names = ["Health", "Attack", "Defense", "Special", "Speed"]
        self.Pid = pid         
        self.Current_HP = 0
        self.XP = 0 #Get XP
        self.Level = level
        self.moves = moves
        self.Stats = {"Health": 0, "Attack": 0, "Defense": 0, 
                      "Special": 0, "Speed": 0}
        self.Ivs = {"Health": 7, "Attack": 7, "Defense": 7, 
                    "Special": 7, "Speed": 7}
        self.Evs = {"Health": 0, "Attack": 0, "Defense": 0, 
                    "Special": 0, "Speed": 0}
        self.Base = {"Health": 0, "Attack": 0, "Defense": 0, 
                    "Special": 0, "Speed": 0}

        ###################################
        # Get base Stats 
        ###################################

        ###################################
        # Define Moves
        #if not Moves:
            # Generate rendom Moves 
        #else:
        #    self.Moves = moves
        ###################################        

        ###################################
        # Define Evs
        #if not Ev:
            # Generate random Evs 
        #else:
        #    self.Ev = ev
        ###################################
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
        Par = ((Base_HP + Health_IV) + (math.sqrt(Health_EV)/4) * Level)/100
        self.Stats["Health"] = Par + Level + 10

        #Set other stats
        for stat in self.stat_names[1:]:
            Base_S = self.Base[stat]
            Stat_IV = self.Ivs[stat]
            Stat_EV = self.Evs[stat]
            Level = self.Level
            Par = ((Base_S + Stat_IV) + (math.sqrt(Stat_EV)/4) * Level)/100
            self.Stats[stat] = Par + 10
