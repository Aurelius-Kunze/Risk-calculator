import random as r
from typing import List

attackers = 0
attackerTurn = 0    # How many attackers attack in this turn
attackRolls = []
attackersLost = 0   # How many defenders were lost this turn
attackWins = 0
attackersRemaining = 0

defenders = 0
defenderTurn = 0    # How many defenders defend in this turn
defenceRolls = []
defendersLost = 0   # How many defenders were lost in this turn
defenceWins = 0
defendersRemaining = 0

victoryChance = 0
expectedAttackersStanding = 0   # Average of attackers left standing at the end of the attack
expectedDefendersStanding = 0   # Average of defenders left standing at the end of the attack

def sort_rolls(rolls):
    for i in range(0, len(rolls)):
        for j in range(0, len(rolls)):
            if rolls[i] > rolls[j]:
                rolls[i], rolls[j] = rolls[j], rolls[i]
    return rolls

attackersConst = int(input("Attackers: "))
defendersConst = int(input("Defenders: "))

for i in range(0, 10000):
    attackers = attackersConst
    defenders = defendersConst
    while attackers > 0 and defenders > 0:

        if attackers > 3:
            attackerTurn = 3
        else:
            attackerTurn = attackers

        if defenders > 3:
            defenderTurn = 3
        else:
            defenderTurn = defenders

        #print(str(attackers) + "v" + str(defenders))
        #print(str(attackerTurn) + "v" + str(defenderTurn))

        for _ in range(0, attackerTurn):
            attackRolls.append(r.randint(1, 6))
        for _ in range(0, defenderTurn):
            defenceRolls.append(r.randint(1, 6))
        attackRolls = sort_rolls(attackRolls)
        defenceRolls = sort_rolls(defenceRolls)
        #print(attackRolls)
        #print(defenceRolls)

        if len(attackRolls) <= len(defenceRolls):
            for j in range(0, len(attackRolls)):
                if attackRolls[j] > defenceRolls[j]:
                    defendersLost += 1
                else:
                    attackersLost += 1
        elif len(attackRolls) > len(defenceRolls):
            for j in range(0, len(defenceRolls)):
                if attackRolls[j] > defenceRolls[j]:
                    defendersLost += 1
                else:
                    attackersLost += 1

        #print("L: " + str(attackersLost) + " " + str(defendersLost))

        attackers -= attackersLost
        attackersLost = 0
        attackRolls = []
        defenders -= defendersLost
        defendersLost = 0
        defenceRolls = []
    if defenders == 0:
        attackWins += 1
        attackersRemaining += attackers
    elif attackers == 0:
        defenceWins += 1
        defendersRemaining += defenders

victoryChance = (attackWins)/(attackWins + defenceWins)
if attackWins != 0:
    expectedAttackersStanding = attackersRemaining/attackWins
else:
    expectedAttackersStanding = 0
if defenceWins != 0:
    expectedDefendersStanding = defendersRemaining/defenceWins
else:
    expectedDefendersStanding = 0
print(str((victoryChance)*100) + "%")
print("Attackers left:" + str(expectedAttackersStanding))
print("Defenders left:" + str(expectedDefendersStanding))

