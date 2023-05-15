import pandas as pd
import datetime
import pytz
from calendar import monthrange


"""
Class to add functions to pandas dataframe
"""

class Dataframe:
    def __init__(self, dataframe):
        self.df: pd.DataFrame = dataframe
    
    def select_rows_by_columnvalue(self, columnname, columnvalue):
        """
        returns the rows of the dataframe which have a certain columnvalue for column x
        """
        self.df = self.df.loc[self.df[columnname] == columnvalue]
        return self
    
    def add_utc(self, columnname_timestamp, location_data: str):
        """
        Turns the time from localized Amsterdam time to UTC time.
        """
        times = []
        for i in self.df.index: 
            timestamp = str(self.df.loc[i, columnname_timestamp]) #2022-08-03T12:00:28+01:00
            date, time = timestamp.split('T') #-> date = 2022-08-03 time = 12:00:28+01:00
            time = time.split('+')[0] #time = 12:00:28
            year, month, day = date.split("-") #format in xlsx is d/m/y but it became y-m-d ??
            hours, minutes, seconds = time.split(":")
            datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
            if location_data.lower() == 'artis':
                datetime_object = pytz.timezone('Europe/Amsterdam').localize(datetime_object)
                datetime_object = datetime_object.astimezone(pytz.utc)
            else:
                if int(hours) - 1 < 0:
                    if int(day) - 1 == 0:
                        num_days = monthrange(int(year), int(month) - 1)[1] # num_days = 28
                        datetime_object = datetime_object.replace(month= int(month) - 1, day=num_days, hour=23)
                    else:
                        datetime_object = datetime_object.replace(day=int(day) - 1, hour=23)
                else:
                    datetime_object = datetime_object.replace(hour=int(hours) -1)
            times.append(datetime_object)
        self.df.insert(len(self.df.columns), "UTC timestamp", times)
        return self
    
    def keep_relevant_columns(self, columnnames: list[str]):
        column_headers = []
        for column_header in self.df.columns:
            column_headers.append(column_header)
        for i in column_headers:
            if i not in columnnames:
                self.df = self.df.drop(columns=[i])
        return self

    def add_epoch(self, columnname_timestamp):
        """
        Turns time into epoch time
        Note!! Time already got to be a datetime.datetime object for this to work
        """
        epoch_times = []
        for i in self.df.index: 
            datestamp: datetime.datetime = self.df.loc[i, columnname_timestamp]
            epoch = datestamp.timestamp()
            epoch_times.append(epoch)
        self.df.insert(len(self.df.columns), "epoch", epoch_times)
        return self
    
 

    def interval(self, columnname_timestamp, interval_minutes):
        """
        Adds an interval (only tested on epoch time) to timestamps.
        """
        seconds = interval_minutes * 60
        datestamps_min = []
        datestamps_max = []
        for i in self.df.index: 
            datestamp = self.df.loc[i, columnname_timestamp]
            datestamp_max = datestamp + seconds
            datestamps_max.append(datestamp_max)
            datestamp_min = datestamp - seconds
            datestamps_min.append(datestamp_min)
        self.df.insert(len(self.df.columns), f"min{interval_minutes}_interval", datestamps_min)
        self.df.insert(len(self.df.columns), f"max{interval_minutes}_interval", datestamps_max)
        return self

    def pair_observations_media(self, data_media):
        filenames = []
        for i in self.df.index:
            sequenceID = self.df.loc[i, 'sequenceID']
            rows: pd.DataFrame = data_media.df.loc[data_media.df['sequenceID'] == sequenceID]
            first_row = rows.iloc[0]
            filename_firstrow = first_row.loc['fileName']
            filenames.append(filename_firstrow)
        self.df.insert(len(self.df.columns), "fileName", filenames)
        return self.df

    def pair_sheets_by_columnvalue1(self, data_other_sheet):
        filenames = []
        for i in self.df.index:
            deploymentID = self.df.loc[i, 'deploymentID']
            rows: pd.DataFrame = data_other_sheet.df.loc[data_other_sheet.df['depolymentID'] == deploymentID]
            """first_row = rows.iloc[0]
            filename_firstrow = first_row.loc['fileName']
            filenames.append(filename_firstrow)"""
            longitude = rows.loc['longitude']
        self.df.insert(len(self.df.columns), "fileName", filenames)
        return self.df

    def pair_sheets_by_columnvalue(self, data_other_sheet, matching_columnname, desired_columnnames: list[str]): 
        for j in desired_columnnames:
            data = []
            for i in self.df.index:
                cellvalue_mathcincolumnname = self.df.loc[i, matching_columnname]
                rows: pd.DataFrame = data_other_sheet.df.loc[data_other_sheet.df[matching_columnname] == cellvalue_mathcincolumnname]
                first_row = rows.iloc[0]
                cell_value_firstrow = first_row.loc[j]
                data.append(cell_value_firstrow)
            self.df.insert(len(self.df.columns), j, data)
        return self.df

    def __repr__(self):
        return str(self.df)