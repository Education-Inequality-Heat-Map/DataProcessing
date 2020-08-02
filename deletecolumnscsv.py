# This program takes in the merged csv file, merged.csv, generated 
# from countyNames.csv and countyStats.csv. It then keeps the 
# necessary columns and deletes the others. 

import pandas as pd
file = pd.read_csv("merged.csv")
keep_col = ['Population', '< 18', 'African American', 'American Indian/ Alaskan Native', 'Asian', 'Native Hawaiian/ Other Pacific Islander', 'Hispanic', 'Non-hispanic white', 'Household Income', '% Free Lunch'] 
cleaned_file = file[keep_col]
cleaned_file.to_csv("cleanedData.csv", index = False)
