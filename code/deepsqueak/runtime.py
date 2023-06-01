from code.deepsqueak.functions import csv_filenames, location_deepsqueak_file, timestamps_deepsqueak_to_datetime, datetime_to_epoch
import datetime
from code.read_data import read_csv
import pandas as pd
from code.classes.dataframe_extension import Dataframe

def runtime(path_folder, location_data):
    """
    Creates a csv(runtime_flevopark) with information of each recording. LocationName | start_recording | end_recording | runtime (seconds)
    """
    starttimes, endtimes, runtime, location = [], [], [], []
    files = csv_filenames(path_folder)
    for file in files:
        current_data = read_csv(file)
        observations: list = current_data.df['Box_1'].tolist()
        last_observation = round(max(observations))
        current_location = location_deepsqueak_file(file)
        start = timestamps_deepsqueak_to_datetime(file)
        end = start + datetime.timedelta(seconds=last_observation)
        run_time = abs(datetime_to_epoch(start) - datetime_to_epoch(end))
        starttimes.append(start)
        endtimes.append(end)
        runtime.append(run_time)
        location.append(current_location)

    data = {'locationName': location, 'start': starttimes, 'end': endtimes, 'runtime (sec)': runtime} 
    df = pd.DataFrame(data)
    df = df.sort_values('locationName')
    path = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/deepsqueak/runtime_{location_data}.csv"
    df.to_csv(path, index=False)
    data = Dataframe(df)
    return data

def total_runtime(pddataframe):
    """
    returns dictionary with total runtime per location and total recordings. {flevopark_1: [3 days 1:36:56, 52}.
    """
    data = Dataframe(pddataframe)
    data = data.total_runtime_per_location()
    print(data)
    return data