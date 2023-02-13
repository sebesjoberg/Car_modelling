from person import person as p
from carpool import carpool as c
import matplotlib.pyplot as plt




def simulation(days,nb_persons=20):
    persons = []#for loops ads the residents
    carpool = c()
    
    cars_in_use = []
    x = []
    crashes = []
    for i in range(nb_persons):
        persons.append(p())
    times = ["night","day","evening"]*days
    #filt = [person for person in persons if person.job=="kid"]
    for h in range(len(times)): 
        t = times[h]
        x.append(h+1)
        cars,cr = carpool.step(t,persons)
        cars_in_use.append(cars)
        crashes.append(cr)
       
        
        

    return x,cars_in_use,crashes
    
def plot_max():
    max_cars = []
    steps = []
    crashes_per_week_person = []
    days = 365
    for x in range(100):
   
        time,cars,crashes = simulation(days,33)
        steps.append(x+1)
        max_cars.append(max(cars))
        crashes_per_week_person.append((sum(crashes)*7)/(days*33))
        
    plt.plot(steps,max_cars,label="Max_cars/simulation")
    plt.plot(steps,crashes_per_week_person,label="crashes/week*persons")
    plt.ylabel('cars')
    plt.xlabel('timestep')
    plt.legend()
   
    plt.show()    
    
def plot_simulation(times):
    days=30
    for t in range(times):
    
        time,cars,crashes = simulation(days,33)
        plt.plot(time,cars,label="cars used")
        plt.plot(time,crashes, label="crashes")
    plt.ylabel('cars')
    plt.xlabel('timestep')
    plt.legend()
   
    plt.show() 
if __name__ == '__main__':
    plot_max()
    #plot_simulation(1)


