from soccersimulator import SoccerTeam
from EgyAlg import team1, team2

def get_team(i):
    s = SoccerTeam(name="EGY")
    if (i==1):
        s.add("Salah",MyAttackStrategy())
    if (i==2):
        s.add("Salah",MyAttackStrategy())
        s.add("Warda",MyDefenseStrategy())
    if (i==4):    
        s.add("Salah",MyAttackStrategy())
        s.add("Warda",MyDefenseStrategy())
        s.add("EGY",MyAttackStrategy())
        s.add("EGY",MyAttackStrategy())
        