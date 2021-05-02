
library(readr)
library(tidyverse)

var <- readline(prompt = "Enter any number : ");

print(var)

Braves <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/BravesData2020.csv")
model <- lm(data = Braves, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)


Brewers <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/BrewersData2020.csv")
model <- lm(data = Brewers, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Cards <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/CardsData2020.csv")
model <- lm(data = Cards, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Cubs <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/CubsData2020.csv")
model <- lm(data = Cubs, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

DBacks <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/DBacksData2020.csv")
model <- lm(data = DBacks, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Giants <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/GiantsData2020.csv")
model <- lm(data = Giants, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Mets <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/MetsData2020.csv")
model <- lm(data = Mets, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Padres <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/PadresData2020.csv")
model <- lm(data = Padres, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Phillies <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/PhilliesData2020.csv")
model <- lm(data = Phillies, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Pirates <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/PiratesData2020.csv")
model <- lm(data = Pirates, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Reds <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/RedsData2020.csv")
model <- lm(data = Reds, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)

Rockies <- read_csv("/Users/corywiard/desktop/Comp/senior-thesis/upload/RockiesData2020.csv")
model <- lm(data = Rockies, Wins ~ GP + AB + R + H + TB + SB + AVG + OBP + SLG)
summary(model)
