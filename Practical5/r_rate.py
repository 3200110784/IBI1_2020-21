print("please enter r rate here")
r=float(input("r_rate="))
n=84
#initialize
for i in range(1,6):
 i=i+1
 n=n*r
#calculate the number of infected
m=str(int(n))
#to obtain an integer
print("the number of infected individuals after 5 rounds of infection for a given r rate "+ str(r) +" is "+m)
exit()
