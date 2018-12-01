import os
import pandas as pd
import matplotlib.pyplot as plt

def plot(test):
    dates = []
    grades = {}

    first_iteration = True
    for csv in os.scandir('CSVs'):

        data = pd.DataFrame.from_csv(csv.path) 

        date = csv.path.split('/')[1].split('.')[0] #CSVs/12-12-12.csv -> 12-12-12
        dates.append(date)

        # the first file will be used as the template to create the dict's key value pairs
        if first_iteration:
            for index, row in data.iterrows():
                if not test:
                    # create a new key value pair in grades with key as course name and value as a list of ints
                    # splitting at space and taking first value to disregard letter 
                    grades[row['Description']] = [row['Term Performance'].split(' ')[0]]
                else:   
                    grades[row['Description']] = [row['Term Performance']] # test data has no letters
            first_iteration = False
        
        # all other files can be added staright to dict
        else:
            for index, row in data.iterrows():
                if not test:
                    # add grade to corresponding list
                    # splitting at space and taking first value to disregard letter 
                    grades[row['Description']].append(row['Term Performance'].split(' ')[0])
                else:
                    grades[row['Description']].append(row['Term Performance']) # test data has no letters

    legend = []
    for key in grades:
        plt.plot(dates, grades[key])
        legend.append(key)
    plt.legend(legend, loc='upper left')
    plt.show()

plot(test=True)