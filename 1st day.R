# Creating vector

mathScore <- c(23,34,53,58,99)
physicsScore <- c(45,64,54,22,34)
pythonScore <-c(45,56,66,65,45)
addition <- mathScore+physicsScore+pythonScore #adding all three vectors
subctraction <- mathScore-physicsScore # subtracting second vector from first


# creating lists
myList <- list(stdId = c(1,2,3,4,5),
               stdName = c("Prabesh","Anup","Hari", "Rohit","Prakriti"),
               stdAge = c(21,22,22,23,21),
               stdDepartment = c("IT","Global Business","Hospitality","IT","Hospitality"),
               stdNation = c("Nepal","India","Afganization","Mongolia","South Korea"),
               stdGender = c("Male","Male","Male","Male","Female"),
               stdResidence = c("busan","seoul","Ulsan","Deagu","busan"),
               std1AverageScore = (67),
               std2AverageScore = (69),
               std3AverageScore = (65),
               std4AverageScore = (67),
               std5AverageScore = (62),
               stdSemesterLevel = c(1,3,2,5,3),
               stdReligons = c("Hindu","Islam","Buddist","Hindu","christan"),
               stdNativeLanguage = c("English","Nepali","Spanish","Mongolian")
  
  )
# retrieving fifth element from list
fifthVariable <-  myList[5]

# removing the last and median one from the list
newList <- myList[-15]
newList2 <- newList[-7]


# adding a new item to the list 
newList3 <- append(newList2, list(stdEnglshLevel = c(1,2,3,4,5)), after = 4)

#creating the factors based on religions and retrieving the frequency and levels

stdReligions <-factor(c("hindu", "christan","Islam","muslim","hindu"))
stdlevel <- levels(stdReligions)
stdfrequency <- table(stdReligions)

# creating dataframes 
education <- data.frame(ID = sample(c(1,2,3,4,NA),50,replace = TRUE),
                        Name = sample(c("Prabesh","Anup","Hari", NA,"Prakriti"),50,replace = TRUE),
                        age = sample(c(21,22,22,23,21, NA),50,replace = TRUE),
                        gender = sample(c("Male", "Female"), 50, replace = TRUE),
                        livingarea = sample(c("rural", NA,"rural","urban","rural"),50,replace = TRUE),
                        major =  sample(c("IT",NA,"Hospitality","IT","Hospitality"),50,replace = TRUE),
                        semester= sample(c(1,3,2,5,3),50,replace = TRUE),
                        attendence = sample(c("yes","No","yes",NA,"NO"),50,replace = TRUE),
                        grade = sample(c('A','B',NA,'D','F'),50,replace = TRUE),
                        result = sample(c("fail","pass",NA,"pass","pass"),50,replace = TRUE),
                        homecountry = sample(c("nepal",NA,"india","bangladesh","philipines"),50,replace = TRUE)
                        
)
education

#finding the structure of dataframe
structure <- str(education)
structure(education)

#finding the summary of the dataframes
summary <- summary(education)
summary(education)


#finding dimensions
Dimension <- dim(education)
Dimension

# records and features 
Records <- nrow(education)
Records

Features <- ncol(education)
Features


#listing features names
featureName <- names(education)
featureName

#counting the features number
Features


#finding the number of NA in dataset
number_of_NA <- sum(is.na(education))
number_of_NA

#percentage of missing values per features
percentageofmissingvalueperfeature <- colSums(is.na(education))*100
percentageofmissingvalueperfeature



# Percentage of missing values
percentage_missing <- (number_of_NA /Features) * 100
#percentage_missing


#adding the missing values
clean_df <- na.omit(education)
sum(is.na(clean_df))


#finding the proportion of males and females std by major
proportion1 <- prop.table(table(education$gender))
proportion1


#finding the proportion of males and females by location
proportion2 <- prop.table(table(education$livingarea))
proportion2

prop.table(table(clean_df$gender, clean_df$livingarea))
prop.table(table(clean_df$gender, clean_df$result))


install.packages("skimr")
library("skimr")


skim(clean_df)
