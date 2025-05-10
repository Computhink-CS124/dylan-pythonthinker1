planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus" ]
print(planets[2])
planets.append ("neptune")
planets[3] = "muskworld"
planets.pop(6)
length = len(planets)
counter = 0
for i in range (length):
    print (planets[counter])
    counter = counter + 1