install.packages("ggplot2")
install.packages("tidyr")
install.packages("dplyr")
install.packages("ggpubr")
install.packages("scales")
install.packages("patchwork")
install.packages("viridis")
install.packages("ggrepel")
library(ggplot2)
library(dplyr)
library(tidyr)


data<-read.csv("C:/Users/user-30/Desktop/education_career_success.csv")

top_fields <- data %>%
  count(Field_of_Study) %>%
  top_n(5, n) %>%
  pull(Field_of_Study)


data %>%
  filter(Field_of_Study %in% top_fields) %>%
  ggplot(aes(x = Field_of_Study, y = Starting_Salary, fill = Field_of_Study)) +
  geom_boxplot() +
  labs(title = "Distribution of Starting Salary by Top 5 Field of Study",
       x = "Field of Study",
       y = "Starting Salary",
       fill = "Field of Study") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


salary_summary <- education_career %>%
  filter(Field_of_Study %in% top_fields) %>%
  group_by(Field_of_Study) %>%
  summarize(
    Median_Salary = median(Starting_Salary, na.rm = TRUE),
    IQR_Salary = IQR(Starting_Salary, na.rm = TRUE)
  ) %>%
  arrange(desc(Median_Salary))

print(salary_summary)


##################################


data <- data %>%
  mutate(Offer_Group = case_when(
    Job_Offers == 0 ~ "0 Offers",
    Job_Offers >= 3 ~ "3+ Offers",
    TRUE ~ NA       # we'll filter these out
  ))

data %>%
  filter(Offer_Group %in% c("0 Offers", "3+ Offers")) %>%
  ggplot(aes(x = Offer_Group, y = High_School_GPA, fill = Offer_Group)) +
  geom_boxplot() +
  labs(title = "Distribution of High School GPA by Job Offer Groups",
       x = "Number of Job Offers",
       y = "High School GPA",
       fill = "Offer Group") +
  theme_minimal() +
  scale_fill_manual(values = c("0 Offers" = "lightcoral", "3+ Offers" = "lightgreen"))


gpa_companion <-data %>%
  filter(Offer_Group %in% c("0 Offers", "3+ Offers")) %>%
  group_by(Offer_Group) %>%
  summarize(
    Median_GPA = median(High_School_GPA, na.rm = TRUE),
    Mean_GPA = mean(High_School_GPA, na.rm = TRUE),
    Count = n()
  )

print(gpa_companion)



################################






# Load required libraries
library(ggplot2)
library(dplyr)
library(ggpubr)   # for adding correlation statistics

# 1. Scatter Plot: University_GPA vs Starting_Salary

# Create scatter plot with trend line
ggplot(data, aes(x = University_GPA, y = Starting_Salary)) +
  geom_point(alpha = 0.6, color = "steelblue") +
  geom_smooth(method = "lm", se = TRUE, color = "darkred", fill = "pink") +
  labs(title = "Relationship between University GPA and Starting Salary",
       x = "University GPA",
       y = "Starting Salary",
       subtitle = "Scatter Plot with Linear Trend Line") +
  theme_minimal() +
  stat_cor(method = "pearson",
           label.x = min(data$University_GPA, na.rm = TRUE),
           label.y = max(data$Starting_Salary, na.rm = TRUE))


#######################################################





# 2. Scatter Plot: Internships_Completed vs Years_to_Promotion


ggplot(data, aes(x = Internships_Completed, y = Years_to_Promotion)) +
  geom_point(alpha = 0.6, color = "darkgreen",
             position = position_jitter(width = 0.1)) +
  geom_smooth(method = "lm", se = TRUE, color = "darkorange", fill = "lightyellow") +
  labs(title = "Relationship between Internships Completed and Years to First Promotion",
       x = "Number of Internships Completed",
       y = "Years to First Promotion",
       subtitle = "Scatter Plot with Linear Trend Line") +
  theme_minimal() +
  scale_x_continuous(breaks = seq(0,
                                  max(data$Internships_Completed, na.rm = TRUE),
                                  1)) +
  stat_cor(method = "pearson",
           label.x = 1,
           label.y = max(data$Years_to_Promotion, na.rm = TRUE))




###################################################




library(ggplot2)
library(dplyr)
library(scales)



