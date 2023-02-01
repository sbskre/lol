import random

print("Welkom in pixel fortnite BETA!")

# create a list of weapons to choose from
weapons = ["pistol", "rifle", "shotgun", "sniper rifle"]

# randomly choose the player's starting weapon
player_weapon = random.choice(weapons)

# initialize the player's health and number of kills
player_health = 100
kills = 0

# game loop
while player_health > 0:
    # show the player their current weapon and health
    print("je hebt een " + player_weapon + " en " + str(player_health) + " levens.")
    
    # get the player's next action
    action = input("wat wil je doen? (vecht, loot) ").lower()
    
    # handle the player's action
    if action == "vecht":
        # choose a random enemy weapon
        enemy_weapon = random.choice(weapons)
        
        # calculate damage based on the player's and enemy's weapons
        if player_weapon == "pistol" and enemy_weapon == "shotgun":
            damage = 40
        elif player_weapon == "shotgun" and enemy_weapon == "sniper rifle":
            damage = 40
        elif player_weapon == enemy_weapon:
            damage = 20
        else:
            damage = 10
        
        # reduce the player's health
        player_health -= damage
        
        # increment the number of kills
        kills += 1
        
        # show the result of the fight
        print("je bent geraakt door een " + enemy_weapon + " voor " + str(damage) + " schade.")
    elif action == "loot":
        # randomly choose a new weapon
        player_weapon = random.choice(weapons)
        
        # show the result of the looting
        print("je vond een " + player_weapon + ".")
    else:
        print("Invalid action.")
    
    # check if the player has won the game
    if kills >= 10:
        print("Congratulations! je hebt gewonnen met " + str(player_health) + " levens en " + str(kills) + " kills.")
        break

# show the game over message
if player_health <= 0:
    print("Game Over. je bent geëindigd met " + str(kills) + " kills.")
