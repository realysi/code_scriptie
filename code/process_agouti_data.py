from code.classes.dataframe_extension import Dataframe
from code.read_data import read_csv
import pandas as pd

"""
This programm summarized:
Agouti (neural network) processes wildlife camera data and returns 3 csv files: media.csv, observations.csv and deployments.csv
observations.csv contains 
"""
unfiltered_observations = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/observations.csv"
unfiltered_media = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv"

def process_observation_data(path_observation_csv: str) -> str:
    """
    processes the data of the observation sheet by filtering on Rattus norvegic, keeping relevant columns, adding UTC
    and epoch time to dataset and finally writing a new csv file containing all this processed data.
    """
    data = read_csv(path_observation_csv)
    data.keep_relevant_columns(['deploymentID', 'sequenceID', 'scientificName', 'timestamp'])
    data.select_rows_by_columnvalue(columnname='scientificName', columnvalue='Rattus norvegicus')
    data.add_utc(columnname_timestamp='timestamp') 
    data.add_epoch(columnname_timestamp='UTC timestamp')
    #data.interval(columnname_timestamp='epoch', interval_minutes=2)
    path_filtered_observations = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/filtered_observation.csv"
    data.df.to_csv(path_filtered_observations, index=False)
    return path_filtered_observations

def link_to_deployments(path_filtered_observation, path_deployments):
    pass

def deployments(path_deploysments_csv, path_filtered_observations):
    data = read_csv(path_deploysments_csv)
    data.keep_relevant_columns(['deploymentID', 'longitude', 'latitude', 'locationName', 'cameraID'])
    data_observation = read_csv(path_filtered_observations)
    data_observation.pair_sheets_by_columnvalue(data, "deploymentID", ['longitude', 'latitude', 'locationName', 'cameraID'])
    path_deployments_linked = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/deployments_linked.csv"
    data_observation.df.to_csv(path_deployments_linked, index=False)
    return path_deployments_linked

def link_observation_media(path_filtered_observations: str, path_media: str) -> str:
    """
    links the data of the observation sheet to that of the media sheet. The media sheet gets searched by the sequenceID
    to find the relevant filename, which contains information about the ID of the camera. The data gets written to a new csv file.
    """
    data_media = read_csv(path_media)
    data_media.keep_relevant_columns(['sequenceID', 'fileName'])
    data_observations = read_csv(path_filtered_observations)
    data_observations.pair_observations_media(data_media)
    path_linked_media_observations = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/linked_media&observations_.csv"
    data_observations.df.to_csv(path_linked_media_observations, index=False)
    return path_linked_media_observations



def add_id_name(linked_data: Dataframe) -> Dataframe:
    """
    Adds ID column to data
    """
    all_id_names = []
    for i in linked_data.df.index:
        name = str(linked_data.df.loc[i, 'fileName'])
        if 'wildlifecamera1' in name:
            name = name.split("_202")[0]
            name = name.split("-")[1]
        all_id_names.append(name)
    linked_data.df.insert(len(linked_data.df.columns), "ID", all_id_names)
    return linked_data


def data_agouti(path_observations: str, path_media: str) -> Dataframe:
    """
    Contains functions above.
    filters observations data, links observation and media data and writes it to new csv file.
    """
    filtered_observations = process_observation_data(path_observations)
    linked_data = link_observation_media(filtered_observations, path_media)
    processed_agouti_data = add_id_name(linked_data)

    path_processed_data = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/processed_agouti_data.csv"
    processed_agouti_data.df.to_csv(path_processed_data)
    return processed_agouti_data


def agoutidata_to_dict(path: str) -> dict: #wordt data: Dataframe maar nu even tijd besparen
    """
    Return dictionary that is ordened by id and dataframes {ID: pd.Dataframe}
    """
    dict_data = {}
    data = read_csv(path)
    all_id_names = list(set(data.df['ID'].tolist())) #all unique id names

    for j in all_id_names:
        rows: pd.DataFrame = data.df.loc[data.df['ID'] == j]
        if rows['ID'].str.contains('artis').any():
            dict_data.update({j: rows})
    return dict_data

