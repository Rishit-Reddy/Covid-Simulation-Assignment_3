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


    # Filter by contries

    s_df = df[df['country'].isin(countries)]
    s_df['sample_population'] = (s_df['population'] / sample_ratio).astype(int)
    s_df['s_less_5'] = (s_df['sample_population'] * s_df['less_5'] / 100).astype(int)
    s_df['s_5_to_14'] = (s_df['sample_population'] * s_df['5_to_14'] / 100).astype(int)
    s_df['s_15_to_24'] = (s_df['sample_population'] * s_df['15_to_24'] / 100).astype(int)
    s_df['s_25_to_64'] = (s_df['sample_population'] * s_df['25_to_64'] / 100).astype(int)
    s_df['s_over_65'] = (s_df['sample_population'] * s_df['over_65'] / 100).astype(int)
    s_df=s_df.drop(['population','median_age'],axis=1)
    s_df['person_id']=0
    s_df.set_index('person_id',drop=False)




    return s_df
    


def run(countries_csv_name, countries, sample_ratio, start_date, end_date):
    sample_population = sample_creation(countries_csv_name, countries, sample_ratio)
    print(sample_population)

