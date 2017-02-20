from soccersimulator import SoccerTeam
from EgyAlg import DribblerStrategy, MyDefenseStrategy, MyAttackStrategy

def get_team(i):
    if (i==1):
        team1 = SoccerTeam(name="EGY",login="")
        team1.add("Salah",MyAttackStrategy())
        return team1
    elif (i==2):
        team2 = SoccerTeam(name="EGYALG",login="")
        team2.add("Mahrez",DribblerStrategy())
        team2.add("Salah",MyDefenseStrategy())
        return team2
    else:    
        team4 = SoccerTeam(name="EGYALG",login="")
        team4.add("Mahrez",DribblerStrategy())
        team4.add("Salah",MyAttackStrategy())
        team4.add("Brahimi",MyDefenseStrategy())
        team4.add("Warda",MyDefenseStrategy())
        return team4