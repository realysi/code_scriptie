import datetime
from .reading_data_voorbeelden import read_data
import pandas as pd

def hours_to_seconds(dataframe: pd.DataFrame, columnname):
    """
    This function will turn time stemps (hh:mm:ss) in total amount of seconds
    This will enable me to calculate different time intervals for the times
    """
    #audio_df: pd.DataFrame = read_data(link_data) #audio_df could become just a df depending on how the data will look
    for i in dataframe.index: 
        time = dataframe.loc[i, columnname] #, "tijd" could be any column name
        hours, minutes, seconds = time.split(":") #works, but vsc just gives red line
        total_seconds = int(datetime.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds)).total_seconds())
        dataframe.loc[i, columnname] = total_seconds #change hh:mm:ss to total seconds in the df
    return dataframe

def seconds_to_hours(dataframe: pd.DataFrame, columnname):
    for i in dataframe.index:
        time_seconds = dataframe.loc[i, columnname]
        time = datetime.timedelta(seconds = time_seconds) #works, but vsc just gives red line
        dataframe.loc[i, columnname] = time #works, but vsc just gives red line
    return dataframe

def dates_to_seconds(dataframe, columnname): #columnname wordt iets van data
    for i in dataframe.index:
        date = dataframe.loc[i, columnname]
        day, month, year = date.split("/")
        datastamp = datetime.datetime(year=int(year), month=int(month), day=int(day))
        total_seconds_1970 = datastamp.timestamp()
        dataframe.loc[i, columnname] = total_seconds_1970
    return dataframe

def select_row_species(dataframe, columnname, species):
    return dataframe.loc[dataframe[columnname] == species]

def select_ID(dataframe, columnname, ID):
    return dataframe.loc[dataframe[columnname] == ID]
