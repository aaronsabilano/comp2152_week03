import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons Array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']


print("Available Weapons:", ', '.join(weapons))

# Inputs combat strength hero
combatStrength = int(input("Enter your combat strength (1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input! Combat Strength should be between 1 and 6.")
    combatStrength = 1 #Default value for invalid input

combatStrength = max(1, min(6, int(input("Hero strength (1-6): "))))

# Input combat strength for monster
mCombatStrength = int (input("Enter monster's combat stength (1-6)"))
if mCombatStrength < 1 or mCombatStrength >6:
    print("invalid input! Monster combat strength should be between 1 and 6.")
    mCombatStrength = 1 #Default value for inlavid input

#simulate battle rounds
for j in range(1,21,2): #simulation of 20 rounds, stepping by 2 
    #dice rolls for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    #Calculate the Weapons
    heroWeapon = weapons[heroRoll-1]
    monsterWeapon = weapons[monsterRoll-1]
    
    #Calculate total stength 
    heroTotal = combatStrength + heroRoll
    monsterTotal = combatStrength + monsterRoll

    # Print round details
    print(f"\nRound {j} Hero rolled {heroRoll}, Monster Rolled {monsterRoll}")
    print(f"Hero Selected: {heroWeapon}, Monster Selected {monsterWeapon}")
    print(f"Hero total Strength: {heroTotal} Monster total Strength: {monsterTotal}")

    #Determine Winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round!")
    else:
        print("It's a tie!")
    
    if j==11:
        print("\n Battle Truce declared in Round 11. Game over!")
        break

    if j != 11: 
        print  ("\n Battle concluded after 20 rounds!")
