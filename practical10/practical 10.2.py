
class student(object):
    def __init__ (self,fname,lname,programm):#self assignment
        self.fname=fname
        self.lname=lname
        self.programm=programm
    def output(self):
        print(self.fname,self.lname,self.programm)#pring the outcome 
studentA = student('Ming', 'Xiao', 'BMS')
studentA.output()