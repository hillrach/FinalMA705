#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import json

"""
#Get all sports
endpoint = "https://olypi.com/sports/?call=GetAllSports"
parameters = {}

olympics_req = requests.get(endpoint, params = parameters)
olympics_req.raise_for_status()    

sports = olympics_req.json()

with open('sports.json', 'w') as f:
    json.dump(sports, f, indent=4)

"""
#Bring in sports data from API
with open('sports.json') as f:
    sports = json.load(f)    
sports = pd.json_normalize(sports, record_path =['result'])
sports = sports.drop([0])
sports['Sport'] = sports['name']
sports = sports.drop(columns=['name'])
  
#Bring in olympics data from csv  
olympics = pd.read_csv('olympics.csv', encoding='latin-1')

#Join dataframes to create one for all info by sport 
olympic_count = olympics.groupby('Sport').count()
olympic_count = olympic_count.drop(columns=['Name', 'Country', 'Event', 'Code', 'Gender', 'Age', 'NOC', 'Discipline', 'Unnamed: 0'])
olympic_count = olympic_count.rename(columns={'Medal': 'NumMedals', 'Rank': 'NumRanked', 'link': 'Link'})

olympic_mean = olympics.groupby('Sport').mean()
olympic_mean = olympic_mean.drop(columns=['Unnamed: 0', 'Code'])
olympic_mean = olympic_mean.rename(columns={'Age': 'AvgAge', 'Rank': 'AvgRank'})

infosport = pd.merge(sports, olympic_count, on='Sport')
infosport = pd.merge(infosport, olympic_mean, on='Sport')
infosport = infosport.drop(columns=['id'])
infosport = infosport.rename(columns={'link': 'Link'})
infosport = infosport[['Sport', 'NumMedals', 'NumRanked', 'AvgAge', 'AvgRank', 'Link']]
infosport.to_pickle('/Users/rachelhill/Desktop/infosport.pkl')

event_mean = olympics.groupby(['Sport', 'Event']).mean()
event_mean = event_mean.drop(columns=['Unnamed: 0', 'Code'])
event_mean = event_mean.rename(columns={'Age': 'AvgAge', 'Rank': 'AvgRank'})

event_count = olympics.groupby(['Sport', 'Event']).count()
event_count = event_count.drop(columns=['Country', 'Code', 'Gender', 'Age', 'NOC', 'Discipline', 'Unnamed: 0'])
event_count = event_count.rename(columns={'Medal': 'NumMedals', 'Rank': 'NumRanked', 'Name': 'Number of Athletes'})

event_max = olympics.drop(columns=['Medal', 'Name'])
event_max = event_max.groupby(['Sport', 'Event']).max()
event_max = event_max.drop(columns=['Code', 'Gender', 'Discipline', 'Unnamed: 0', 'Rank', 'Country', 'NOC'])
event_max = event_max.rename(columns={'Age': 'MaxAge'})

event_min = olympics.drop(columns=['Medal', 'Name'])
event_min = event_min.groupby(['Sport', 'Event']).min()
event_min = event_min.drop(columns=['Code', 'Gender', 'Discipline', 'Unnamed: 0', 'Rank', 'Country', 'NOC'])
event_min = event_min.rename(columns={'Age': 'MinAge'})

infoevent_multi = pd.merge(event_mean, event_max, on=['Sport', 'Event'])
infoevent_multi = pd.merge(infoevent_multi, event_count, on=['Sport', 'Event'])
infoevent_multi = pd.merge(infoevent_multi, event_min, on=['Sport', 'Event'])
infoevent_multi.to_pickle('/Users/rachelhill/Desktop/infoevent_multi.pkl')

infoevent = infoevent_multi
infoevent = infoevent.reset_index(level=None, drop=False, inplace=False, col_level=0)
infoevent["AvgAge"] = round(infoevent.AvgAge, 2)
infoevent["AvgRank"] = round(infoevent.AvgRank, 2)
infoevent = infoevent[['Sport', 'Event', 'Number of Athletes', 'MinAge', 'MaxAge', 'AvgAge', 'NumRanked', 'AvgRank']] 
infoevent = infoevent.rename(columns={'Event': 'EVENT',
                                      'Sport': 'SPORT',
                                      'NumMedals': 'NO. MEDALS AWARDED',
                                      'Number of Athletes': 'NO. OF ATHLETES',
                                      'MinAge': 'YOUNGEST ATHLETE AGE',
                                      'MaxAge': 'OLDEST ATHLETE AGE',
                                      'AvgAge': 'AVERAGE ATHLETE AGE', 
                                      'NumRanked': 'NO. RANKED ATHLETES',
                                      'AvgRank': 'AVERAGE ATHLETE RANK'})
infoevent.to_pickle('/Users/rachelhill/Desktop/infoevent.pkl')



olympics['Gold'] = olympics['Medal'] == "Gold"
olympics['Gold'] = olympics['Gold'].astype('uint8')

olympics['Silver'] = olympics['Medal'] == "Silver"
olympics['Silver'] = olympics['Silver'].astype('uint8')

olympics['Bronze'] = olympics['Medal'] == "Bronze"
olympics['Bronze'] = olympics['Bronze'].astype('uint8')

olympics.to_pickle('/Users/rachelhill/Desktop/olympics.pkl')






