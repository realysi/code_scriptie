from code.matchingdates import matching_dates
from code.files_matchingdates import deepsqueak_files, agouti_rows
from code.agouti.filter import agoutidata_to_dict
from code.read_data import read_csv
from code.deepsqueak.info_data import csv_filenames, timestamps_deepsqueak_to_datetime, datetime_epoch, location_deepsqueak_file
import pandas as pd
import numpy

"""
what do we have:
- matching dates, - files from deepsqueak per location that contain those mathcing dates, -agouti rows that contain that date
"""

def deepsqueak_observations(runtime_agouti, runtime_deepsqueak, path_deepsqueak_data, interval_seconds):
    """
    interval is what amounts to one 1 sighting
    Returns the amount of observations per location {location: [total observations, epoch observations]}
    """
    location_files = deepsqueak_files(runtime_agouti, runtime_deepsqueak, path_deepsqueak_data)

    filenames, total_observations_files, locations, timestamps   = [], [], [], []

    total_length_observations = 0
    for location in location_files.keys():
        files = location_files[location]
        for file in files:
            current_data = read_csv(file)
            start = timestamps_deepsqueak_to_datetime(file)
            observations: list = current_data.df['Box_1'].tolist()
            total_length_observations += len(observations)
            #start with first observation
            current_timestamps = []
            total_observations_now = 0
            end_interval = 0
            for i in range(0, len(observations)):
                    if observations[i] > end_interval:
                        total_observations_now += 1
                        timestamp_observation_epoch = datetime_epoch(start) + observations[i]
                        current_timestamps.append(timestamp_observation_epoch)
                        end_interval = observations[i] + interval_seconds
                    else:
                        continue
            
            timestamps.extend(current_timestamps)
            for j in range(len(current_timestamps)):
                filenames.append(file)
                locations.append(location)
                total_observations_files.append(total_observations_now)

    path = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/data/DS_{interval_seconds}s_{len(timestamps)}obs.csv"

    dictionary = {
        'locationName': locations,
        'filename': filenames,
        'total_observations_file': total_observations_files,
        'timestamps': timestamps
        }
    df = pd.DataFrame(dictionary)
    df = df.sort_values('locationName')
    df.to_csv(path, index=False)
    
    return df

def agouti_observations(runtime_agouti, runtime_deepsqueak, path_agouti_data, interval_seconds):
    locations_rows = agouti_rows(runtime_agouti, runtime_deepsqueak, path_agouti_data)
    locations, filenames, timestamps   = [], [], []

    for location in locations_rows.keys():
        rows: pd.DataFrame = locations_rows[location]
        rows = rows.sort_values('epoch')

        timestamps_location, filename_observation, location  = [], [], []

        if len(rows) > 0:
            end_interval = 0
            for i in rows.index:
                timestamp = float(str(rows.loc[i, 'epoch']))
                if timestamp > end_interval:
                    timestamps_location.append(rows.loc[i, 'epoch'])
                    filename_observation.append(rows.loc[i, 'fileName'])
                    location.append(rows.loc[i, 'locationName'])
                    end_interval = timestamp + interval_seconds
                else:
                    continue

            timestamps.extend(timestamps_location)
            filenames.extend(filename_observation)
            locations.extend(location)
        else:
            continue

    path = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/data/AG_{interval_seconds}s_{len(timestamps)}obs.csv"

    dictionary = {
        'locationName': locations,
        'filename': filenames,
        'timestamps': timestamps
        }
    df = pd.DataFrame(dictionary)
    df = df.sort_values('locationName')
    df.to_csv(path, index=False)
    
    return df


    """print(type(cell_value_firstrow))
            print(f"location: {location}, rows: {len(rows)}")
            print(observations)"""
        
    """for i in range(0, len(rows)):
            if floatrows.loc[i, 'epoch'] > end_interval:
                timestamps_location.append(rows.loc[i, 'epoch'])"""
        #rows.to_csv(f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/agouti/filtered/test_{location}.csv", index=False)
        #first_observation = min(observations)
        #print(f'first observatoin {first_observation}')

    """current_data = read_csv(file)
    start = timestamps_deepsqueak_to_datetime(file)
    observations: list = current_data.df['Box_1'].tolist()
    total_length_observations += len(observations)
    #start with first observation
    current_timestamps = []
    total_observations_now = 0
    end_interval = 0
    for i in range(0, len(observations)):
            if observations[i] > end_interval:
                total_observations_now += 1
                timestamp_observation_epoch = datetime_epoch(start) + observations[i]
                current_timestamps.append(timestamp_observation_epoch)
                end_interval = observations[i] + interval_seconds
            else:
                continue"""