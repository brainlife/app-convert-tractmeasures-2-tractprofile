#!/usr/bin/env python3

def convert_tm(tractmeasures_path,outpath):

	tractmeasures = pd.read_csv(tractmeasures_path)

	for i in tractmeasures.structureID.unique():
		print("converting "+i)
		tmp = tractmeasures.loc[tractmeasures['structureID'] == i]
		tmp = tmp.drop(columns={'subjectID','structureID','nodeID'})
		tmp.to_csv(outpath+'/'+i+'_profiles.csv',index=False)

def main():

	# load config
	with open('config.json','r') as config_f:
		config = json.load(config_f)

	# create outpath
	outpath = './profiles'
	if ~os.path.isdir(outpath):
		os.mkdir(outpath)
	
	# convert tractmeasures to tractprofile datatype
	convert_tm(config["tractmeasures"])

if __name__ == '__main__':
	main()