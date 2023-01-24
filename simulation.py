from person import person as p
from carpool import carpool as c
import matplotlib.pyplot as plt




def simulation(days,nb_of_students=20,nb_of_homeworkers=20,nb_of_officeworkers=20,nb_of_kids=20):
    persons = []#for loops ads the residents
    carpool = c()
    partdays = ["early", "day","evening"]
    cars_in_use = []
    x = []
    for i in range(nb_of_students):
        persons.append(p("student"))
    for i in range(nb_of_homeworkers):
        persons.append(p("homeworker"))
    for i in range(nb_of_officeworkers):
        persons.append(p("officeworker"))
    for i in range(nb_of_kids):
        persons.append(p("kid"))
    #filt = [person for person in persons if person.job=="kid"]
    for h in range(days*24): #each h represents a hour of the day depending on modulo do some things eg at 7 people go to work
        x.append(h)# add the hour
        cars_in_use.append(carpool.step(h,persons))
        
        

    return x,cars_in_use
    
    
    

if __name__ == '__main__':
    time,cars = simulation(10)
    plt.plot(time,cars)
    plt.ylabel('some numbers')
    plt.show()


