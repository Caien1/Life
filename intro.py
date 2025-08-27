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


def display_paused_helper(text,y_incr,screen)->None:
    font = pg.font.Font(None,40)
    text = font.render(text,True,(10,255,10))
    text_position = text.get_rect(centerx=screen.get_width() / 2 + 20, y=screen.get_width()/2+y_incr)
    screen.blit(text,text_position )
    

def display_paused(screen):
    bg_color = pg.Color(51,51,51,200)
    screen.fill(bg_color);
    font = pg.font.Font(None,64)
    color = pg.Color(255,255,255)
    text =font.render("PAUSED",True, color)
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=screen.get_width()/2-110)
    screen.blit(text, textpos)
    screen.blit(screen, (0, 0))
    display_paused_helper("Press P to Start and Stop",0,screen=screen)

    display_paused_helper("Press R to reset",40,screen=screen)
    display_paused_helper("Press E to toggle edit mode",80,screen)
    
    
 
    screen.blit(screen, (0, 0))
    pg.display.flip()



   
   

    



a,b = pg.init()
# print(a,b)
X,Y = 1080, 1080 #resolution
(L,B) = 32,32 #grid_size


boxes = np.random.randint(0,2,(L,B))
columns,rows = int( X/L), int(Y/B)


# print(boxes)
screen = pg.display.set_mode((X,Y))
clock =pg.time.Clock();
running = True


WindowPaused = True
WindowEdit = False
while running:
    for event in pg.event.get():
        mouse_x,mouse_y=pg.mouse.get_pos()
         
        if event.type == pg.MOUSEBUTTONDOWN:
            x,y =pg.mouse.get_pos()
            logic.state_changer((x//columns,y//rows),boxes,None)  
            
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                WindowPaused = not WindowPaused
            if event.key == pg.K_e:
                WindowEdit = not WindowEdit
            if event.key == pg.K_r:
                boxes.fill(False)
                

    if WindowPaused:
        display_paused(screen)
    elif WindowEdit:
       
        screen.fill("black")
        make_grid(screen,rows,columns,X,Y)
        paint_cells(screen,rows,columns,boxes)
        make_grid(screen,rows,columns,X,Y)

    else:         
        screen.fill("black")
        make_grid(screen,rows,columns,X,Y)
        paint_cells(screen,rows,columns,boxes)
        make_grid(screen,rows,columns,X,Y)
        boxes=logic.life(boxes).copy()
        time.sleep(0.5)
    

    pg.display.flip()
    clock.tick(60)
pg.quit()


