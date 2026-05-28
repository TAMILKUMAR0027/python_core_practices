class TeamMember1:
    def __init__(self,name,uid):
        self.name=name
        self.uid=uid
    def display(self):
        print(f"Team member: {self.name}, UID : {self.uid}")
class worker:
    def __init__(self,pay,jobTitle):
        self.pay=pay
        self.jobTitle=jobTitle
    def display(self):
        print(f"Worker: {self.jobTitle}, Pay:{self.pay}")
class TeamLeader1(TeamMember1,worker):
    def __init__(self, name, uid,pay,jobtitle,exp):
        self.exp=exp
        TeamMember1.__init__(self,name,uid)
        worker.__init__(self,pay,jobtitle)
    def display(self):
        TeamMember1.display(self)
        worker.display(self)
        print(f"Experience: {self.exp}")


tl=TeamLeader1("Tamil",1001,25000,"SDET",5)
tl.display()