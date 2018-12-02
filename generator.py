import pandas as pd
import random

for i in range(1, 16):
    
    courses = ['Course 1', 'Course 2', 'Course 3', 'Course 4', 'Course 5', 'Course 6']
    nums = random.sample(range(80, 100), 6)

    # creates a data frame with two columns, each using one of the respective lists above for the values
    frame = pd.DataFrame({'Description' : courses, 'Term Performance' : nums})

    # name each test datapoint with a date in december
    csv_path = 'CSVs/12-' + str(i) + '.csv'
    frame.to_csv(csv_path)
