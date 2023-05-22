import pandas as pd
from code.classes.dataframe_extension import Dataframe

"""
This file imports the data and turns it into panda dataframes, which will be stored in the class Dataframe.
"""

def read_sheets_xlsx(path: str, sheet_names: list) -> list[Dataframe]:
    """
    Reads in xlsx files with multiple sheets and turns every sheet into a pandas dataframe.
    Probably much easier way to to this...
    """
    xlsx = pd.ExcelFile(path)
    dataframes = []
    for i in range(len(sheet_names)):
        dataframe = Dataframe(pd.read_excel(xlsx, f'{sheet_names[i]}'))
        dataframes.append(dataframe)
    return dataframes

def read_xlsx(path: str, name: str) -> Dataframe:
    xlsx = pd.read_excel(path)
    data = Dataframe(xlsx)
    return data


def read_csv(relative_path: str, ):
    csv = pd.read_csv(relative_path, delimiter=",", index_col=False, low_memory=False)
    data = Dataframe(csv)
    return data


dtype={"user_id": int, "username": "string"}
