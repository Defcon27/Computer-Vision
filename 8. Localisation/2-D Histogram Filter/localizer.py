# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    
    for i in range(len(grid)):
        t=[]
        for j in range(len(grid)):
            #print(grid[i][j],beliefs[i][j])
            if(grid[i][j]==color):
                t.append(beliefs[i][j]*p_hit)
            else:
                t.append(beliefs[i][j]*p_miss)
            
        
        new_beliefs.append(t)
        
    
    print(new_beliefs)
    
    sum=.0
    for i in new_beliefs:
        for j in i:
            sum+=j
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            new_beliefs[i][j]=new_beliefs[i][j]/sum
    
    return new_beliefs
    
    
    

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)