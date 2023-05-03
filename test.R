#install.packages("R.matlab")
#library(R.matlab)
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("rhdf5")

library(rhdf5)

setwd("/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/20220202")
files = list.files("/Users/yanickidsinga/Documents/GitHub/code_scriptie/data/Deepsquak/20220202")

for (i in files){
  #updated_string = gsub(" ", "", i)
  data = h5read(i, 'audiodata')
  str(data)
}
