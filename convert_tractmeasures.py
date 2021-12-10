#!/usr/bin/env python3

import json
import pandas as pd
import os

outpath = 'profiles'

def convert_tm(tractmeasures_path):
    tractmeasures = pd.read_csv(tractmeasures_path)
    for i in tractmeasures.structureID.unique():
        print("converting "+i)
        tmp = tractmeasures.loc[tractmeasures['structureID'] == i]
        tmp = tmp.drop(columns={'subjectID','structureID','nodeID'})
        tmp.to_csv('profiles/'+i+'_profiles.csv',index=False)

def main():
    with open('config.json','r') as config_f:
        config = json.load(config_f)
    if ~os.path.isdir(outpath):
        os.mkdir(outpath)
    convert_tm(config["tractmeasures"])

if __name__ == '__main__':
    main()
