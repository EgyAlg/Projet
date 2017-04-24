from soccersimulator import SoccerTeam
from golf import GolfStrategy, SlalomStrategy

def get_golf_team():
        team1 = SoccerTeam(name="USA",login="")
        team1.add("Woods",GolfStrategy())
        return team1
def get_slalom_team1():
        team1 = SoccerTeam(name="USA",login="")
        team1.add("Woods",SlalomStrategy())
        return team1
def get_slalom_team2():        
        team2 = SoccerTeam(name="ETU",login="")
        team2.add("Yass",SlalomStrategy())
        team2.add("Saitama",SlalomStrategy())
        return team2
