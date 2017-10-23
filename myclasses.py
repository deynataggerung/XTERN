import csv, sys, math, datetime, pickle
import matplotlib.pyplot as plt
import numpy as np

args = sys.argv

# add args check

#data structure to store information on each location in relation to a person
class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #coordinates is a list of all the close points included in this location
        self.coordinates = []
        self.coordinates.append([x,y])
        
        self.avgInterval = 0
        self.varInterval = 0
        self.range = 0
        self.times = []
        self.intervals = []
    
    #redefines x and y as the average of all nearby points
    def update(self):
        sumx = 0
        sumy = 0
        for coord in self.coordinates:
            sumx += coord[0]
            sumy += coord[1]
        self.x = sumx/len(self.coordinates)
        self.y = sumy/len(self.coordinates)
    
    #takes a datetime type and adds it to the list of times this location was visited
    def addTime(self, datetime, x, y):
        #we will update the new location center as an aggregate 
        self.coordinates.append([x,y])
        self.update()
        
        self.times.append(datetime)
        
    def analyze(self):
        #the times need to be sorted because I want to track successive visits
        sort(self.times)
        
        #create a list of the intervals between visits
        for i in range(len(self.times)):
            self.intervals.append(self.times[i+1] - self.times[i])
        
        #find the average interval between visits
        self.avgInterval = sum(intervals) / len(self.times)
        
        #get the variance to see how regular the interval is
        variance = datetime.timedelta(0)
        for i in self.intervals:
            variance += pow((i - self.avgInterval), 2)
        self.varInterval = variance / len(self.intervals)
        
        #calc range of visit times, is this one off, several weeks, months?
        self.range = self.times[len(self.times)-1] - self.times[0]
        
    def close(self, x, y):
        if (pow((self.x - x), 2) + pow((self.y - y), 2)) < 0.1:
            return True
        return False
        
            
#data structure to hold information for each person separately
class Person():
    def __init__(self, number):
        #given identity and and initialize dictionaries for storing location/time data
        self.identity = number
        self.locations = []
    
    #adds each data point to the locations table.
    def addPoint(self, time, x, y):
        #decide if the point should be added to a pre-existing spot
        for location in self.locations:
            if location.close(x, y):
                location.addTime(time, x, y)
                #this assumes it's not close to more than one pre-existing spot, 
                return
            
        #otherwise add a new location at x
        self.locations.append(Location(x,y))

def createDate(timestamp):
    dateandtime = timestamp.split(" ")
    dateandtime[0] = dateandtime[0].split("-")
    dateandtime[1] = dateandtime[1].split(":")
    return datetime.datetime(int(dateandtime[0][0]), int(dateandtime[0][1]), int(dateandtime[0][2]), int(dateandtime[1][0]), int(dateandtime[1][1]), int(dateandtime[1][2]))
        