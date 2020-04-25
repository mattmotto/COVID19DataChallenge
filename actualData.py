import random
import math
from matplotlib import pyplot as plt
import numpy as np

"""
Written by Matthew Otto for Daniel Bauer's Intro Computing course
"""

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
virality = 0.05   # probability that a neighbor cell is infected in 
                  # each time step 

avg_time_to_death = 18
stand_dev = 2

def setVirality(x):
    virality = x
    
def getVirality():
    return virality
                                
#def convertToLat(n):
#    # 40.752 - 40.508
#    return ((-(40.752 - 40.508)/149) * n + 40.752)     
#
#def convertToLong(n):
#    # -74.248 - -73.91
#    # n: 0 - 149
#    return ((-74.248 - (-73.91))/149) * n - 73.91

def coordsToN(*n):
#    return n[0][0]
    return ((int)((n[0][0] - 40.900819)/(-(40.900819 - 40.560167)/149)), (int)((n[0][1] + 73.70956)/((-74.04118 - (-73.70956))/149)))

#def longToN(n):
#    return (int)((n + 73.91)/((-74.248 - (-73.91))/149))

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time = 0
        self.numSpread = 0
        self.numInfected = 0
    
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
    
    def infect(self):
        self.time = 0
        self.state = "I"
    
#    def process(self, adjacent_cells, cells):
#        if(self.state == "I" and self.time > recovery_time):
#            self.state = "E"
#        
#        if(self.state == "I" and self.time >= 1):
#            for c in adjacent_cells:
#                if (c.state == "S"):
#                    if (random.random() <= self.virality):
#                        c.infect()
#                        self.numInfected += 1
#            
#            farSpread = random.choice(list(cells.keys()))
#            if (cells[farSpread].state == "S"):
#                if (random.random() <= self.virality):
#                    cells[farSpread].infect()
#                    self.numInfected += 1
            
        
                
            
                        
#        if(self.state == "I" and pdeath(self.time, avg_time_to_death, stand_dev) > random.random() and self.time >= 1):
#            self.state = "R"
        
#        self.time += 1
    
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
            if (self.cells[c].numInfected == 0):
                a[self.cells[c].x, self.cells[c].y, 0] = 1.0
                a[self.cells[c].x, self.cells[c].y, 1] = 1.0
                a[self.cells[c].x, self.cells[c].y, 2] = 1.0
#            elif (self.cells[c].state == "R"):
#                a[self.cells[c].x, self.cells[c].y, 0] = 0.5
#                a[self.cells[c].x, self.cells[c].y, 1] = 0.5
#                a[self.cells[c].x, self.cells[c].y, 2] = 0.5
            else:
                a[self.cells[c].x, self.cells[c].y, 0] = 1.0/2486 * self.cells[c].numInfected
                a[self.cells[c].x, self.cells[c].y, 1] = 0
                a[self.cells[c].x, self.cells[c].y, 2] = 0
#            elif (self.cells[c].state == "E"):
#                a[self.cells[c].x, self.cells[c].y, 0] = 0
#                a[self.cells[c].x, self.cells[c].y, 1] = 0
#                a[self.cells[c].x, self.cells[c].y, 2] = 1.0
            
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

        RNaught = totalSpread/totalCells
        
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
                
    def getCells(self):
        return self.cells

            
def read_map(filename):
    
    m = Map()
    
    f = open(filename,'r')
    
    for line in f:
        coordinates = line.strip().split(',')
        c = Cell(int(coordinates[0]),int(coordinates[1]))
        Map.add_cell(m, c)

    return m

def readZips(filename):
    zips = dict()
    
    f = open(filename,'r')
    
    for line in f:
        data = line.split(';')
        zipCode = data[0]
        if(zipCode != "Zip"):
            lat = float(data[3])
            long = float(data[4])
            zips[zipCode] = (lat, long)
    
    return zips

def readTests(filename):
    tests = dict()
    
    f = open(filename,'r')
    
    firstLine = True
    lines = []
    
    for line in f:
        data = line.split(',')
#        print(data)
        if(firstLine):
            for i in range(2, len(data) - 2):
#                print(int(float(data[i])))
                tests[str(int(float(data[i])))] = []
            firstLine = False
        else:
#            for i in range(2, len(data) - 2):
#                temp = []
#                temp.append(data[i])
#                lines.append(temp)
#                print(data[i])
            temp = data[2:31] + data[32:len(data) - 2]
            lines.append(temp)
            
#                
#    print(lines)
            
    allKeys = list(tests.keys())
#    print(allKeys)
#    print(len(allKeys))
            
    for l in lines:
#        print(l)
#        print(len(l))
        for i in range(0, len(l)):
            tests[allKeys[i]].append(int(l[i]))
        
    
    return tests

zipCodes = readZips('us-zip-code-latitude-and-longitude.csv')
tests = readTests('april_zipcode_positive.csv')

del tests['10065']
del tests['10075']

allKeys = list(tests.keys())

m = read_map('nyc_map.csv')

#m = Map()
maxLat = 0.0
minLat = 100.0

maxLong = -1000.0
minLong = 1000.0
for key in allKeys:
    # -74.248 - -73.91
#    if (coordsToN(zipCodes[key])[0] > 40.752 or coordsToN(zipCodes[key])[0] < 40.508
#        or coordsToN(zipCodes[key])[1] > -73.91 or coordsToN(zipCodes[key])[1] < -74.248):
#        print(zipCodes[key])
    
#    if (zipCodes[key][0] > maxLat):
#        print(zipCodes[key][0], '>', maxLat)
#        maxLat = zipCodes[key][0]
#        
#    if (zipCodes[key][0] < minLat):
#        print(zipCodes[key][0], '<', minLat)
#        minLat = zipCodes[key][0]
#        
#    if (zipCodes[key][1] > maxLong):
#        print(zipCodes[key][1], '>', maxLong)
#        maxLong = zipCodes[key][1]
#        
#    if (zipCodes[key][1] < minLong):
#        print(zipCodes[key][1], '<', minLong)
#        minLong = zipCodes[key][1]
    
    c = Cell(coordsToN(zipCodes[key])[0], coordsToN(zipCodes[key])[1])
    Map.add_cell(m, c)
        
#print('maxLat:', maxLat)
#print('minLat:', minLat)
#print('minLong:', minLong)
#print('maxLong:', maxLong)
    
m.display()
    

for i in range(0, len(tests[allKeys[0]])):
#    biggest = 0
    for key in allKeys:
#        print(m.cells[coordsToN(zipCodes[key])])
        m.cells[coordsToN(zipCodes[key])].numInfected = tests[key][i]
#        print(coordsToN(zipCodes[key]))
#        if(tests[key][i] > biggest):
#            biggest = tests[key][i]
#        print(coordsToN(zipCodes[key]), ':', tests[key][i])
    m.display()        
    plt.pause(0.001)
    

#print(biggest)
        
#print(tests)

    
