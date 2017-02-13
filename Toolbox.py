from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator.settings import * 
from Toolbox import *
import math

class Toolbox(object):
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        self.key = (id_team, id_player)
        
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
        
    def ball_position(self):
        return self.state.ball.position
        
    def ball_vitesse(self):
        return self.state.ball.vitesse 
        
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())
        
    def shoot(self,p):
        return SoccerAction(Vector2D(), p-self.my_position())
        
    def fonceur(self,me):
        return me.aller(me.ball_position)+me.shoot(me.but_adv)
        
    def position_but_adv(self):
        if (self.id_team == 1):
            return Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
        else :
            return Vector2D(0,GAME_HEIGHT/2)
    def position_mon_but(self):
        if (self.id_team == 1):
            return Vector2D(0,GAME_HEIGHT/2)
        else :
            return Vector2D(GAME_WIDTH,GAME_HEIGHT/2)    
    
    def get_pos_def(self):
        if (self.id_team == 1):
            return Vector2D(5,GAME_HEIGHT/2)
        else :
            return Vector2D(GAME_WIDTH-5,GAME_HEIGHT/2) 
            
    def mini_shoot(self, p):
        return SoccerAction(Vector2D(),(p-self.my_position())*0.015)