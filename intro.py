import pygame as pg
import numpy as np
import  logic
import time



def make_grid(screen:pg.surface.Surface,rows:int,columns:int,X:int,Y:int)->None:
    for i in range(0,X,columns):
        pg.draw.line(screen,"gray",((columns+i),0),(columns+i,X))
    for j in range(0,Y,rows):
        pg.draw.line(screen,"gray",(0,rows+j),(Y,rows+j))


def paint_cells(screen:pg.surface.Surface,width:int,height:int,np_array:np.ndarray):
    length_x,length_y = np_array.shape
    for i in range(length_x):
        for j in range(length_y):
            if np_array[i,j] ==1:
                    pg.draw.rect(screen,"beige",(i*width,j*height,width,height))





a,b = pg.init()
# print(a,b)
X,Y = 720, 720 #resolution
(L,B) = 16,16 #grid_size


boxes = np.random.randint(0,2,(L,B))
columns,rows = int( X/L), int(Y/B)


# print(boxes)
screen = pg.display.set_mode((X,Y))
clock =pg.time.Clock();
running = True


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 

    screen.fill("black")



    make_grid(screen,rows,columns,X,Y)
    paint_cells(screen,rows,columns,boxes)
    make_grid(screen,rows,columns,X,Y)
    boxes=logic.life(boxes).copy()
    time.sleep(1)

    

    pg.display.flip()
    clock.tick(60)
pg.quit()


