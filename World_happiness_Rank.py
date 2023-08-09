import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Preprocessing each data into same format

data_2015 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2015.csv')
data_2015['Year'] = 2015

data_2016 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2016.csv')
data_2016['Year'] = 2016

data_2017 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2017.csv')
data_2017 = data_2017.rename(columns = {'Happiness.Rank' : 'Happiness Rank', 'Happiness.Score' : 'Happiness Score', 
                                        'Economy..GDP.per.Capita.' : 'Economy (GDP per Capita)', 
                                        'Health..Life.Expectancy.' : 'Health (Life Expectancy)', 
                                        'Trust..Government.Corruption.' : 'Trust (Givernment Corruption)'})
data_2017['Year'] = 2017

data_2018 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2018.csv')
data_2018 = data_2018.rename(columns = {'Overall rank' : 'Happiness Rank', 'Country or region' : 'Country', 'Score' : 'Happiness Score',
                                      'GDP per capita' : 'Economy (GDP per Capita)', 'Social support' : 'Family',
                                      'Healthy life expectancy' : 'Health (Life Expectancy)','Freedom to make life choices' : 'Freedom',
                                      'Perceptions of corruption' : 'Trust (Government Corruption)'})
data_2018['Year'] = 2018


data_2019 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2019.csv')
data_2019 = data_2019.rename(columns = {'Overall rank':'Happiness Rank', 'Country or region' : 'Country', 'Score' : 'Happiness Score',
                                      'GDP per capita' : 'Economy (GDP per Capita)', 'Social support' : 'Family',
                                      'Healthy life expectancy' : 'Health (Life Expectancy)','Freedom to make life choices' : 'Freedom'
                                     , 'Perceptions of corruption' : 'Trust (Government Corruption)'})
data_2019['Year'] = 2019

data_2020 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2020.csv')
data_2020['Happiness Rank'] =  range(1, len(data_2020.index)+1)
data_2020 = data_2020.rename(columns = {'Country name' : 'Country', 'Ladder score' : 'Happiness Score', 
                                      'Logged GDP per capita' : 'Economy (GDP per Capita)', 'Social support' : 'Family', 'Healthy life expectancy' : 'Health (Life Expectancy)',
                                      'Freedom to make life choices' : 'Freedom', 'Perceptions of corruption' : 'Trust (Government Corruption)'})
data_2020['Year'] = 2020

data_2021 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2021.csv')
data_2021['Happiness Rank'] =  range(1, len(data_2021.index)+1)
data_2021 = data_2021.rename(columns = {'Country name' : 'Country', 'Ladder score' : 'Happiness Score', 
                                      'Logged GDP per capita' : 'Economy (GDP per Capita)', 'Social support' : 'Family', 'Healthy life expectancy' : 'Health (Life Expectancy)',
                                      'Freedom to make life choices' : 'Freedom', 'Perceptions of corruption' : 'Trust (Government Corruption)'})
data_2021['Year'] = 2021

data_2022 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2022.csv')
data_2022 = data_2022.rename(columns = {'RANK' : 'Happiness Rank', 'Explained by: GDP per capita' : 'Economy (GDP per Capita)', 'Explained by: Social support' : 'Family', 'Explained by: Healthy life expectancy' : 'Health (Life Expectancy)',
                                      'Explained by: Freedom to make life choices' : 'Freedom', 'Explained by: Perceptions of corruption' : 'Trust (Government Corruption)', 'Explained by: Generosity' : 'Generosity'})
data_2022['Year'] = 2022

data_2023 = pd.read_csv('/Users/Yu/Documents/GitHub/Midterm_Project/data/2023.csv')
data_2023['Happiness Rank'] =  range(1, len(data_2023.index)+1)
data_2023 = data_2023.rename(columns = {'Country name' : 'Country', 'Ladder score' : 'Happiness Score', 
                                      'Logged GDP per capita' : 'Economy (GDP per Capita)', 'Social support' : 'Family', 'Healthy life expectancy' : 'Health (Life Expectancy)',
                                      'Freedom to make life choices' : 'Freedom', 'Perceptions of corruption' : 'Trust (Government Corruption)'})
data_2023['Year'] = 2023


# Store esch data from 2015 - 2023 into new DataFrame

datasets = [data_2015, data_2016, data_2017, data_2018, data_2019, data_2020, data_2021, data_2022, data_2023]
combined_data = pd.concat(datasets, ignore_index=True)

columns = ['Year', 'Country', 'Happiness Rank', 'Happiness Score', 'Economy (GDP per Capita)',
                   'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)',
                   'Generosity']
filtered_data = combined_data[columns]
data_rank = filtered_data

data_rank.to_csv('data_rank.csv', sep=',', index=False)