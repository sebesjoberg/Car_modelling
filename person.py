class person():
    def __init__(self,job="student"):
        self.job = job
        self.usingcar = False
        if job == "student":
            self.night = [0.1/7,2]
            self.day  = [0,2]
            self.evening = [0,2]
        elif job == "homeworker":
            self.night = [0.1/7,2]
            self.day  = [0,2]
            self.evening = [0,2]
        elif job == "officeworker":
            self.night = [0.1/7,2]
            self.day  = [0,2]
            self.evening = [0,2]
        else:
            self.night = [0.1/7,2]
            self.day  = [0,2]
            self.evening = [0,2]