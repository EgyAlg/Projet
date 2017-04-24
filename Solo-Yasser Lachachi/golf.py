from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
from Toolbox import *

GOLF = 0.001
SLALOM = 10.


class GolfStrategy(Strategy):
    def __init__(self):
        super(GolfStrategy,self).__init__("Golf")
    def compute_strategy(self,state,id_team,id_player):
        my_state = Toolbox(state, id_team, id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return SoccerAction(my_state.ball_prediction()-my_state.my_position(),\
                    my_state.position_but_adv()-my_state.ball_prediction())
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if(my_state.distanceAuBallon()>PLAYER_RADIUS+BALL_RADIUS):
            return my_state.aller(my_state.ball_prediction())
        else:
            if zone.dedans(state.ball.position):
                return SoccerAction()
            return my_state.mini_shoot(zone.position+Vector2D(zone.l/2.,zone.l/2.))

class SlalomStrategy(Strategy):
    def __init__(self):
        super(SlalomStrategy,self).__init__("Slalom")
    def compute_strategy(self,state,id_team,id_player):
        my_state = Toolbox(state, id_team, id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return SoccerAction(my_state.ball_prediction()-my_state.my_position(),\
                    my_state.position_but_adv()-my_state.ball_prediction())
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """            
        if(my_state.distanceAuBallon()>PLAYER_RADIUS+BALL_RADIUS):
            return my_state.aller(my_state.ball_prediction())
        return my_state.mini_shoot(zone.position+Vector2D(zone.l/2.,zone.l/2.))
            
team1 = SoccerTeam()
team2 = SoccerTeam()
team1.add("John",SlalomStrategy())
team2.add("Wick",SlalomStrategy())
simu = Parcours1(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours2(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours3(team1=team1,vitesse=SLALOM)
show_simu(simu)
simu = Parcours4(team1=team1,team2=team2,vitesse=SLALOM)
show_simu(simu)