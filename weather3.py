# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:00:58 2021

@author: saira

"""

# Date:          November  2021


import numpy as np



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

#import matplotlib.pyplot as plt
#print(Precip)
#print(Dates)
    
#print(Dates)
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
# avg_prec = 0
# for prec in Precip:
#     avg_prec += prec
# avg_prec = avg_prec/len(Precip)
# print('3-year average precipitation: {:.3f} inches'.format(avg_prec))



with open('CLLWeatherData.csv', 'r') as weather:
    title = weather.readline()
    weather_read = weather.read().strip().split('\n')
   # Precip += [float(LineParts[2])]
    all_data = []
    for line in weather_read:
        all_data.append(line.split(','))
     #   print(all_data[line][0][0])
       # Precip += [float(LineParts[2])]
        

#print(TempMin)
#print(all_data)

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


#month1 = {'January': {'avg temp': 2}}

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

#days = []
#print(all_data)

Jan = []
Feb = []
March = []
April = []
May = []
June = []
July = []
Aug = []
Sept = []
Oct = []
Nov = []
Dec = []

sum_Jan = 0
sum_Feb = 0
sum_March = 0
sum_April = 0
sum_May = 0
sum_June = 0
sum_July = 0
sum_Aug = 0
sum_Sept = 0
sum_Oct = 0
sum_Nov = 0
sum_Dec = 0

month_dict = {}
    #print(dates[1])
for i in all_data:
   # red = all_data[0][0]   # date 
   # print(red)
    date = i[0].split('/')
    month1 = int(date[0])
    if month1 == 1:
        Jan.append(float((i[3])))
        sum_Jan += int(i[3])
    if month1 == 2:
        Feb.append(float((i[3])))
        sum_Feb += int(i[3])
    if month1 == 3:
        March.append(float(i[3]))
        sum_March += int(i[3])
    if month1 == 4:
        April.append(float(i[3]))
        sum_April += int(i[3])
    if month1 == 5:
        May.append(float(i[3]))
        sum_May += int(i[3])
    if month1 == 6:
        June.append(float(i[3]))
        sum_June += int(i[3])
    if month1 ==7:
        July.append(float(i[3]))
        sum_July += int(i[3])
    if month1 == 8:
        Aug.append(float(i[3]))
        sum_Aug += int(i[3])
    if month1 == 9:
        Sept.append(float(i[3]))
        sum_Sept += int(i[3])
    if month1 == 10:
        Oct.append(float(i[3]))
        sum_Oct += int(i[3])
    if month1 == 11:
        Nov.append(float(i[3]))
        sum_Nov += int(i[3])
    if month1 == 12:
        Dec.append(float(i[3]))
        sum_Dec += int(i[3])
        

        



    
    #print(date)
    
   # print(date)
   # day = date[1]
   # days.append(day)
    #day = date[1]
    #days.append(day)
   # day = date[1]
    #print(day)
    if months[month] == int(date[0]) and year == int(date[2]):
        new_dates.append(i)
#sum_months = [sum_Jan, sum_Feb, sum_March, sum_April, sum_May, sum_June, sum_July, sum_Aug, sum_Sept, sum_Oct, sum_Nov, sum_Dec]

month_dict[1] = Jan
month_dict[2] = Feb
month_dict[3] = March
month_dict[4] = April
month_dict[5] = May
month_dict[6] = June
month_dict[7] = July
month_dict[8] = Aug
month_dict[9] = Sept
month_dict[10] = Oct
month_dict[11] = Nov
month_dict[12] = Dec  
avg_Jan = 0
avg_Feb = 0
avg_March = 0
avg_April = 0
avg_May = 0
avg_June = 0
avg_July = 0
avg_Aug = 0
avg_Sept = 0
avg_Oct = 0
avg_Nov = 0
avg_Dec = 0
#for l in Jan:
 #   avg_Jan += 1
#avg_Jan/= len(Jan)     
mx1 = max(Jan)
mn1 = min(Jan)
avg_Jan = sum_Jan/len(Jan)
#for l in Feb:
#    avg_Feb += 1
#avg_Feb/= len(Feb)
mx2 = max(Feb)
mn2 = min(Feb)
avg_Feb = sum_Feb/len(Feb)
##   avg_March += 1
#avg_March /= len(March)
mx3 = max(March)
mn3 = min(March)
avg_March = sum_March/len(March)
##   avg_April += 1
#avg_April /= len(April)
mx4 = max(April)
mn4 = min(April)
avg_April = sum_April/len(April)
#for l in May:
#    avg_May += 1
#avg_May /= len(May)
mx5 = max(May)
mn5 = min(May)
avg_May = sum_May/len(May)
#for l in June:
 #   avg_June += 1
#avg_June /= len(June)
mx6 = max(June)
mn6= min(June)
avg_June = sum_June/len(June)
#for l in July:
#    avg_July += 1
#avg_July /= len(July)
mx7 = max(July)
mn7 = min(July)
avg_July = sum_July/len(July)
#for l in Aug:
 #   avg_Aug += 1
#vg_Aug /= len(Aug)
mx8 = max(Aug)
mn8 = min(Aug)
avg_Aug = sum_Aug/len(Aug)
##for l in Sept:
 #   avg_Sept += 1
#avg_Sept /= len(Sept)
mx9  = max(Sept)
mn9 = max(Sept)
avg_Sept = sum_Sept/len(Sept)
#for l in Oct:
 #   avg_Oct += 1
#avg_Oct /= len(Oct)
mx10 = max(Oct)
mn10 = min(Oct)
avg_Oct = sum_Oct/len(Oct)
#for l in Nov:
 #   avg_Nov += 1
#avg_Nov /= len(Nov)
mx11 = max(Nov)
mn11 = min(Nov)
avg_Nov = sum_Nov/len(Nov)
#for l in Dec:
 #   avg_Dec +=1
#avg_Dec /= len(Dec)
mx12 = max(Dec)
mn12 = min(Dec)
avg_Dec = sum_Dec/len(Dec)

print(avg_Jan)
mx =[mx1, mx2, mx3, mx4, mx5, mx6, mx7, mx8, mx9, mx10, mx11, mx12]
mn = [mn1, mn2, mn3, mn4, mn5, mn6, mn7, mn8, mn9, mn10, mn11, mn12]
#print(mx)
#print(mx)
  #  print(red)
#print(days)
#print(day)
#print(date)
#print(new_dates)
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
#print(new_dates)
days_list = []
for dates in new_dates:
   # print(dates[2])
   # print(dates)
    days = dates[0]
    days_list.append(days)
   # print(days
    #days.split('/')
   # day = days[1]
   # days_list.append(day)
    avg_temp += float(dates[3])
    if float(dates[1]) > 10:
        count += 1
    daily_precip += float(dates[2])
# actual_days_list = []
# for day in days_list:
#     day.split('/')
#     actual_day = day[1]
#     actual_days_list.append(actual_day)
#print(actual_days_list)
#print(days_list)    
avg_temp = avg_temp/len(new_dates) 
percent_wind = count/len(new_dates) * 100
daily_precip = daily_precip/len(new_dates)

print('\nFor {} {}:'.format(month, year))
print('Mean daily temperature: {:.1f} F'.format(avg_temp))
print('Percentage of days with average wind speed above 10 mph: {:.1f}%'.format(percent_wind))
print('Mean daily precipitation: {:.4f} inches'.format(daily_precip))    
#print(red)   
            
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


# TempMin = np.array(TempMin) + 459.6   #R
# Precip = np.array(Precip) * 25.4      # mm
# print(TempMin)
#SoundSpeed = np.sqrt(1.4 * 287.0 * MaxTemp)
#WindSpeeds = np.array(WindSpeeds) * 1600 / 3600
#WindMachNo = WindSpeeds/SoundSpeed

# save the data
# def SaveSpeeds(SpeedFileName):
#     SpeedFileName = 'WindSonic.csv'
#     with open(SpeedFileName, 'w') as SpeedFileID:
#         # Header - comma seperated
#         SpeedFileHeader = "Date" + "," + "Wind speeds (m/s)" + ","+ "SoundSpeed (m/s)"
#         SpeedFileHeader += ',' + 'Wind Mach#' + '\n'
#         SpeedFileID.write(SpeedFileHeader) # write the header into the file
#         for iData in range(len(SoundSpeed)):
#             EachLine = Dates[iData] + ','
#             EachLine += "{:.2f},".format(WindSpeeds[iData])
#             EachLine += "{:.2f},".format(SoundSpeed[iData])
#             EachLine += "{:.2f}\n".format(WindMachNo[iData])
#             SpeedFileID.write(EachLine)
            

#print(Precip)
import matplotlib.pyplot as plt


# #Plot 1
# #print(days_list)
# for days in days_list:
#     days.split(',')
#     #print(days)
#     days = str(days)
    #print(type(days))
   
fig = plt.figure(1)
ax = fig.add_subplot(111)

lns1 = ax.plot(Avg_Temp, color = 'red', label = 'Temp avg')
ax2= ax.twinx()
lns2 = ax2.plot(WindSpeeds, color = 'blue', label = 'Wind avg')
lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc = 0)

ax.set_xlabel("Day")
ax.set_ylabel("Average Temperature, F")
#ax.plt.legend(loc = 'lower left')
ax.set_title('Average Temperature and Wind Speed')
#ax.plot(label = 'Wind avg')

ax2.set_ylabel("Average Wind Speed, mph")
plt.show()
#plt.legend(loc = 'lower left')
#print(Precip)
#plt.twinx()

# Plot 2
#print(Precip)
# bins = 0
# precipmax = Precip[0]
# for precip in Precip:
#     if precipmax < precip:
#         precipmax = precip
# precipmin = Precip[0]
# for precip in Precip:
#     if precip < precipmin:
#         precipmin = precip
# Range = precipmax - precipmin
# intervals = np.sqrt(len(Precip))
# width = Range/intervals
#print(type(intervals))
#print(width)
#for precip in Precip:
    
# for precip in Precip:
#   #  print(precip)
#     if precip == 0:
#         Precip.remove(precip)

Precip_graph = plt.figure(2)
y = np.linspace(0.1,5,50)
plt.hist(Precip,y)

plt.show()  


#Plot 3

#TempMin = np.linspace(20,80)
TempWin = plt.figure(3)
plt.scatter(TempMin, WindSpeeds, color = 'black')
plt.title("Average Wind Speed vs Minimum Temeprature")
plt.xlabel('Minimum Temperature, F')
plt.ylabel('Average Wind Speed, mph')
plt.show()
#print(sum_months)
#print(Precip)
#print(TempMin)
# Plot 4
m = list(month_dict.keys())
values = list(month_dict.values())
bar = plt.figure(4)
#ax3 = bar.subplots(111)
month2 = [Jan, Feb, March, April, May, June, July, Aug, Sept, Oct, Nov, Dec]
month_num = [1,2,3,4,5,6,7,8,9,10,11,12]
y_values = [avg_Jan, avg_Feb, avg_March, avg_April, avg_May, avg_June, avg_July, avg_Aug, avg_Sept, avg_Oct, avg_Nov, avg_Dec]
plt.bar(month_num, y_values, color = 'y')
plt.title('Average Tempearture by Month')
plt.xlabel("Month")
plt.ylabel('Average Temperature, F')


#plt.bar(sum_months,values, color = 'green' )
plt.plot(month_num,mx, color = 'red', label = 'High T')
plt.legend(loc = 'upper left')
plt.plot(month_num,mn, color = 'blue', label = 'Low T')
plt.legend(loc = 'upper left')
#bar.set_ylabel(0,100)
#Plot 2
# Precip_graph = plt.figure(2)
# plt.hist(Precip)



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
