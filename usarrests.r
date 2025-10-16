data("USArrests")
install.packages("skimr")
library("skimr")
skim(USArrests)

#comparing numeric values
prop.table(table(USArrests$Murder,USArrests$UrbanPop))
unique(USArrests)
USArrests[6:12,1:2]#THIS IS THE PROCESS OF SLICING