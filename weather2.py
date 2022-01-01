# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:30:05 2021

@author: saira

"""

# Date:              12 November 2021
#weather
import numpy as np

#FolderName = "/Users/saira/lab1b/"
#wFileName = FolderName + "CLLWeatherData.csv"

Dates = []
WindSpeeds = []
MaxTemp = []
TempMin = []
Precip = []
Avg_Temp = []
#all_data = []
with open('CLLWeatherData.csv', 'r') as wFileID:
    wHeader = wFileID.readline()
    for Eachline in wFileID:
        
        LineParts = Eachline.strip('\n').split(',')
        Dates.append(LineParts[0])
        WindSpeeds += [float(LineParts[1])]
        Avg_Temp += [float(LineParts[3])]
        MaxTemp += [float(LineParts[4])]
        Precip += [float(LineParts[2])]
        TempMin.append(float(LineParts[5]))

#print(all_data)
#print(MaxTemp)
#print(Dates)
#find the maximum temperature value
tempmax = MaxTemp[0]
for temp in MaxTemp:
    if tempmax < temp:
        tempmax = temp
print('3-year maximum temperature:',int(tempmax), "F")
    

# find the minimum temperature value
mintemp = TempMin[0]
for temp in TempMin:
    if temp < mintemp:
        mintemp = temp
print("3-year minimum temperature:", int(mintemp), "F")



#find the average daily precipitation 
avg_prec = 0
for prec in Precip:
    avg_prec += prec
avg_prec = avg_prec/len(Precip)
print('3-year average precipitation: {:.3f} inches'.format(avg_prec))
  

with open('CLLWeatherData.csv', 'r') as weather:
    title = weather.readline()
    weather_read = weather.read().strip().split('\n')
    all_data = []
    for line in weather_read:
        all_data.append(line.split(','))

months = {'January' : 1,
          'February': 2,
          'March': 3,
          'April': 4,
          'May' : 5,
          'June': 6,
          'July': 7,
          'August': 8,
          'September': 9,
          'October': 10,
          'November': 11,
          'December': 12
          }

month = (input("\nPlease enter a month: "))
year = int((input("Please enter a year: ")))
#Dates = Dates.split('/')
#print(Dates[2])
new_dates = []
# for data in all_data:
#        # data.split('\n')
#         data = data.strip().split(',')
#         for i in data:
#             data.append(i.split(','))

for i in all_data:
    date = i[0].split('/')
    if months[month] == int(date[0]) and year == int(date[2]):
        new_dates.append(i)

# for date in Dates:
#     date = date.split('/')
    
#     # print(date)
#     # for month1 in months:
#     #     if month == month1:
#     #         #month = months[1]
#     #         month = (months[month1])
#     for x in i:
#        # print(x)
#         if month == int(date[0]) and year == int(date[2]):
#             print(x)
#             new_dates.append(x)
              #  print(new_dates)
#print(new_dates)
    # for month1 in months:
    #     if month == month1:
    #         #month = months[1]
    #         month = (months[month1])
            
  #  year = date[2]


# new_dates = []
# for month1 in Dates:
#     date = month1[0].split('/')
#     print(date)
#     if months[month] == int(date[0]) and year == int(date[2]):
#         new_dates.append(month1)
        
avg_temp = 0
percent_wind = 0
daily_precip = 0
count = 0
#print(new_dates[2])

for dates in new_dates:
    #print(dates[2])
    avg_temp += float(dates[3])
    if float(dates[1]) > 10:
        count += 1
    daily_precip += float(dates[2])
    
avg_temp = avg_temp/len(new_dates) 
percent_wind = count/len(new_dates) * 100
daily_precip = daily_precip/len(new_dates)

print('\nFor {} {}:'.format(month, year))
print('Mean daily temperature: {:.1f} F'.format(avg_temp))
print('Percentage of days with average wind speed above 10 mph: {:.1f}%'.format(percent_wind))
print('Mean daily precipitation: {:.4f} inches'.format(daily_precip))    
    
            
    #print(date[2])
#print(months['April'])   
    
# go through dictionary of months and compare month input till match found
#find the mean of the average tempeartures 
# print("Mean daily temperature: {:.1f} F".format(np.mean(Avg_Temp)))

# # find the average daily wind speed above 10 mph
# ten_wind = 0
# for winds in WindSpeeds:
#     if winds > 10:
#         ten_wind += 1
# ten_wind = ten_wind/len(WindSpeeds)
# print("Percentage of days with average wind speed above 10 mph: {:.1f}%".format(ten_wind))

# # find the mean daily precipiTATION
# print("Mean daily precipitation: {:.4f} inches".format(np.mean(Precip)))


#print("len(Dates) = {:d} == {:d} = len(MaxTemp) = {}".
 #     format(len(Dates), len(MaxTemp), len(Dates) == len(MaxTemp)))
#print(TempMin)


TempMin = np.array(TempMin) + 459.6   #R
Precip = np.array(Precip) * 25.4      # mm
print(TempMin)
SoundSpeed = np.sqrt(1.4 * 287.0 * MaxTemp)
WindSpeeds = np.array(WindSpeeds) * 1600 / 3600
WindMachNo = WindSpeeds/SoundSpeed

# save the data
def SaveSpeeds(SpeedFileName):
    SpeedFileName = 'WindSonic.csv'
    with open(SpeedFileName, 'w') as SpeedFileID:
        # Header - comma seperated
        SpeedFileHeader = "Date" + "," + "Wind speeds (m/s)" + ","+ "SoundSpeed (m/s)"
        SpeedFileHeader += ',' + 'Wind Mach#' + '\n'
        SpeedFileID.write(SpeedFileHeader) # write the header into the file
        for iData in range(len(SoundSpeed)):
            EachLine = Dates[iData] + ','
            EachLine += "{:.2f},".format(WindSpeeds[iData])
            EachLine += "{:.2f},".format(SoundSpeed[iData])
            EachLine += "{:.2f}\n".format(WindMachNo[iData])
            SpeedFileID.write(EachLine)
            
            
#graphing
# import matplotlib.pyplot as plt

# PreciTemFig = plt.figure(1)

# plt.plot(Precip, color='blue', label='Precipitation')

# plt.xlabel("Day")
# plt.ylabel("Precip. (mm)")
# plt.legend(loc = 'upper center')
# plt.title("Precip. & Temp.")
# plt.suptitle("Easterwood Airport weather 2017-2020")
# plt.twinx()

# plt.plot(TempMin, color='m', label='$T_{min}$')
# plt.ylabel("Temp. (R)")
# plt.legend(loc = "upper right")


# PTFigSubPlots = plt.figure(2)
# plt.subplot(2, 2, 1)
# plt.plot(Precip, color='blue', label="Precipitation")
# plt.xlabel("Day")
# plt.ylabel("Precip. (mm)")
# plt.legend(loc = 'upper center')
# plt.title("Precip. & Temp.")

# plt.subplot(2, 2, 2)
# plt.plot(TempMin, color='m', label='$T_{min}$')
# plt.ylabel("Temp. (R)")
# plt.xlabel('Day')
# plt.legend(loc = "lower right")
# plt.title("Min Temp.")
# plt.subplots_adjust(hspace = .5)

# plt.subplot(2, 2, 3)
# plt.plot(TempMin, Precip, color='c', label='$Precip(T_{min})$')
# plt.ylabel("Precip. (mm)")
# plt.xlabel('Temp. (R)')
# plt.legend(loc = "upper left")
# plt.title("Precip. vs T")

# plt.subplot(2, 2, 4)
# plt.ylabel("Temp. (R)")
# plt.xlabel('Precip. (mm)')
# plt.legend(loc = "lower right")
# plt.title("T vs Precip.")

# plt.show()
