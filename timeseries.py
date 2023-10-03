
import pandas as pd
import random

import pandas as pd
import random

def create_sample_dataframe():
    # Initialize an empty DataFrame
    sample_df = pd.DataFrame(columns=['person_id', 'age_group_name', 'country'])

    # Define the possible values for age_group_name and country
    age_groups = ["less_5", "5_to_14", "15_to_24", "25_to_64", "over_65"]
    countries = ["S", "A", "J"]

    # Generate 50 random records
    for i in range(167):
        person_id = 0  # Unique person_id for each record
        age_group = random.choice(age_groups)  # Randomly select an age group
        country = random.choice(countries)  # Randomly select a country

        # Create a temporary DataFrame for the current record
        record_df = pd.DataFrame({'person_id': [person_id], 'age_group_name': [age_group], 'country': [country]})

        # Concatenate the temporary DataFrame with the sample_df
        sample_df = pd.concat([sample_df, record_df], ignore_index=True)

    return sample_df

# Create the sample DataFrame
sample_dataframe = create_sample_dataframe()

def create_timeseries(sample_df, start_date, end_date):
    # Create an empty DataFrame with the desired columns
    columns = ['person_id', 'age_group_name', 'country', 'date', 'state', 'staying_days']
    timeseries_df = pd.DataFrame(columns=columns)

    # Generate date range from start_date to end_date
    date_range = pd.date_range(start=start_date, end=end_date)

    # Repeat each row in sample_df for each date in the date range
    for date in date_range:
        timeseries_df = pd.concat([timeseries_df, sample_df.assign(date=date)], ignore_index=True)

    # Initialize the 'state' and 'staying_days' columns as empty
    timeseries_df['state'] = ''
    timeseries_df['staying_days'] = ''

    return timeseries_df

# Create the sample DataFrame
sample_dataframe = create_sample_dataframe()

# Define the start and end dates
start_date = '2021-04-01'
end_date = '2022-04-30'

# Create the time-series DataFrame
timeseries_dataframe = create_timeseries(sample_dataframe, start_date, end_date)

# Print the first few records to check
print(timeseries_dataframe)