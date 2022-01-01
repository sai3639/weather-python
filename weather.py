# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:30:05 2021

@author: saira

"""
import numpy as np

FolderName = "/Users/saira/lab1b/"
wFileName = FolderName + "CLLWeatherData.csv"

Dates = []
WindSpeeds = []
MaxTemp = []
TempMin = []
Percip = []
Avg_Temp = []

with open(wFileName, 'r') as wFileID:
    wHeader = wFileID.readline()
    for Eachline in wFileID:
        LineParts = Eachline.strip('\n').split(',')
        Dates.append(LineParts[0])
        WindSpeeds += [float(LineParts[1])]
        Avg_Temp += [float(LineParts[3])]
        MaxTemp += [float(LineParts[4])]
        Percip += [float(LineParts[2])]
        TempMin.append(float(LineParts[5]))


#find the maximum temperature value
tempmax = MaxTemp[0]
for temp in MaxTemp:
    if tempmax < temp:
        tempmax = temp
print('3-year maximum temperature: ',tempmax)
    

# find the minimum temperature value
mintemp = TempMin[0]
for temp in TempMin:
    if temp < mintemp:
        mintemp = temp
print("3-year minimum temperature: ", mintemp)



#find the average daily precipitation 
avg_prec = 0
for prec in Percip:
    avg_prec += prec
avg_prec = avg_prec/len(Percip)
print('3-year average precipitation: {:.3f}'.format(avg_prec))
    


#find the mean of the average tempeartures 


#print("len(Dates) = {:d} == {:d} = len(MaxTemp) = {}".
 #     format(len(Dates), len(MaxTemp), len(Dates) == len(MaxTemp)))
#print(TempMin)


TempMin = np.array(TempMin) + 459.6   #R
Precip = np.array(Percip) * 25.4      # mm
#print(TempMin)



import matplotlib.pyplot as plt

PreciTemFig = plt.figure(1)

plt.plot(Precip, color='blue', label='Precipitation')

plt.xlabel("Day")
plt.ylabel("Precip. (mm)")
plt.legend(loc = 'upper center')
plt.title("Precip. & Temp.")
plt.suptitle("Easterwood Airport weather 2017-2020")
plt.twinx()

plt.plot(TempMin, color='m', label='$T_{min}$')
plt.ylabel("Temp. (R)")
plt.legend(loc = "upper right")


PTFigSubPlots = plt.figure(2)
plt.subplot(2, 2, 1)
plt.plot(Precip, color='blue', label="Precipitation")
plt.xlabel("Day")
plt.ylabel("Precip. (mm)")
plt.legend(loc = 'upper center')
plt.title("Precip. & Temp.")

plt.subplot(2, 2, 2)
plt.plot(TempMin, color='m', label='$T_{min}$')
plt.ylabel("Temp. (R)")
plt.xlabel('Day')
plt.legend(loc = "lower right")
plt.title("Min Temp.")
plt.subplots_adjust(hspace = .5)

plt.subplot(2, 2, 3)
plt.plot(TempMin, Precip, color='c', label='$Precip(T_{min})$')
plt.ylabel("Precip. (mm)")
plt.xlabel('Temp. (R)')
plt.legend(loc = "upper left")
plt.title("Precip. vs T")

plt.subplot(2, 2, 4)
plt.plot(Precip, TempMin, color='orange', label='$T_{min}(Precip)$')
plt.ylabel("Temp. (R)")
plt.xlabel('Precip. (mm)')
plt.legend(loc = "lower right")
plt.title("T vs Precip.")

plt.show()