job_offers_by_gender <- data %>%
  group_by(Gender) %>%
  summarize(
    Average_Job_Offers = mean(Job_Offers, na.rm = TRUE),
    Count = n(),
    Std_Error = sd(Job_Offers, na.rm = TRUE) / sqrt(n())
  ) %>%
  filter(!is.na(Gender))

ggplot(job_offers_by_gender, aes(x = Gender, y = Average_Job_Offers, fill = Gender)) +
  geom_col(alpha = 0.8) +
  geom_text(aes(label = round(Average_Job_Offers, 2)),
            vjust = -0.5, size = 5, fontface = "bold") +
  geom_errorbar(aes(ymin = Average_Job_Offers - Std_Error,
                    ymax = Average_Job_Offers + Std_Error),
                width = 0.2, color = "darkgray") +
  labs(title = "Average Number of Job Offers by Gender",
       x = "Gender",
       y = "Average Number of Job Offers",
       subtitle = "With standard error bars") +
  theme_minimal() +
  scale_fill_manual(values = c("Male" = "steelblue", "Female" = "lightpink")) +
  ylim(0, max(job_offers_by_gender$Average_Job_Offers) * 1.2)


gender_comparison <- t.test(Job_Offers ~ Gender, data = education_career)
print("T-test results for Job Offers by Gender:")
print(gender_comparison)
print("Average Job Offers by Gender:")
print(job_offers_by_gender)


#########################################





# 2. Bar Chart: Count of Students for Soft Skills Scores 1, 5, and 10


soft_skills_counts <- data %>%
  filter(Soft_Skills_Score %in% c(1, 5, 10)) %>%
  count(Soft_Skills_Score) %>%
  mutate(Percentage = n / sum(n) * 100)


ggplot(soft_skills_counts, aes(x = factor(Soft_Skills_Score), y = n, fill = factor(Soft_Skills_Score))) +
  geom_col(alpha = 0.8) +
  geom_text(aes(label = paste0(n, " (", round(Percentage, 1), "%)")),
            vjust = -0.3, size = 5, fontface = "bold") +
  labs(title = "Count of Students by Soft Skills Score",
       x = "Soft Skills Score",
       y = "Number of Students",
       subtitle = "Showing only scores 1, 5, and 10",
       fill = "Soft Skills Score") +
  theme_minimal() +
  scale_fill_manual(values = c("1" = "firebrick", "5" = "darkorange", "10" = "forestgreen")) +
  ylim(0, max(soft_skills_counts$n) * 1.15)

# Display the count summary
print("Student Counts by Soft Skills Score:")
print(soft_skills_counts)



#######################################################


library(patchwork) 


