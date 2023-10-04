
import pandas as pd

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
