from code.classes.dataframe_extension import Dataframe
from code.read_data import read_csv
import pandas as pd

"""
This is not set for processing the data of flevopark only (doesn't use ID but locationName)!!!

Agouti (neural network) processes wildlife camera data and returns 3 csv files: media.csv, observations.csv and deployments.csv
observations.csv contains: 'deploymentID', 'sequenceID', 'scientificName', 'timestamp'
media.csv contains: sequenceID, fileName
deployments.csv contains: 'deploymentID', 'longitude', 'latitude', 'locationName', 'cameraID'

Steps of the program:
1. observation data gets filtered; Drops all but the 'deploymentID', 'sequenceID', 'scientificName', 'timestamp' columns
, adds column where the timestamp gets converted to UTC and epoch time --> result gets written to csv file to work further with (and save in case of data loss)
2. data of deployments.csv gets added to filtered observations data (New columns = 'longitude', 'latitude', 'locationName', 'cameraID')
3. 
"""

def process_observation_data(path_observation_csv: str, location_dataset: str) -> str:
    """
    processes the data of the observation sheet by filtering on Rattus norvegic, keeping relevant columns, adding UTC
    and epoch time to dataset and finally writing a new csv file containing all this processed data.
    return path to that newly written csv file.
    """
    data: Dataframe = read_csv(path_observation_csv)
    data.keep_relevant_columns(['deploymentID', 'sequenceID', 'scientificName', 'timestamp'])
    data.select_rows_by_columnvalue(columnname='scientificName', columnvalue='Rattus norvegicus')
    data.add_utc(columnname_timestamp='timestamp', location_data=location_dataset) 
    data.add_epoch(columnname_timestamp='UTC timestamp')
    path_filtered_observations = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/{location_dataset}_filtered_observation.csv"
    data.df.to_csv(path_filtered_observations, index=False)
    return path_filtered_observations


def add_deployment_data(path_deploysments: str, path_filtered_observations: str, location_dataset: str) -> str:
    """
    data of deployments.csv gets added to filtered observations data (New columns = 'longitude', 'latitude', 'locationName', 'cameraID').
    Result gets written to new csv file, return the path to that csv file.
    """
    data: Dataframe = read_csv(path_deploysments)
    data.keep_relevant_columns(['deploymentID', 'longitude', 'latitude', 'locationName', 'cameraID'])
    data_observation = read_csv(path_filtered_observations)
    data_observation.pair_sheets_by_columnvalue(data, "deploymentID", ['longitude', 'latitude', 'locationName', 'cameraID'])
    path_deployments_linked = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/{location_dataset}_+deploymentdata.csv"
    data_observation.df.to_csv(path_deployments_linked, index=False)
    return path_deployments_linked


def add_media_data(path_media: str, path_addeddeployment: str, location_dataset) -> str:
    """
    links the data of the observation sheet to that of the media sheet. The media sheet gets searched by the sequenceID
    to find the relevant filename, which contains information about the ID of the camera. The data gets written to a new csv file.
    Return path to that new csv file.
    """
    data_media = read_csv(path_media)
    data_media.keep_relevant_columns(['sequenceID', 'fileName'])
    data_observations = read_csv(path_addeddeployment)
    data_observations.pair_sheets_by_columnvalue(data_media, 'sequenceID', ['fileName'])
    #data_observations.pair_observations_media(data_media)
    path_linked_media_observations = f"/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/{location_dataset}+mediadata.csv"
    data_observations.df.to_csv(path_linked_media_observations, index=False)
    return path_linked_media_observations


def filter_data_agouti(path_observations: str, path_media: str, path_deployments: str, location_dataset: str) -> str:
    """
    Contains functions above.
    filters observations data, links observation and media data and writes it to new csv file.
    """
    filtered_observations = process_observation_data(path_observations, location_dataset)
    add_deploymentdata = add_deployment_data(path_deployments, filtered_observations, location_dataset)
    add_mediadata = add_media_data(path_media, path_addeddeployment=add_deploymentdata, location_dataset=location_dataset)
    return add_mediadata


def agoutidata_to_dict(path: str): #wordt data: Dataframe maar nu even tijd besparen
    """
    Return dictionary that is ordened by id and dataframes {ID: pd.Dataframe}
    for artis data: ID column
    for Flevopark data: locationName column
    """
    dict_data = {}
    data = read_csv(path)
    all_id_names = list(set(data.df['locationName'].tolist())) #all unique locationnames (flevopark_1, flevopark_2 etc)
    for j in all_id_names:
        rows: pd.DataFrame = data.df.loc[data.df['locationName'] == j]
        if rows['locationName'].str.contains('flevopark').any():
            dict_data.update({j: rows})
    return dict_data


def data_agouti_final(path_observations: str, path_media: str, path_deployments: str, location_dataset: str):
    """
    Main functions of this file
    """
    path = filter_data_agouti(path_observations, path_media, path_deployments, location_dataset)
    data = agoutidata_to_dict(path)
    return data


def data_aougti_test(path_filtered_data):
    data = agoutidata_to_dict(path_filtered_data)
    return data





def add_id_name(linked_data: Dataframe) -> Dataframe:
    """
    Adds ID column to data
    This functions only gets used for the Artis files, as those do not have relevant information in the locationName column
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