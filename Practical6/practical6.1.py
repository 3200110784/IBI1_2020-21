import matplotlib.pyplot as plt
country= ["USA", "India", "Brazil", "Russia", "UK"]#list country
totalcases= [29862124, 11285561, 11205972, 4360823, 4234924]#list total cases
fre= {"USA":29862124, "India":11285561, "Brazil":11205972, "Russia":4360823, "UK":4234924}#make a dictionary
explode=(0.05, 0, 0, 0, 0)
plt.pie(totalcases,explode=explode, labels=country, autopct='%1.1f%%', shadow=True)#make a figure
plt.axis('equal')
plt.show()#show the figure