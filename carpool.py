from random import random as rand
class carpool():
    def __init__(self,cars=999999):
        self.cars = cars
        self.cars_in_use = []
        self.night = [22,23,0,1,2,3,4,5]
        self.day = [6,7,8,9,10,11,12,13,14,15,16,17]
        self.evening = [18,19,20,21]

    def step(self,h,persons):
        #remove one hour from each car
        self.unoccopy()
        #first look at hour by using modulo
        hour = h%24
        if hour in self.night:
            for p in persons:#now add conditions for job types esp in day
                if rand() < p.night[0] and not p.usingcar:
                    self.occupy(p,p.night[1])
        if hour in self.day:
            for p in persons:
                if rand() < p.day[0] and not p.usingcar:
                    self.occupy(p,p.day[1])
        if hour in self.evening:
            for p in persons:
                if rand() < p.evening[0] and not p.usingcar:
                    self.occupy(p,p.evening[1])
        return len(self.cars_in_use)
    
    def occupy(self,p,hours):
        self.cars_in_use.append([hours,p])
        p.usingcar = True
    def unoccopy(self):
        new_cars = []
        for index in range(len(self.cars_in_use)):
           
            car,person = self.cars_in_use[index]
            car = car - 1
            if car > 0:
                new_cars.append([car,person])
            else:
                person.usingcar = False
        self.cars_in_use = new_cars


        