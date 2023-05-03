import pandas as pd
from .classes.data import Data

"""
This file imports the data and turns it into panda dataframes.
"""

def read_sheets_xlsx(path: str, sheet_names: list) -> list[Data]:
    """
    Reads in xlsx files with multiple sheets and turns every sheet into a pandas dataframe.
    Probably much easier way to to this...
    """
    xlsx = pd.ExcelFile(path)
    dataframes = []
    for i in range(len(sheet_names)):
        dataframe = Data(pd.read_excel(xlsx, f'{sheet_names[i]}'))
        dataframe.name = f"{sheet_names[i]}"
        dataframes.append(dataframe)
    return dataframes

def read_xlsx(path: str, name: str) -> Data:
    xlsx = pd.read_excel(path)
    data = Data(xlsx)
    data.name = name
    return data


def read_csv(relative_path: str):
    csv = pd.read_csv(relative_path, delimiter=",", index_col=False)
    data = Data(csv)
    return data



