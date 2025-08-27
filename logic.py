import numpy as np
from typing import Union
# 1)Any live cell with fewer than two live neighbours dies, 
# as if by underpopulation.
# 2)Any live cell with two or three live neighbours
#  lives on to the next generation.
# 3)Any live cell with more than three live neighbours dies
# , as if by overpopulation.
#4) Any dead cell with exactly three live neighbours becomes a live cell,
#  as if by reproduction.
def judge(cell:tuple,neighbour_live_count:int,np_array:np.ndarray)->None:
    isalive = check_alive(cell,np_array)
    if(isalive and neighbour_live_count<2):
        state_changer(cell,np_array,0)
    elif(isalive and neighbour_live_count>3):
        state_changer(cell,np_array,0)
    elif(not isalive and neighbour_live_count==3):
        state_changer(cell,np_array,1)
    else:
        state_changer(cell,np_array,isalive)

 
def does_cell_exist(cell:tuple,array_shape:tuple)->bool:
    x,y = cell
    length_x,length_y = array_shape
    if(x < 0 or y < 0):
        return False
    if(x> length_x-1 or y > length_y-1):
       # print("Index out of bound")
        return False
    return True


def state_changer(cell:tuple,np_array:np.ndarray,state:Union[None,bool])->None:
    x,y = cell
    if does_cell_exist(cell,np_array.shape):
        np_array[x,y] = not(np_array[x,y]) if state==None else state 


def check_alive(cell:tuple,np_array:np.ndarray)->bool:
    x,y = cell
    if does_cell_exist(cell,np_array.shape):
        return bool(np_array[x,y])


def enumerate_neighbours(cell:tuple,np_array:np.ndarray)->list[tuple]:
    neighbours =[]
    x,y=cell
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if does_cell_exist((i,j),np_array.shape) and not (x==i and y==j):
                neighbours.append((i,j))
    return neighbours
                
def check_live_neighbours(cell:tuple,np_array:np.ndarray)->int:  #ask for opinion here
    neighbours = enumerate_neighbours(cell,np_array)
    neighbour_count =0
    for neighbour in neighbours:
        alive = check_alive(neighbour,np_array)
        if alive:
            neighbour_count+=1
    return neighbour_count


def life(np_array:np.ndarray)->np.ndarray:
    np_copy_array = np_array.copy()
    l,b = np_array.shape
    for i in range(l):
        for j in range(b):
            live_neighbours = check_live_neighbours((i,j),np_array)
            judge((i,j),live_neighbours,np_copy_array)
    return np_copy_array