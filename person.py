
from scipy.stats import poisson
class person():
    def __init__(self):
        #for work day

        self.night = int(poisson.rvs(mu=2,size=1))
        self.day  = int(poisson.rvs(mu=78,size=1))
        self.evening = int(poisson.rvs(mu=45,size=1))

        # 10 60 30
        #for non-work day
        #self.night = 0.1*int(poisson.rvs(mu=47,size=1))
        #self.day  = 0.6*int(poisson.rvs(mu=47,size=1))
        #self.evening = 0.3*int(poisson.rvs(mu=47,size=1))

