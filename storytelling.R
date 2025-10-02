install.packages("skimr")
library("skimr")


data("iris")
View(iris)

#structure of the dataset
str(iris)

skim(iris)

#2 dimension/shape of the dataset
dim(iris)

#3 the features of the dataset
names(iris)

#4  finding missing values
sum(is.na(iris))

#5 #summary of the dataset
summary(iris)

#6 comparing the means between mean of species
aggregate(. ~ Species, data = iris, mean)

# finding unique values
lapply(iris,unique)
#in sepal length
length(unique(iris$Sepal.Length))
#in sepal.width
length(unique(iris$Sepal.Width))
#in petal.length
length(unique(iris$Petal.Length))
#in petal.width
length(unique(iris$Petal.Width))
#in species
length(unique(iris$Species))

#8obtaing information
prop.table(table(iris$Species))




# The dataset (iris) is about the explaining of a plant called iris.It has five features(i.e Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width"  "Species"  
# ) with 150 records in each of them. petal length is shortest in setosa,longest in virginica and sepal width is widest in setosa,narrowest in versicolor
# there are three unique values in species that are setosa,versicolor and virginica.we see unique 
# value in each features i.e 35,23,43,22,3 in sepallength ,sepal width ,petal length,petalwidth, and species respectively
# thre are many limiations in the dataset as it has only 150 samples with only four features and it is very limited dataset ie only three speceis. 
7