sat_hist <- ggplot(data, aes(x = SAT_Score)) +
  geom_histogram(binwidth = 50, fill = "skyblue", color = "black", alpha = 0.7) +
  geom_vline(aes(xintercept = mean(SAT_Score, na.rm = TRUE)),
             color = "red", linetype = "dashed", size = 1) +
  geom_vline(aes(xintercept = median(SAT_Score, na.rm = TRUE)),
             color = "blue", linetype = "dashed", size = 1) +
  labs(title = "Distribution of SAT Scores",
       x = "SAT Score",
       y = "Number of Students",
       subtitle = "Red dashed line = Mean, Blue dashed line = Median") +
  theme_minimal() +
  scale_x_continuous(breaks = seq(400, 1600, 100)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


sat_hist <- sat_hist +
  geom_density(aes(y = after_stat(count) * 50), alpha = 0.3, fill = "orange")

print(sat_hist)


sat_stats <- data %>%
  summarise(
    Mean = mean(SAT_Score, na.rm = TRUE),
    Median = median(SAT_Score, na.rm = TRUE),
    SD = sd(SAT_Score, na.rm = TRUE),
    Min = min(SAT_Score, na.rm = TRUE),
    Max = max(SAT_Score, na.rm = TRUE),
    Q1 = quantile(SAT_Score, 0.25, na.rm = TRUE),
    Q3 = quantile(SAT_Score, 0.75, na.rm = TRUE)
  )

print("SAT Score Statistics:")
print(sat_stats)


sat_ranges <- data %>%
  mutate(Score_Range = cut(SAT_Score,
                           breaks = seq(400, 1600, 100),
                           labels = paste0(seq(400, 1500, 100), "-", seq(500, 1600, 100)))) %>%
  count(Score_Range) %>%
  arrange(desc(n))

print("Most Common SAT Score Ranges:")
print(head(sat_ranges, 5))





##############################################






satisfaction_hist <- ggplot(data, aes(x = Career_Satisfaction)) +
  geom_histogram(binwidth = 1, fill = "lightgreen", color = "black", alpha = 0.7) +
  geom_vline(aes(xintercept = mean(Career_Satisfaction, na.rm = TRUE)),
             color = "red", linetype = "dashed", size = 1) +
  geom_vline(aes(xintercept = median(Career_Satisfaction, na.rm = TRUE)),
             color = "blue", linetype = "dashed", size = 1) +
  labs(title = "Distribution of Career Satisfaction Ratings",
       x = "Career Satisfaction Rating (1-10)",
       y = "Number of Students",
       subtitle = "Red dashed line = Mean, Blue dashed line = Median") +
  theme_minimal() +
  scale_x_continuous(breaks = 1:10) +
  ylim(0, NA)

print(satisfaction_hist)


satisfaction_stats <- data %>%
  summarise(
    Mean = mean(Career_Satisfaction, na.rm = TRUE),
    Median = median(Career_Satisfaction, na.rm = TRUE),
    SD = sd(Career_Satisfaction, na.rm = TRUE),
    Min = min(Career_Satisfaction, na.rm = TRUE),
    Max = max(Career_Satisfaction, na.rm = TRUE),
    Skewness = moments::skewness(Career_Satisfaction, na.rm = TRUE)
  )
print("Career Satisfaction Statistics:")
print(satisfaction_stats)
satisfaction_breaks <- data %>%
  mutate(
    Career_Satisfaction_Level = case_when(
      Career_Satisfaction >= 1 & Career_Satisfaction <= 3 ~ "Low (1–3)",
      Career_Satisfaction >= 4 & Career_Satisfaction <= 7 ~ "Medium (4–7)",
      Career_Satisfaction >= 8 & Career_Satisfaction <= 10 ~ "High (8–10)"
    )
  ) %>%
  count(Career_Satisfaction_Level) %>%
  mutate(Percentage = n / sum(n) * 100)``
print("Career Satisfaction Levels:")
print(satisfaction_breaks)
sat_hist + satisfaction_hist +
  plot_annotation(title = "Comparison of SAT Scores and Career Satisfaction Distributions")



###############################################################



library(viridis)
library(scales)
library(ggrepel)
ggplot(data, aes(x = University_GPA, y = Starting_Salary, color = Field_of_Study)) +
  geom_point(alpha = 0.7, size = 2) +
  geom_smooth(method = "lm", se = FALSE, aes(group = Field_of_Study), size = 0.5) +
  labs(title = "University GPA vs Starting Salary by Field of Study",
       x = "University GPA",
       y = "Starting Salary",
       color = "Field of Study",
       subtitle = "Colored by Field of Study with Trend Lines") +
  theme_minimal() +
  scale_color_viridis_d() +
  theme(legend.position = "right") +
  scale_y_continuous(labels = dollar_format())

##############################################################



salary_by_internships_gender <- data %>% 
  filter(Internships_Completed %in% c(0, 1, 2)) %>% 
  group_by(Internships_Completed, Gender) %>% 
  summarize(
    Average_Salary = mean(Starting_Salary, na.rm = TRUE),
    Count = n(),
    Std_Error = sd(Starting_Salary, na.rm = TRUE) / sqrt(n())
  ) %>% 
  filter(!is.na(Gender)) %>% 
  ungroup()


ggplot(salary_by_internships_gender, 
       aes(x = factor(Internships_Completed), y = Average_Salary, fill = Gender)) +
  geom_col(position = position_dodge(0.8), width = 0.7) +
  geom_errorbar(aes(ymin = Average_Salary - Std_Error, ymax = Average_Salary + Std_Error), 
                position = position_dodge(0.8), width = 0.2) +
  geom_text(aes(label = dollar(round(Average_Salary, 0))), 
            position = position_dodge(0.8), vjust = -0.5, size = 3.5) +
  labs(title = "Average Starting Salary by Internship Count and Gender",
       x = "Number of Internships Completed",
       y = "Average Starting Salary",
       fill = "Gender",
       subtitle = "With standard error bars") +
  theme_minimal() +
  scale_fill_manual(values = c("Male" = "steelblue", "Female" = "lightcoral")) +
  scale_y_continuous(labels = dollar_format()) +
  theme(legend.position = "top")

