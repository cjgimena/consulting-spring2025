import pandas as pd
import numpy as np

def out_clinch(loc):
    df = pd.read_csv(loc)
    #print(data.head())
    df['clinches'] = df['Player_1'].where(df['Team_1'] == 'UCLA', df['Player_2'])
    clinches = df[df['Winning Team_1'] == 1].groupby('clinches').size().to_dict()
    return clinches
    
def clinch_comp(loc):
    df = pd.read_csv(loc)
    #print(data.head())
    df['clinches'] = df['Player_1'].where(df['Team_1'] == 'UCLA', df['Player_2'])
    df['Team'] = df['Team_1'].where(df['Team_1'] != 'UCLA', df['Team_2'])
    
    clinch_df = df[df['Winning Team_1'] == 1]
    
    groups = clinch_df.groupby('clinches').agg(
        clinch_c = ('Winning Team_1', 'count'),
        opps = ('Team',list)
    )
    
    clinches = groups.apply(lambda row: [row['clinch_c'], row['opps']],axis=1).to_dict()
    return clinches
    
loc = r'C:\Users\pavan\Documents\Programming Stuff\Tennis_Consult\consulting-spring2025\data\womens\tennis_matches_data.csv'
print(out_clinch(loc))

print(clinch_comp(loc))
