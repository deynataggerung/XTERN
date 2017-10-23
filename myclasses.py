import csv, sys, math, datetime, pickle
import matplotlib.pyplot as plt
import numpy

#data structure to store information on each location in relation to a person
class Location():
    def __init__(self, datetime, x, y):
        self.x = x
        self.y = y
        #coordinates is a list of all the close points included in this location
        self.coordinates = []
        self.coordinates.append([x,y])
        
        self.avgTimes = datetime.time()
        self.stdTimes = datetime.time()
        self.avgInterval = 0
        self.stdInterval = 0
        self.range = 0
        self.times = []
        self.intervals = []
        
        #initialized with a time
        self.addTime(datetime, x, y)
    
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
        #get the average time
        minutes = [(i.hour*60 + i.minute) for i in self.times]
        taverage = int(numpy.average(minutes))
        self.avgTimes = datetime.time(taverage/60, taverage%60)
        
        #get the standard deviation of times
        tstd = int(numpy.std(minutes))
        self.stdTimes = datetime.time(tstd/60, tstd%60)
        
        #calc range of visit times, is this one off, several weeks, months?
        self.range = self.times[-1] - self.times[0]
        
        #if there is only one instance then we can't have intervals and there's nothing to change
        if len(self.times) == 1:
            return
        
        #the times need to be sorted because I want to track successive visits
        self.times.sort()
        
        #create a list of the intervals between visits
        for i in range(len(self.times)-1):
            self.intervals.append(self.times[i+1] - self.times[i])
        
        #find the average interval between visits
        self.avgInterval = sum(self.intervals, datetime.timedelta(0)) / len(self.times)
        
        #get the variance to see how regular the interval is
        #Converts to second, gets the variance and then converts back to a timedelta
        self.stdInterval = datetime.timedelta(seconds=(numpy.std([time.total_seconds() for time in self.intervals])))
        
        
    def close(self, x, y):
        if (pow((self.x - x), 2) + pow((self.y - y), 2)) < 0.01:
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
        self.locations.append(Location(time, x, y))
        
    #run the analysis on all locations
    def analyze(self):
        for location in self.locations:
            location.analyze()

def createDate(timestamp):
    dateandtime = timestamp.split(" ")
    dateandtime[0] = dateandtime[0].split("-")
    dateandtime[1] = dateandtime[1].split(":")
    return datetime.datetime(int(dateandtime[0][0]), int(dateandtime[0][1]), int(dateandtime[0][2]), int(dateandtime[1][0]), int(dateandtime[1][1]), int(dateandtime[1][2]))
        
