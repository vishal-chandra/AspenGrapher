import os
import pandas as pd

dates = []
grades = {}

first_iteration = True
for csv in os.scandir('CSVs'):

    data = pd.DataFrame.from_csv(csv.path)
    date = csv.path.split('/')[1].split('.')[0].split(' ')[0]
    dates.append(date)

    if first_iteration:
        for index, row in data.iterrows():
            # create a new key value pair in grades with key as course name and value as a list of ints
            # splitting at space and taking first value to disregard letter 
            grades[row['Description']] = [row['Term Performance'].split(' ')[0]]
        first_iteration = False
    
    else:
        for index, row in data.iterrows():
            # add grade to corresponding list
            grades[row['Description']].append(row['Term Performance'].split(' ')[0])

print(dates)
print(grades)