from .classes.data import Data
from code.read_data import read_csv
import pandas as pd

unfiltered_observations = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/observations.csv"
unfiltered_media = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Agouti/Artis/media.csv"


def process_observation_data(path: str):
    data = read_csv(path)
    data.keep_relevant_columns(['sequenceID', 'timestamp', 'scientificName'])
    data.select_rows_by_columnvalue(columnname='scientificName', columnvalue='Rattus norvegicus') #select only rows with brown rat observations

    data.add_utc(columnname_timestamp='timestamp') #3: Time to utc
    data.add_epoch(columnname_timestamp='utc') #4: Time to epoch
    data.interval(columnname_timestamp='epoch', interval_minutes=2) #add intervals
    path_filtered_results = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/filtered_observation.csv"
    data.df.to_csv(path_filtered_results) #save dataframe
    return path_filtered_results

def link_observation_media(path_filtered_observations, path_media):
    data_media = read_csv(path_media)
    data_media.keep_relevant_columns(['sequenceID', 'fileName'])
    data_observations = read_csv(path_filtered_observations)
    data_observations.pair_observations_media(data_media)
    path_linked_data = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/results/linked_results.csv"
    data_observations.df.to_csv(path_linked_data) #save dataframe
    return path_linked_data

def data_agouti(path_observations, path_media):
    filtered_observations = process_observation_data(path_observations)
    path_linked_data = link_observation_media(filtered_observations, path_media)
    return path_linked_data
