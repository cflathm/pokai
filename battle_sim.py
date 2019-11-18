import tensorforce

class battle_sim():
    
    ########################################################################################
    # Intialize the battle simulator                                                       #
    # pokemon_0 -- pokemon on one of the teams                                             #
    # pokemon_1 -- pokemon on the oposite team of pokemon_0                                #
    ########################################################################################
    def __init__(self, pokemon_0, pokemon_1):                                              
        self.pokemon_0 = pokemon_0             
        self.pokemon_1 = pokemon_1
        self.pokemon = [pokemon_0, pokemon_1]
   



    ######################################################################################## 
    # Attack function that processes an attack on a pokemon and returns the value          #
    # move -- the integer value of the moved used, correlated with the move, integer table #
    # attack -- 1/0, the pokemon who is doing the attacking                                #
    #                                                                                      #
    #           / (2xlevel)/5 + 2) * Power * (A/D)      \                                  #
    # Damage = | ----------------------------------- + 2 | * Modifier                      #
    #           \                50                     /                                  #
    ########################################################################################
    def calc_damage(self, move, attacker): 
        A = self.pokemon[attacker] # Get attack stat of attacker 
        D = self.pokemon[not attacker] # Get defenes stat of the attacker 
        level = self.pokemon[attacker] # Get level of the attacker 
        Power = 40 #Get move power
        Modifier = 1 #Calculate modifier based on types 
        
        return ((((2 * level)/5 * Power * (A/D)) / 50) + 2) * Modifier        
    

    ########################################################################################
    # Small simulation used to train the indivdual AI, not used for the entire system      #
    ########################################################################################
    def single_battle():
        print(self.calc_damage(None, 0)
        #if the battle is still going on
        while self.pokemon[0].Hp > 0 and self.pokemon[1].Hp > 0:
            exit()
            #Do attacking 
        
        #Terminal Observe, fight is over 

sim = battle_sim(None, None)
sim.single_battle()
