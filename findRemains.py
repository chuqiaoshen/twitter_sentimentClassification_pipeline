import os
import glob
import sys

'''this script is for find all the remains list and split them into evenly seperately list and process simultaneously'''
splitnum = 4#change this when u want to split into more parts

current_working_path = os.path.dirname(os.path.abspath(__file__))

for directory in os.listdir(os.path.join(current_working_path, "Libs")):
    sys.path.insert(0, os.path.join(os.path.join(current_working_path, "Libs"), directory))

import inputParameters
#the readin path which contains all the csv input
os.chdir(inputParameters.read_directory)
#print(inputParameters.read_directory)
extension = 'csv'
inputcsvs = [i for i in glob.glob('*.{}'.format(extension))]
inputname_set = set([name.split('.csv')[0] for name in inputcsvs])
print('input csv total num: ',len(inputname_set))

#the storage path wich contains all the csv output that have the same name as the input part
os.chdir(inputParameters.store_directory)
#print(inputParameters.store_directory)
extension = 'csv'
outputcsvs = [i for i in glob.glob('*.{}'.format(extension))]
outputname_set = set([name.split('.csv')[0] for name in outputcsvs])
print('out excel total num: ',len(outputname_set))

#get the remains set
remains_set = inputname_set.difference(outputname_set)
print('remains csv length: ',len(remains_set))
remains_csv_list = [name+'.csv' for name in list(remains_set)]
print(remains_csv_list)


#for stable running I use pickle to store it and read back in the run_01
#Pickling
import pandas as pd
df = pd.DataFrame({'remainlist':remains_csv_list})
df.to_csv(os.path.join(current_working_path, "remainlist.csv"))
