import  re
import csv
import pandas as pd
import matplotlib.pyplot as plt
from functions import *

#TODO: add to this program
    # clean the data using your functions 
    # write the cleaned data into a new csv file (optional but helpful for next step)
    # put the cleaned data into a dataframe
    #    - use your cereal_analysis python file as a template to read from csv

with open('alumni_anonymized.csv') as records:
    reader = csv.reader(records)
    entries = [] #this will store the rows in dictionary form
    next(reader)  #skip header
    count = 0
    for row in reader:
        new_row = dict()
        new_row['Last_Name'] = row[0]
        new_row['Id'] = row[3].strip()
        birth = row[4].strip()
        new_row['Birth_Year'] = get_birth_year(birth)
        year_text= row[1].strip()

        match = re.search(r'\d{4}', year_text)

        if match:
            new_row['Exit_Year'] = match.group()
        else:
            year = remove_text(year_text)
            if is_four_digits(year):
                new_row['Exit_Year'] = year
            else:
                new_row['Exit_Year'] = add_digits(year)

        
        if count< 500:
            print(row)
            print(row[0])
                
        entries.append(new_row)
        count+=1

with open('alumni_clean.csv', 'w', newline='') as new_file:
    csv_writer = csv.DictWriter(new_file,fieldnames=['Id','Last_Name','Exit_Year', 'Birth_Year'])
    csv_writer.writeheader()
    csv_writer.writerows(entries)

import pandas as pd

df = pd.read_csv("alumni_clean.csv")

# convert to numbers
df["Birth_Year"] = pd.to_numeric(df["Birth_Year"], errors="coerce")
df["Exit_Year"] = pd.to_numeric(df["Exit_Year"], errors="coerce")
df["Id"] = pd.to_numeric(df["Id"], errors="coerce")

# compute age
df["Age_at_Exit"] = df["Exit_Year"] - df["Birth_Year"]

#filtering
df = df[(df["Age_at_Exit"] >= 7) & (df["Age_at_Exit"] <= 24)]
df = df[(df["Exit_Year"] >= 1880) & (df["Exit_Year"] <= 1984)]
df = df[(df["Birth_Year"] >= 1857) & (df["Birth_Year"] <= 1980)]

# set index
df = df.set_index("Id")
df.to_csv("alumni_clean.csv")



#plot of Age of Exit
df["Age_at_Exit"].plot(kind="hist", bins=10)
plt.title("Distribution of Age at Exit")
plt.xlabel("Age at Exit")
plt.ylabel("Number of Cadets")
plt.show()








