import numpy as np
import pandas as pd
from helper import create_plot
from sim_parameters import TRASITION_PROBS, HOLDING_TIMES

#Can this be a seperate module? Just to escape plagiarism
def sample_creation(countries_csv_name, countries, sample_ratio):
    '''
    Parameters:
        - countries_csv_name: The file name of the CSV containing country data.
        - countries: A list of countries to filter the data.
        - sample_ratio: The ratio used to calculate the sample size.

    Returns:
        - sample_population: A dictionary containing the sample size for each country, categorized by age group.
    '''

    # Initialize a dictionary to store sample size

    # Reading CSV File
    df = pd.read_csv(countries_csv_name)

    # Filter by countries
    country_specific_df = df[df['country'].isin(countries)]
    

    columns_list = ['person_id', 'age_group_name', 'country']
    sample_population = pd.DataFrame(columns=columns_list)

    for index, row in country_specific_df.iterrows():
        temp_dict = dict()

        sample_size = int(row['population'] / sample_ratio)
        temp_dict['less_5'] = int((row['less_5'] * sample_size) / 100)
        temp_dict['5_to_14'] = int((row['5_to_14'] * sample_size) / 100)
        temp_dict['15_to_24'] = int((row['15_to_24'] * sample_size) / 100)
        temp_dict['25_to_64'] = int((row['25_to_64'] * sample_size) / 100)
        temp_dict['over_65'] = int((row['over_65'] * sample_size) / 100)

        
        for age_group, value in temp_dict.items(): 
            
            temp_list = [{"person_id":0, "age_group_name":age_group, "country": row['country']} for _ in range(value)]
            sample_population = pd.concat([sample_population, pd.DataFrame(temp_list)], ignore_index=True)
    return sample_population


def run(countries_csv_name, countries, sample_ratio, start_date, end_date):
    sample_population = sample_creation(countries_csv_name, countries, sample_ratio)
    print(sample_population)


