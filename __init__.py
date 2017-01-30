from soccersimulator import SoccerTeam
from EgyAlg import MyAttackStrategy.MyDefenseStrategy

team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Salah",MyAttackStrategy())
team1.add("Gomaa",MyDefenseStrategy()) 
team2.add("Mahrez",MyAttackStrategy())
team2.add("Mandi",MyDefenseStrategy()) 