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
        
        v_cage2=Vector2D(GAME_WIDTH,GAME_GOAL_HEIGHT/2)
        v_cage1=Vector2D(0,GAME_GOAL_HEIGHT/2)
        
        if(id_team == 1):
            if((my_state.ball_position()-my_state.my_position()).norm>PLAYER_RADIUS+BALL_RADIUS):
                return my_state.aller(my_state.ball_position())
            return my_state.shoot(v_cage2)
        else: 
            if((my_state.ball_position()-my_state.my_position()).norm>PLAYER_RADIUS+BALL_RADIUS):
                return my_state.aller(my_state.ball_position())
            return my_state.shoot(v_cage1)

## Ma Strategie de defense
class MyDefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma Strategie de defense")
    def compute_strategy(self,state,id_team,id_player):
        my_state = Toolbox(state, id_team, id_player)
        
        v_cage2=Vector2D(GAME_WIDTH,GAME_GOAL_HEIGHT/2)
        v_cage1=Vector2D(0,GAME_GOAL_HEIGHT/2)
        
        if(id_team == 1):
            if((my_state.ball_position()-v_cage1).norm<=30):
                return my_state.aller(my_state.ball_position())
            return my_state.shoot(v_cage2)
        else: 
            if((my_state.ball_position()-v_cage2).norm<=30):
                return my_state.aller(my_state.ball_position())
            return my_state.shoot(v_cage1)            

## Creation d'une equipe
team1 = SoccerTeam(name="EGY",login="")
team2 = SoccerTeam(name="ALG",login="")
team1.add("Salah",MyAttackStrategy())
team1.add("Warda",MyDefenseStrategy()) 
team2.add("Mahrez",MyAttackStrategy())
team2.add("Brahimi",MyDefenseStrategy()) 

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()