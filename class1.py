import math

#read the csv file and converted the data in a list
import csv 

with open("C105/class1.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

#removed the first row i.e. headings for columns
data.pop(0)

total_entries = len(data)

total_marks = 0

for item in data:
    total_marks = total_marks + float(item[1])

mean = total_marks / total_entries
print("Average of the marks for class 1 is: ", mean)

#scatter plot

import pandas as pd
import plotly.express as px

df = pd.read_csv("C105/class1.csv")

fig = px.scatter(df, x= "Student Number", y = "Marks")

fig.update_layout(shapes = [dict(type = 'line', x0 = 0 , y0 = mean, x1 = total_entries, y1 = mean)])

#fig.show()

#standard deviation 
# mean 
# datapoint - mean 
# (datapoint - mean)^2
#sum all the previous entries 
# divide by total number of marks enteries 
# take the square root
marks = []
for item in data: 
    mark = int(item[1])
    marks.append(mark)

squared_list = []
for number in marks:
    a = number - mean
    a= a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum + i

result = sum / total_entries

standard_deviation = math.sqrt(result)
print("the standard deviation for class 1 is: ", standard_deviation)

