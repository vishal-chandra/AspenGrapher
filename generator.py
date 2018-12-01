import pandas as pd
import random

for i in range(1, 32):
    
    courses = ['Course 1', 'Course 2', 'Course 3', 'Course 4', 'Course 5', 'Course 6']
    nums = random.sample(range(80, 100), 6)
    frame = pd.DataFrame({'Description' : courses, 'Term Performance' : nums})

    csv_path = 'CSVs/12-' + str(i) + '.csv'
    frame.to_csv(csv_path)
