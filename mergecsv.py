# This program takes in two csv files, countyStats.csv 
# and countyNames.csv and merges them based on FIPS.

import pandas as pd

# read the files
file1 = pd.read_csv('countyStats.csv')
file2 = pd.read_csv('countyNames.csv')

# merge the files
file3 = pd.merge(file1, file2, on = 'FIPS')
file3.set_index('FIPS', inplace = True)

# write to a new csv file
file3.to_csv('merged.csv')
