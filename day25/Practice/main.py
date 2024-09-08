# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
'''
import csv

with open('weather-data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] !='temp':
            temperatures.append(int(row[1]))
    print(temperatures) '''

import pandas

data = pandas.read_csv('weather-data.csv')
print(type(data["temp"]))
print(type(data))

data_dictionary = data.to_dict()
print(data_dictionary)

temp_list = data['temp'].to_list()
print(temp_list)

average_temp = sum(temp_list) / len(temp_list)
print("average temperature: ", average_temp)
print('Mean temperature: ', data['temp'].mean())
print("Maximum temperature: ", data['temp'].max())

#Getting data in rows:

print(data[data.day == "Monday"])
print("Day with the highest temperature: \n", data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
monday_temperature = int(monday.temp)
monday_temp_F = monday_temperature * 9/5 + 32
print("Monday temperature in fahrenheit: ", monday_temp_F)


'''Creating a dataframe from scratch'''
data_dict = {
    'student': ["Amy", "Jenny", "Mark"],
    "scores": [90, 56, 87]
}

data = pandas.DataFrame(data_dict)
data.to_csv("student_data.csv")
print(data)