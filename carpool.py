from random import random as rand
class carpool():
    def __init__(self,cars=12):
        self.cars = cars
        self.cars_in_use = 0
        

    def step(self,time,persons):
        #remove one hour from each car
        self.cars = self.cars + self.cars_in_use
        self.cars_in_use = 0
        crashes = 0
        if time == "night":
            for p in persons:
                if (100*rand()) < p.night:
                    if self.cars > 0:
                        self.cars_in_use = self.cars_in_use+1
                        self.cars = self.cars - 1
                    else:
                        crashes += 1
                    #take away car and chekc if car is left
        if time == "day":
            for p in persons:
                if (100*rand()) < p.day:
                    if self.cars > 0:
                        self.cars_in_use = self.cars_in_use+1
                        self.cars = self.cars - 1
                    else:
                        crashes += 1
                    
        if time == "evening":
            for p in persons:
                if (100*rand()) < p.evening:
                    if self.cars > 0:
                        self.cars_in_use = self.cars_in_use+1
                        self.cars = self.cars - 1
                    else:
                        crashes += 1
        return self.cars_in_use,crashes
    
   
    


        