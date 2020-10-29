game1   = "Minecraft"
game2   = "Counter Strike: Global Offensive"
game3   = "Monster's Inc. Scream Arena"
game4   = "Legend of Zelda Twilight Princess"
game5   = "Pokemon Emerald"
game6   = "Euro Truck Simulator 2"
game7   = "Star Wars: Battlefront 2 (2005)"
game8   = "Dead Cells"
game9   = "Super Smash Bros. Melee"
game10 = "Spider-Man PS4"
game11 = "Elder Scrolls V Skyrim"
game12 = "Rogue Legacy"
game13 = "Legend of Zelda The Minish Cap"
game14 = "Halo: Reach"
game15 = "The Binding of Isaac: Rebirth"
game16 = "Legend of Zelda Breath of the Wild"
game17 = "PULSAR: Lost Colony"
game18 = "Super Mario Sunshine"
game19 = "Super Mario Party 7"
game20 = "Legend of Zelda Majora's Mask"
game21 = "Legend of Zelda Ocarina of Time"
game22 = "Undertale"
game23 = "Sims 4"
game24 ="League of Legends"
game25 = "Super Smash Bros. Ultimate"

topGames = [game1, #0
                        game2, #1
                        game3, #2
                        game4, #3
                        game5, #4, etc.
                        game6,
                        game7,
                        game8,
                        game9,
                        game10,
                        game11,
                        game12,
                        game13,
                        game14,
                        game15,
                        game16,
                        game17,
                        game18,
                        game19,
                        game20,
                        game21,
                       game22,
                        game23,
                        game24,
                        game25] # length of list -1

if "World of Warcraft" in topGames:
    print("Pass")
else:
    print("Fail")
if topGames[0] != "Legend of Zelda Link to the Past":
    print("Fail")
else:
    print("Pass")

for i in topGames:
    if "Pokemon" in i or "Halo" in i:
        print("Fail")


#print(topGames)

#highScores = [100, 950, 875, 600, 550, 500, 443, 410, 395, 380]
#dogBreeds = ["Poodle", "Collie", "Terrier", "Beagle"]
#ogicalResults = [True, True, False, True]
#myCollection = [1000, 3.1415, "Carrots", False]

#print(str.format("Some weird stuff: {} - What do you think?", myCollection[1]))

#topGames[2] = "something"
#topGames[1] = "something"
#topGames[0] = "something"
#topGames.append("New game")
#CLASSLIST = ("Bob", "Tim", "Frank", "Anthony")
#classList[0] = "george"
#print(classList[0])

#print(len(highScores))

#print(highScores[len(highScores) - 1])
#print(max(highScores))
#print(min(highScores))
#highScores.append(200)
#print(highScores[len(highScores)-1])
#highScores.insert(0,20000)
#print(max(highScores))

#topscore = highScores.pop(0)
#print (topscore)

#print(max(highScores))
