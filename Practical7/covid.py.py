import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('D:\课件\第二学期\IBI\practical\上交')
covid_data = pd.read_csv("full_data.csv")#initialize

print(covid_data.iloc[0:11:2,:])#show columns and every second row between 0 to 10

my_row=[]
for i in range(0,len(covid_data)):
 if covid_data.loc[i,"location"] == "Afghanistan":
     my_row.append(True)
 else:
     my_row.append(False)
#compute a boolean for Afghanistan

print('All rows corresponding to Afghanistan')
print(covid_data.iloc[my_row,:])

world_new_cases=covid_data.loc[(covid_data["location"]=="World"),"new_cases"]
world_new_deaths=covid_data.loc[(covid_data["location"]=="World"),"new_deaths"]
world_dates=covid_data.loc[(covid_data["location"]=="World"),"date"]
#select the datas about world

median=np.median(world_new_cases)
mean=np.mean(world_new_cases)
print(median)
print(mean)
#calculate median and mean

plt.figure()
plt.boxplot(world_new_cases,vert=True,whis=1.5,patch_artist=True,meanline=True,showbox=True,showcaps=True,showfliers=True,notch=False,boxprops = {'color':'red','facecolor':'blue'})
plt.title("new cases boxplot")
#make a figure about world new cases (boxplot)

plt.figure()
plt.plot(world_dates, world_new_cases,'ro',label="new cases")
plt.plot(world_dates, world_new_deaths,'yo',label="new deaths")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.legend()
#make a figure anout world new cases and world new deaths

#Plot a boxplot of total case numbers in different countries on 14 March 2020
total_cases=covid_data.loc[(covid_data["date"]=="2020/3/14"),'total_cases']
plt.figure()
plt.boxplot(total_cases,vert=True, whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False, boxprops={'color':'pink','facecolor':'orangered'})
plt.title("total cases boxplot")
plt.show()