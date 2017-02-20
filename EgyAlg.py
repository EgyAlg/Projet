from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator.settings import * 
from Toolbox import *
import math


## Ma Strategie d'attaque
class MyAttackStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma Strategie d'attaque")
    def compute_strategy(self,state,id_team,id_player):
        my_state = Toolbox(state, id_team, id_player)
        
        if((my_state.ball_position()-my_state.my_position()).norm>PLAYER_RADIUS+BALL_RADIUS):
            return my_state.aller(my_state.ball_position())    
        return my_state.shoot(my_state.position_but_adv())

## Ma Strategie de defense
class MyDefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma Strategie de defense")
    def compute_strategy(self,state,id_team,id_player):
        my_state = Toolbox(state, id_team, id_player)
        
        if((my_state.ball_position()-my_state.position_mon_but()).norm<GAME_WIDTH/4):
            if((my_state.ball_position()-my_state.my_position()).norm>PLAYER_RADIUS+BALL_RADIUS):   
                return my_state.aller(my_state.ball_position())
            else:
                return my_state.shoot(my_state.position_but_adv())
        else:
            return my_state.get_position_def()
                   

class DribblerStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Ma strategie de dribble")
    def compute_strategy(self, state, id_team, id_player):
        my_state = Toolbox(state, id_team, id_player)
        
        if((my_state.ball_position()-my_state.my_position()).norm>PLAYER_RADIUS+BALL_RADIUS):
            return my_state.aller(my_state.ball_position())
        else:
            if((my_state.ball_position()-my_state.position_but_adv()).norm>GAME_WIDTH/3.5):
                return my_state.mini_shoot(my_state.position_but_adv())
            else:
                return my_state.shoot(my_state.position_but_adv())
    
## Creation d'une equipe
team1 = SoccerTeam(name="EGY",login="")
team2 = SoccerTeam(name="ALG",login="")
team1.add("Salah",DribblerStrategy())
team1.add("Warda",MyDefenseStrategy()) 
team2.add("Mahrez",MyAttackStrategy())
team2.add("Brahimi",MyDefenseStrategy())  