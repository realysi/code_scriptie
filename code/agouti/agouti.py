from code.classes.dataframe_extension import Dataframe
from code.read_data import read_csv
import pandas as pd

"""
This is not set for processing the data of flevopark only (doesn't use ID but locationName)!!!
"""

def process_observation_data(path_observation_csv: str, location_dataset: str) -> Dataframe:
    """
    processes the data of the observation sheet by filtering on Rattus norvegic, keeping relevant columns, adding UTC
    and epoch time to dataset and finally writing a new csv file containing all this processed data.
    return path to that newly written csv file.
    """
    data: Dataframe = read_csv(path_observation_csv)
    data.keep_relevant_columns(['deploymentID', 'sequenceID', 'scientificName', 'timestamp'])
    data.select_rows_by_columnvalue(columnname='scientificName', columnvalue='Rattus norvegicus')
    data.add_utc(columnname_timestamp='timestamp', location_data=location_dataset, desired_name_column='UTC timestamp') 
    data.add_epoch(columnname_timestamp='UTC timestamp')
    return data


def add_deployment_data(path_deploysments: str, path_observations_csv: str, location_dataset: str) -> Dataframe:
    """
    data of deployments.csv gets added to filtered observations data (New columns = 'longitude', 'latitude', 'locationName', 'cameraID').
    Result gets written to new csv file, return the path to that csv file.
    """
    data: Dataframe = read_csv(path_deploysments)
    data.keep_relevant_columns(['deploymentID', 'longitude', 'latitude', 'locationName', 'cameraID'])
    data_observation = process_observation_data(path_observations_csv, location_dataset)
    data_observation.pair_sheets_by_columnvalue(data, "deploymentID", ['longitude', 'latitude', 'locationName', 'cameraID'])
    return data_observation


def add_media_data(path_media: str, path_observations_csv: str, path_deployments: str, location_dataset) -> Dataframe:
    """
    links the data of the observation sheet to that of the media sheet. The media sheet gets searched by the sequenceID
    to find the relevant filename, which contains information about the ID of the camera. The data gets written to a new csv file.
    Return path to that new csv file.
    """
    data_media = read_csv(path_media)
    data_media.keep_relevant_columns(['sequenceID', 'fileName'])
    data_observations = add_deployment_data(path_deployments, path_observations_csv, location_dataset)
    data_observations.pair_sheets_by_columnvalue(data_media, 'sequenceID', ['fileName'])
    return data_observations


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


def filter_data_agouti(path_observations: str, path_media: str, path_deployments: str, location_dataset: str) -> Dataframe:
    """
    Contains functions above.
    filters observations data, links observation and media data and writes it to new csv file.
    """
    filtered_data = add_media_data(path_media, path_observations, path_deployments, location_dataset)
    total_runningtime(path_deployments, location_dataset)

    path_final_data = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/agouti/final/data_{location_dataset}.csv"
    filtered_data.df = filtered_data.df.sort_values('locationName')
    filtered_data.df.to_csv(path_final_data, index=False)

    return filtered_data


def agoutidata_to_dict(data: Dataframe) -> dict[str, pd.DataFrame]: #wordt data: Dataframe maar nu even tijd besparen
    """
    Return dictionary that is ordened by id and dataframes {ID: pd.Dataframe}
    for artis data: ID column
    for Flevopark data: locationName column
    """
    dict_data = {}
    all_locations = list(set(data.df['locationName'].tolist())) #all unique locationnames (flevopark_1, flevopark_2 etc)
    for j in all_locations:
        rows: pd.DataFrame = data.df.loc[data.df['locationName'] == j]
        if rows['locationName'].str.contains('flevopark').any():
            dict_data.update({j: rows})
    return dict_data


def data_agouti(path_observations: str, path_media: str, path_deployments: str, location_dataset: str):
    """
    Main functions of this file
    Filters the agouti data, writes csv file with specific information that can be used later on
    """
    filtered_data = filter_data_agouti(path_observations, path_media, path_deployments, location_dataset)
    data = agoutidata_to_dict(filtered_data)
    return data


def data_aougti_test(path_filtered_data):
    data = agoutidata_to_dict(path_filtered_data)
    return data

