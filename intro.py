import pygame as pg
import numpy as np

def fill_alternate_zeros(array:np.ndarray)->None:
    array.fill(0)
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                boxes[i,j]=1;


def make_grid(screen:pg.surface.Surface,rows:int,columns:int,X:int,Y:int)->None:
    for i in range(0,X,columns):
        pg.draw.line(screen,"white",((columns+i),0),(columns+i,X))
    for j in range(0,Y,rows):
        pg.draw.line(screen,"white",(0,rows+j),(Y,rows+j))


a,b = pg.init()
# print(a,b)
X,Y = 720, 720 #resolution
(L,B) = 16,16 #grid_size


boxes = np.empty((L,B))
print(type(boxes))
columns,rows = int( X/L), int(Y/B)
print(columns,rows)

fill_alternate_zeros(boxes)

# print(boxes)
screen = pg.display.set_mode((X,Y))
print(type(screen))
clock =pg.time.Clock();
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 

    screen.fill("black")
    make_grid(screen,rows,columns,X,Y)


    

    pg.display.flip()
    clock.tick(60)
pg.quit()
print(type(screen))


