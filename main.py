from code.reading_data_voorbeelden import read_audio_data

"https://www.geeksforgeeks.org/how-to-convert-datetime-to-integer-in-python/"

link_audio_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_audio.csv"
link_video_voorbeelden = "/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Voorbeeld_data_video.csv"

a = read_audio_data(link_audio_voorbeelden)
#print(a.to_markdown())
b = a[["ID", "Tijd begin detectie"]]
print(b)
print("\n\n")
#print(b.loc[1])

tijd = b.loc[0, "Tijd begin detectie"]
print(tijd)
print(tijd)
print(type(tijd))

for i in a["Tijd begin detectie"]:
    print(i)
#b.loc[0, "Tijd begin detectie"] = tijd + 5