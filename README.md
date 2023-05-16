# Scriptie program

# agouti.py
This file processes the data received by the agouti (neural network). The agouti software scans wildlifecamera images for sightings of animals, and labels these. It returns three csv files containing usable information: observations.csv, media.csv and deployments.csv. All three data sheets contain usefull information for this program, which this program links together.

The datasheets are connected with one another by the form of IDs
observations.csv contains: deploymentID, sequenceID, scientificName and to the second exact timestamp.
media.csv contains: sequenceID and fileName.
deployments.csv contains: deploymentID, longitude, latitude, locationName and cameraID.

pictures of the three csv files, with their data

![image](https://github.com/realysi/code_scriptie/assets/116087413/1f5c99b4-ff34-4c38-bf8e-1c82df6b1d10)

