from soccersimulator import SoccerTeam
from EgyAlg import team1, team2
from EgyAlg import MyAttackStrategy, MyDefenseStrategy

def get_team(i):
    s = SoccerTeam(name="EGYALG")
    if (i==1):
        s.add("Mahrez",MyAttackStrategy())
    if (i==2):
        s.add("Mahrez",MyAttackStrategy())
        s.add("Salah",MyDefenseStrategy())
    if (i==4):    
        s.add("Mahrez",MyAttackStrategy())
        s.add("Salah",MyDefenseStrategy())
        s.add("Brahimi",MyAttackStrategy())
        s.add("Warda",MyAttackStrategy())
        