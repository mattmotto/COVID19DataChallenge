import random
import math
from matplotlib import pyplot as plt
import numpy as np

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
        
    return integral    
    
recovery_time = 14 # recovery time in time-steps
virality = 0.15   # probability that a neighbor cell is infected in 
                  # each time step 

avg_time_to_death = 15
stand_dev = 2
                                                 

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0
        self.numInfected = 0
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
    
    def infect(self):
        self.time = 0
        self.state = "I"
    
    def process(self, adjacent_cells, cells):
        if(self.state == "I" and self.time > recovery_time):
            self.state = "E"
        
        if(self.state == "I" and self.time >= 1):
            for c in adjacent_cells:
                if (c.state == "S"):
                    if (random.random() <= virality):
                        c.infect()
                        self.numInfected += 1
            
            farSpread = random.choice(list(cells.keys()))
            if (cells[farSpread].state == "S"):
                if (random.random() <= virality):
                    cells[farSpread].infect()
                    self.numInfected += 1
                
            
                        
        if(self.state == "I" and pdeath(self.time, avg_time_to_death, stand_dev) > random.random() and self.time >= 1):
            self.state = "R"
        
        self.time += 1
    
    def getNumInfected(self):
        return self.numInfected
    
    def getState(self):
        return(self.state)
        
        
        
class Map(object):
    
    cells = dict()
    
    peoplePerCell = 8398748/7378
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        self.cell = cell
        key = (cell.x, cell.y)
        self.cells[key] = self.cell
        
    def display(self):
        a = np.zeros(shape=(150,150,3))
        
#        print("R_0 = " + self.getRNaught())
        
        # make each pixel black by default
        for x in range(0, 150):
            for y in range(0, 150):
                a[x, y, 0] = 0
                a[x, y, 1] = 0
                a[x, y, 2] = 0
        
        # draw out the cells
        for c in self.cells:
            if (self.cells[c].state == "S"):
                a[self.cells[c].x, self.cells[c].y, 0] = 0
                a[self.cells[c].x, self.cells[c].y, 1] = 1.0
                a[self.cells[c].x, self.cells[c].y, 2] = 0
            elif (self.cells[c].state == "R"):
                a[self.cells[c].x, self.cells[c].y, 0] = 0.5
                a[self.cells[c].x, self.cells[c].y, 1] = 0.5
                a[self.cells[c].x, self.cells[c].y, 2] = 0.5
            elif (self.cells[c].state == "I"):
                a[self.cells[c].x, self.cells[c].y, 0] = 1.0
                a[self.cells[c].x, self.cells[c].y, 1] = 0
                a[self.cells[c].x, self.cells[c].y, 2] = 0
            elif (self.cells[c].state == "E"):
                a[self.cells[c].x, self.cells[c].y, 0] = 0
                a[self.cells[c].x, self.cells[c].y, 1] = 0
                a[self.cells[c].x, self.cells[c].y, 2] = 1.0
            
        plt.imshow(a)
    
    def adjacent_cells(self, x, y):
        adjacent_cells = []
        
        if ((x-1, y) in self.cells):
            adjacent_cells.append(self.cells[(x-1, y)])
        if ((x+1, y) in self.cells):
            adjacent_cells.append(self.cells[(x+1, y)])
            
        if ((x, y-1) in self.cells):
            adjacent_cells.append(self.cells[(x, y-1)])
        if ((x, y+1) in self.cells):
            adjacent_cells.append(self.cells[(x, y+1)])
                
        return adjacent_cells
    
    def time_step(self):
        # Update each cell on the map 
        # display the map.
        
        # ... cell.process(adjacent_cells... )
        for c in self.cells:
            self.cells[c].process(self.adjacent_cells(self.cells[c].x, self.cells[c].y), self.cells)
            
        self.display()
        
    def total_cells(self):
        return len(self.cells)
    
    def getRNaught(self):
        totalCells = 0
        totalSpread = 0
        
        for c in self.cells:
            if (self.cells[c].numInfected > 0):
                totalSpread += self.cells[c].getNumInfected()
                totalCells += 1

        RNaught = totalCells/totalSpread * 7
        
        return RNaught
    
    def numCurrentlyInfected(self):
        ans = 0
        for c in self.cells:
            if (self.cells[c].getState() == "I"):
                ans += 1
        return ans
    
    def totalNumInfected(self):
        ans = 0
        for c in self.cells:
            if (self.cells[c].getState() == "I" or 
                self.cells[c].getState() == "E" or 
                self.cells[c].getState() == "R"):
                ans += 1
        return ans
    
    def getNumDead(self):
        ans = 0
        for c in self.cells:
            if (self.cells[c].getState() == "R"):
                ans += 1
        return ans
    
    def getNumRecovered(self):
        ans = 0
        for c in self.cells:
            if (self.cells[c].getState() == "E"):
                ans += 1
        return ans
                
    
    def test(self):
        for c in self.cells:
            if (self.cells[c].state == 'I'):
                print(self.cells[c].numInfected)
                
    def getCells():
        return self.cells

            
def read_map(filename):
    
    m = Map()
    
    f = open(filename,'r')
    
    for line in f:
        coordinates = line.strip().split(',')
        c = Cell(int(coordinates[0]),int(coordinates[1]))
        Map.add_cell(m, c)

    return m
