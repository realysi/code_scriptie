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

    def calculate_difference_datetime(self, columnname1, columnname2, desired_name_column):
        differences = []
        for i in self.df.index:
            value_column1 = self.df.loc[i, columnname1]
            value_column2 = self.df.loc[i, columnname2]
            value_column1 = value_column1.timestamp()
            value_column2 = value_column2.timestamp()
            difference = abs(value_column1 - value_column2)
            differences.append(difference)
        self.df.insert(len(self.df.columns), desired_name_column, differences)
    
    def select_rows_by_columnvalue(self, columnname, columnvalue):
        """
        returns the rows of the dataframe which have a certain columnvalue for column x
        """
        self.df = self.df.loc[self.df[columnname] == columnvalue]
        return self
    
    def add_utc(self, columnname_timestamp, location_data: str, desired_name_column):
        """
        Turns the time from localized Amsterdam time to UTC time.
        """
        times = []
        for i in self.df.index: 
            #this should be done in another function
            timestamp = str(self.df.loc[i, columnname_timestamp]) #2022-08-03T12:00:28+01:00
            date, time = timestamp.split('T') #-> date = 2022-08-03 time = 12:00:28+01:00
            time = time.split('+')[0] #time = 12:00:28
            year, month, day = date.split("-") #format in xlsx is d/m/y but it became y-m-d ??
            hours, minutes, seconds = time.split(":")
            datetime_object: datetime.datetime = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hours), minute=int(minutes), second=int(seconds))
            #2.change timezone
            if location_data.lower() == 'artis':
                datetime_object = pytz.timezone('Europe/Amsterdam').localize(datetime_object)
                datetime_object = datetime_object.astimezone(pytz.utc)
            else:
                if int(hours) - 1 < 0:
                    if int(day) - 1 == 0:
                        if int(month) - 1 == 0:
                            num_days = monthrange(int(year) - 1, 12)[1]
                            datetime_object = datetime_object.replace(year=int(year)-1, month=12,day=num_days,hour=23)
                        else:
                            num_days = monthrange(int(year), int(month) - 1)[1] # num_days = 28
                            datetime_object = datetime_object.replace(month= int(month) - 1, day=num_days, hour=23)
                    else:
                        datetime_object = datetime_object.replace(day=int(day) - 1, hour=23)
                else:
                    datetime_object = datetime_object.replace(hour=int(hours) -1)
            times.append(datetime_object)
        self.df.insert(len(self.df.columns), desired_name_column, times)
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
    
    def total_runtime_per_location(self):
        """
        Uses the dataframe returned by recordings(). Returns the total amount of time (datetime object) recorderd by each camera.
        Does so in a dictionary {flevopark_1: 3 days 1:36:56}
        """
        data = {}
        locations = list(set(self.df['locationName'].tolist()))
        for location in locations:
            total_seconds = 0
            rows = self.df.loc[self.df['locationName'] == location]
            recordings = len(rows)
            for i in rows.index:
                seconds = rows.loc[i, 'runtime (sec)']
                total_seconds += int(seconds)
            time = datetime.timedelta(seconds=total_seconds)
            data.update({location: [time, recordings]})
        return data

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