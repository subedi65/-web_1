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
education <- data.frame(ID = c(1,2,3,4,5),
                        Name = c("Prabesh","Anup","Hari", "Rohit","Prakriti"),
                        age = c(21,22,22,23,21),
                        livingarea = c("rural", "urban","rural","urban","rural"),
                        major =  c("IT","Global Business","Hospitality","IT","Hospitality"),
                        semester= c(1,3,2,5,3),
                        attendence = c("yes","No","yes","No","NO"),
                        grade = c('A','B','C','D','F'),
                        result = c("fail","pass","fail","pass","pass")
                        
)
education
structure <- str(education)
summarys <- summary(education)

