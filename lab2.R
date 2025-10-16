install.packages("skimr")
install.packages("dplyr")
install.packages("moments")
install.packages("psych")
library(dplyr)
library(psych)
library(skimr)
library(moments)

set.seed(123) 

students_data <- data.frame(
  student_id = 1:50,
  name = paste0("Student_", 1:50),
  age = sample(18:25, 50, replace = TRUE),
  grade_year = sample(1:4, 50, replace = TRUE),
  major = sample(c("Computer Science", "Biology", "Economics", "Psychology"), 50, replace = TRUE),
  gpa = round(runif(50, 2.0, 4.0), 2),
  hours_studied = sample(10:40, 50, replace = TRUE),
  passed = sample(c(TRUE, FALSE), 50, replace = TRUE, prob = c(0.8, 0.2)))

students_data

students_data$gpa[sample(1:50, 5)] <-NA
students_data$hours_studied[sample(1:50, 3)] <-NA
head(students_data)
str(students_data)
summary(students_data) 
skim(students_data)
sum(is.na(students_data))

#shows the first 10 rows of dataset
first_10 <-students_data[1:10,]
first_10

skewness(students_data$grade_year)
describe(students_data)
summary(students_data)

#How many students have computer science as their major?
cs_students <-students_data[students_data$major=="Computer Science",]
cs_students
length(cs_students)

economics <- students_data[students_data$major=="Biology",]
length(economics)
#How many students achieved the highest grades and passed, regardless of the major?
#getting last 20 students
last_20 <- students_data[30:50,]
last_20
tail(students_data)

#How many students achieved the highest grades and passed, regardless of the major?
high_achievers <- students_data[students_data$gpa > 3.5 & students_data$passed == TRUE, ]
high_achievers
length(high_achievers)


#How many students are younger but still achieved high performance?
young_high_achievers <- subset(students_data, age < 21 & gpa > 3.0)
young_high_achievers

#How many students achieved the lowest grades and failed, regardless of the major?
low_achievers <- students_data[students_data$gpa < 2.4 & students_data$passed == FALSE, ]
low_achievers
nrow(low_achievers)

#Add a new column status based on students GPA. If it is above 3.0 it is good but below the student needs improvements

students_data$status <- ifelse(students_data$gpa > 3.0, "Good", "Needs Improvement")
students_data

#Consider rounding up their grades to 1
students_data$gpa_rounded <- round(students_data$gpa, 1)
students_data


#Calculate and add a column displaying each students efficiency which is GPA by the number of hours studied
students_data$study_efficiency <- students_data$gpa / students_data$hours_studied
students_data$gpa_imputed <- ifelse(is.na(students_data$gpa),
                                    mean(students_data$gpa, na.rm = TRUE), 
                                    students_data$gpa)
students_data

#names of the coloums in ascending order
ls(students_data)
colnames(students_data)#normal names

#aranging coloums_ assignment
students_data <- students_data %>%
select(name, major, gpa, everything())
#Since they are doing double major, how many are doing computer science and economics
bio_or_econ <- students_data %>%
filter(major == "Biology" | major == "Economics")





