import pandas as pd
import os
import glob
import numpy as np

# Folder containing CSV files
folder = 'temperatures'
files = glob.glob(os.path.join(folder, '*.csv'))

# Combine all CSVs
all_data = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Convert date column to datetime if exists
all_data['Date'] = pd.to_datetime(all_data['Date'])

# Define seasons
def get_season(month):
    if month in [12, 1, 2]:
        return 'Summer'
    elif month in [3, 4, 5]:
        return 'Autumn'
    elif month in [6, 7, 8]:
        return 'Winter'
    else:
        return 'Spring'

all_data['Season'] = all_data['Date'].dt.month.apply(get_season)

# Seasonal Average
seasonal_avg = all_data.groupby('Season')['Temperature'].mean()
with open('average_temp.txt', 'w') as f:
    for season, avg in seasonal_avg.items():
        f.write(f"{season}: {avg:.1f}°C\n")

# Temperature range per station
station_stats = all_data.groupby('Station')['Temperature'].agg(['max','min','std'])
station_stats['range'] = station_stats['max'] - station_stats['min']
max_range = station_stats['range'].max()
largest_range_stations = station_stats[station_stats['range'] == max_range]

with open('largest_temp_range_station.txt', 'w') as f:
    for station, row in largest_range_stations.iterrows():
        f.write(f"Station {station}: Range {row['range']:.1f}°C (Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n")

# Temperature stability
min_std = station_stats['std'].min()
max_std = station_stats['std'].max()
most_stable = station_stats[station_stats['std'] == min_std]
most_variable = station_stats[station_stats['std'] == max_std]

with open('temperature_stability_stations.txt', 'w') as f:
    for station, row in most_stable.iterrows():
        f.write(f"Most Stable: Station {station}: StdDev {row['std']:.1f}°C\n")
    for station, row in most_variable.iterrows():
        f.write(f"Most Variable: Station {station}: StdDev {row['std']:.1f}°C\n")

