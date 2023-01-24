from random import random as rand
class carpool():
    def __init__(self,cars=999999):
        self.cars = cars
        self.cars_in_use = [1,4]
        self.night = [22,23,0,1,2,3,4,5]
        self.day = [6,7,8,9,10,11,12,13,14,15,16,17]
        self.evening = [18,19,20,21]

    def step(self,h,persons):
        #remove one hour from each car
        self.cars_in_use = [car-1 for car in self.cars_in_use if car >1] # this decrements one hour and removes zeroed from queue
        #first look at hour by using modulo
        hour = h%24
        if hour in self.night:
            for p in persons:#now add conditions for job types esp in day
                if rand() < p.night[0]:
                    self.cars_in_use.append(p.night[1])
        if hour in self.day:
            for p in persons:
                if rand() < p.day[0]:
                    self.cars_in_use.append(p.day[1])
        if hour in self.evening:
            for p in persons:
                if rand() < p.evening[0]:
                    self.cars_in_use.append(p.evening[1])
        return len(self.cars_in_use)
        