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
    
#POSITIONS
    
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
    
    def my_positionX(self):
        return self.state.player_state(self.key[0],self.key[1]).position.x
    
    def my_positionY(self):
        return self.state.player_state(self.key[0],self.key[1]).position.y    
        
    def position_player1(self):
         return self.state.player_state(self.id_team,0).position
         
    def position_player2(self):
         return self.state.player_state(self.id_team,1).position     
        
    def ball_position(self):
        return self.state.ball.position
        
    def ball_positionX(self):
        return self.state.ball.position.x

    def ball_positionY(self):
        return self.state.ball.position.y        
        
    def fonceur(self,me):
        return me.aller(me.ball_position())+me.shoot(me.position_but_adv())
        
    def position_but_adv(self):
        if (self.id_team == 1):
            return Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
        else :
            return Vector2D(0,GAME_HEIGHT/2)
    
    def getX_position_but_adv(self):
        if (self.id_team == 1):
            return GAME_WIDTH
        else :
            return 0
        
    def position_mon_but(self):
        if (self.id_team == 1):
            return Vector2D(0,GAME_HEIGHT/2)
        else :
            return Vector2D(GAME_WIDTH,GAME_HEIGHT/2) 
            
    def distanceAuButAdv(self):
        return (self.ball_position()-self.position_but_adv()).norm
    
    def distanceAuBallon(self):
        return (self.ball_position()-self.my_position()).norm
  
#DEPLACEMENTS

    def ball_vitesse(self):
        return self.state.ball.vitesse 
        
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())  
        
    def get_position_def(self):
        if (self.id_team == 1):
            return self.aller(Vector2D(7,GAME_HEIGHT/2))
        else :
             return self.aller(Vector2D(GAME_WIDTH-7,GAME_HEIGHT/2))    

#ACTIONS

    def shoot(self,p):
        return SoccerAction(Vector2D(), p-self.my_position())
        
    def mini_shoot(self, p):
        return SoccerAction(Vector2D(),(p-self.my_position())*0.015)    

    def passe(self):
        if (self.id_player == 0):
            return SoccerAction(Vector2D(),(self.position_player2()-self.my_position())*0.115) 
        else :
            return SoccerAction(Vector2D(),(self.position_player1()-self.my_position())*0.115) 
            
    def laisse(self):
        if (self.id_player == 0):
            if(self.distanceAuBallon()>(self.ball_position()-self.position_player2()).norm):
                return self.trace()
            else :
                return self.aller(self.ball_position())
        else:
            if(self.distanceAuBallon()>(self.ball_position()-self.position_player1()).norm):
                return self.trace()
            else :
                return self.aller(self.ball_position())
            
    def trace(self):
        if (self.id_team == 1):
            return self.aller(Vector2D(self.ball_positionX()+10,self.my_positionY()))
        else:
            return self.aller(Vector2D(self.ball_positionX()-10,self.my_positionY()))                            