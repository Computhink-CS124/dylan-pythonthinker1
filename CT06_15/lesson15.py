planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]
print(planets[2])
planets.append ["uranus"]
planets[3] = "muskworld"
del(planets[6])
length = len(planets)
counter = 0
for i in range (length):
    print (planets[counter])