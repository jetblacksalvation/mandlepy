import pygame

pygame.init()

z = 0 +0j

def man_val(com : complex(), zat: complex):
    com = com**2 +zat
    return com
color =0 

if "__main__":
    
    screen = pygame.display.set_mode((800,800))
    pass
    while 1:
        
        for x in range(800):
            for y in range(800):
                for f in range(255):
                    
                    z = man_val(z, complex(x/800,y/800))
                else:
                    color = f
                screen.set_at((y,x), (color, color, color))
                color = 0
                pygame.display.flip()
    