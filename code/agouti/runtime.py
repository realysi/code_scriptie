from code.classes.dataframe_extension import Dataframe
from code.read_data import read_csv
import pandas as pd

def total_runningtime(path_deployments, location_dataset):
    """
    Calculates how much time (seconds) every camera recorderd (still got to add for the same locaitons) and displays the dates at which
    it recorded. Writes the data to a csv file.
    """
    data_deployments = read_csv(path_deployments)
    data_deployments.keep_relevant_columns(['deploymentID', 'start', 'end', 'locationName', 'longitude', 'latitude'])
    data_deployments.df = data_deployments.df.dropna()
    data_deployments.add_utc('start', location_data="flevopark", desired_name_column='start_utc')
    data_deployments.add_utc('end', location_data="flevopark", desired_name_column='end_utc')
    data_deployments.calculate_difference_datetime('start_utc', 'end_utc', 'running_time(sec)')
    data_deployments.keep_relevant_columns(['deploymentID', 'start_utc', 'end_utc', 'locationName', 'running_time(sec)', 'longitude', 'latitude' ])
    data_deployments.df = data_deployments.df.sort_values('locationName')
    path_running_times = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/agouti/runtime/runtime_{location_dataset}.csv"
    data_deployments.df.to_csv(path_running_times, index=False)
    return data_deployments

