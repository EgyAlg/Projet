from soccersimulator import SoccerTeam
from EgyAlg import MyDefenseStrategy, MyAttackStrategy, IntelligentStrategy

def get_team(i):
    if (i==1):
        team1 = SoccerTeam(name="EGY",login="")
        team1.add("Salah",MyAttackStrategy())
        return team1
    elif (i==2):
        team2 = SoccerTeam(name="EGYALG",login="")
        team2.add("Mahrez",IntelligentStrategy())
        team2.add("Salah",IntelligentStrategy())
        return team2
    else:    
        team4 = SoccerTeam(name="EGYALG",login="")
        team4.add("Mahrez",IntelligentStrategy())
        team4.add("Salah",MyAttackStrategy())
        team4.add("Brahimi",IntelligentStrategy())
        team4.add("Warda",MyDefenseStrategy())
        return team4