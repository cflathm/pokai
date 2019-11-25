#import tensorforce
import random
from pokemon import pokemon

class battle_sim():
    
    ############################################################################
    # Intialize the battle simulator                                           #
    # pokemon_0 -- pokemon on one of the teams                                 #
    # pokemon_1 -- pokemon on the oposite team of pokemon_0                    #
    ############################################################################
    #def __init__(self, pokemon_0, pokemon_1):                                              
        
        



    ############################################################################ 
    # Attack function that processes an attack on a pokemon and                #
    #   returns the value                                                      #
    # move -- the integer value of the moved used,                             #
    #   correlated with the move, integer table                                #
    # attack -- 1/0, the pokemon who is doing the attacking                    #
    #                                                                          #
    #           / (2xlevel)/5 + 2) * Power * (A/D)      \                      #
    # Damage = | ----------------------------------- + 2 | * Modifier          #
    #           \                50                     /                      #
    ############################################################################
    def calc_damage(self, move, attacker, defender): 
        A = attacker.Stats["Attack"] # Get attack stat of attacker 
        D = defender.Stats["Defense"] # Get defenes stat of the attacker 
        level = attacker.Level # Get level of the attacker 
        Power = int(move["Power"]) #Get move power
        Modifier = 1 #Calculate modifier based on types 
        
        left = ((((2 * level)/5 * Power * (A/D)) / 50) + 2) 
        r = left * Modifier
        return int(r)
    

    ############################################################################
    # Small simulation used to train the indivdual AI on a single turn,        #
    #   not used for the entire system, on the fight ai                        #
    ############################################################################
    def single_turn(self, pokemon_1, pokemon_2, move_1, move_2): 
        if pokemon_1.Stats["Speed"] > pokemon_2.Stats["Speed"]:
            First = 0
        elif pokemon_2.Stats["Speed"] > pokemon_1.Stats["Speed"]:
            First = 1
        else:
            First = random.randint(0,1)
        poks = [pokemon_1, pokemon_2]
        moves = [move_1, move_2]

        for i in range(2):
            attacker = poks[(First+i)%2]
            defender = poks[(First+1+i)%2]
            move = moves[(First+i)%2]
            move["Current_PP"] -= 1
            
            #Confusion Check

            #Sleep check 

            #calculate miss


            #calculate damage
            if move["Power"] != 0:
                damage = self.calc_damage(move, attacker, defender)
                defender.Battle_Stats["Health"] -= damage
            
            #Effects 

            #Status stuff 

            if defender.Battle_Stats["Health"] <= 0:
                return (First+1+i)%2

            #Poison/Burn

        return -1

random.seed()
sim = battle_sim()
p1 = pokemon(random.randint(0, 1000000), random.randint(1,151))
p2 = pokemon(random.randint(0, 1000000), random.randint(1,151))
m1 = p1.Moves[0]
m2 = p2.Moves[0]

print(p1.Battle_Stats)
print(p2.Battle_Stats)
print(m1)
print(m2)

sim.single_turn(p1, p2, m1, m2)

print(p1.Battle_Stats)
print(p2.Battle_Stats)

