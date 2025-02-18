triplets = [ ]
for x in range(1, 100):
    for y in range(x + 1, 100):
        for z in range(y + 1, 100):
            if x ** 2 + y ** 2 == z ** 2:
                triplets.append((x, y, z))
print(triplets)
triplets.clear()
triplets=[(x,y,z) for x in range(1,100) for y in range(1,100) for z in range(1,100) if x**2+y**2==z**2]
print(triplets)