from code.classes.dataframe_extension import Dataframe
from code.read_data import read_csv
import pandas as pd


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