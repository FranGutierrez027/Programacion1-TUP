def resolver_laberinto(laberinto, x, y, camino):
    if x < 0 or y < 0 or x >= len(laberinto) or y >= len(laberinto[0]) or laberinto [x][y] == 1:
        return False
    
    camino.append((x,y))

    if x == len(laberinto) -1 and y == len(laberinto[0]) - 1:
        return True
    
    laberinto[x][y] = 1

    if (resolver_laberinto(laberinto, x + 1, y ,camino)or
        resolver_laberinto(laberinto, x,y + 1,camino)or
        resolver_laberinto(laberinto,x - 1,y,camino)or
        resolver_laberinto(laberinto,x,y-1,camino)):
        return True
    
    camino.pop()
    laberinto[x][y] = 0
    return False
