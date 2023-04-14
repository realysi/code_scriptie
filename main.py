from code.reading_data_voorbeelden import read_data
from code.intervals import hours_to_seconds, seconds_to_hours, dates_to_seconds, select_row_species
from code.intervals import select_ID
import datetime
"https://www.geeksforgeeks.org/how-to-convert-datetime-to-integer-in-python/"

link_audio_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_audio.csv"
link_video_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_video.csv"

"""df = read_data(link_audio_voorbeelden)
print(df)
for i in df.index:
    print(df.loc[i, "Tijd begin detectie"],'\n')"""

df = read_data(link_video_voorbeelden)
print(df)
hours_to_seconds(df, "Tijd foto")
print(df)
seconds_to_hours(df, "Tijd foto")
print(df)
dates_to_seconds(df, "Datum")
print(df)
print(select_row_species(df, "Soort", "Rattus Norvegicus"))
print(select_ID(df, "ID", 6))