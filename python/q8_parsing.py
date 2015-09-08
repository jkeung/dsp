#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv
import pandas as pd

def read_data(data): 
    df = pd.read_csv(data, header=0)
    return df

def get_min_score_difference(parsed_data):
    temp = parsed_data['Goals'] - parsed_data['Goals Allowed']
    return temp.min()

def get_team(index_value, parsed_data):
    return parsed_data[parsed_data['Goals'] - parsed_data['Goals Allowed'] == get_min_score_difference(parsed_data)]['Team']


df = read_data('football.csv')
get_team(get_min_score_difference(df), df)