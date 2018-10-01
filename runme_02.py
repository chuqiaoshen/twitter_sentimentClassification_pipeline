#this file is the only .py file you need to run to get the output(sentiment + classification)
#please follow the Readme before you run this
#the structure reedit version

import sys
import os
import glob
#import openpyxl
#import xlsxwriter
import pandas as pd
# Import self defined functions
import inputParameters
import textCleaning
import textClassification
import SentimentModel
from logger import Logging
from lib_import import *
from textClassification import allforClassification

# Insert all the sub-folder path under Libs folder into system path so that we can import different modules
current_working_path = os.path.dirname(os.path.abspath(__file__))
for directory in os.listdir(os.path.join(current_working_path, "Libs")):
    sys.path.insert(0, os.path.join(os.path.join(current_working_path, "Libs"), directory))
#model reload
file_name = os.path.join(current_working_path, 'scv_model_v3.sav')
feature_name = os.path.join(current_working_path,'feature3.pkl')
#logger initiate
script_name = os.path.basename(__file__).split(".")[0]
Logger = Logging(current_working_path, script_name, "_log")
Logger.write_separator(2)

#get the output from the remainlist.txt file and use the outputlist as input
#if we want to use split methods, edit this part
#CHANGE BELOW
df_remains = pd.read_csv('remainlist.csv')
inputcsvs_all = df_remains.remainlist.tolist()
totalnum = len(inputcsvs_all)
splitnum = int(totalnum/4)
inputcsvs = inputcsvs_all[ splitnum : 2 * splitnum]

#inputcsvs_full = glob.glob(inputParameters.read_directory+'*.csv')
#inputcsvs = [file.split('/')[-1] for file in inputcsvs_full]
#CHANGE ABOVE
totalnum = len(inputcsvs)
print('Total csv will be processed: {}'.format(totalnum))
Logger.write('Total csv will be processed: {}'.format(len(inputcsvs)))
Logger.write_separator(2)

#process all the csv step by step
counter = 0
for inputfilename in inputcsvs:
    counter += 1
    print(str(counter)+'/'+str(totalnum))
    print(inputfilename+'..is being processed')
    Logger.write(str(counter)+'/'+str(totalnum))
    Logger.write(inputfilename+'..is being processed')
    try:
        #print(inputParameters.read_directory)
        #print(inputfilename)
        ###read in file
        try:
            #print(os.path.join(inputParameters.read_directory, inputfilename))
            df = pd.read_csv(os.path.join(inputParameters.read_directory, inputfilename))
            #print('Readin csv file successfully {}'.format(inputfilename))
        except Exception as e:
            print('not able to Readin csv file {}'.format(inputfilename))
            Logger.write("Not able to Readin csv file {} exceptions happen {}".format(inputfilename,e))
        ###data cleaning
        try:
            df_sentiment = df[['tweet','id']].copy()
            df_sentiment['clean_text']=df_sentiment.tweet.apply(lambda x: textCleaning.textCleanning_Pipeline(x))
            #print("textcleaning_Pipeline: finished")
        except Exception as e:
            print("textcleaning_Pipeline has problems, exceptions {}".format(e))
            Logger.write("textcleaning_Pipeline has problems, exceptions {}".format(e))
        ###sentiment analysis based on tweets cleaned
        try:
            sentiment_arr, Logger = SentimentModel.GetPositiveProb(feature_name, file_name, df_sentiment.clean_text, Logger)
            df_sentiment['nb_pos']= sentiment_arr
            #print('text sentiment analysis for finished')
        except Exception as e:
            print('text sentiment analysis for file has problems')
            Logger.write("text sentiment analysis for file {} has problems".format(inputfilename))
        ###add classification
        #construct classification columns and 4 more columns based on the classification out
        try:
            df_classification = df[['tweet','id']].copy()
            df_classification['classification'] = df_classification.tweet.apply(allforClassification)
            df_classification['financial_disclosure'] = df_classification['classification'].apply(lambda x: 1 if x == 'financial_disclosure' else 0)
            df_classification['crm']= df_classification['classification'].apply(lambda x: 1 if x == 'crm'else 0)
            df_classification['marketing_and_sales'] = df_classification['classification'].apply(lambda x: 1 if x == 'marketing_and_sales' else 0)
            df_classification['jobs']= df_classification['classification'].apply(lambda x: 1 if x == 'jobs' else 0)
            #print("construct new columns with 0 & 1 : finished ")
        except Exception as e:
            Logger.write("add classifcation columns has problems {} ".format(e))
        ###merge them together
        try:
            merged_df = pd.merge(df, df_sentiment,  how='left', on='id')
            merged_df = pd.merge(merged_df, df_classification,  how='left', on='id')
        except Exception as e:
            print("merging columns has problems")
            Logger.write("merging columns has problems {} ".format(e))

        ###add three more columns which is just for adding four more columns for further processing
        try:

            merged_df['fin_s'] = merged_df['nb_pos']* merged_df['financial_disclosure']
            merged_df['crm_s'] = merged_df['nb_pos'] * merged_df['crm']
            merged_df['sm_s'] = merged_df['nb_pos'] * merged_df['marketing_and_sales']
            merged_df['jobs_s'] = merged_df['nb_pos'] * merged_df['jobs']
            #print('add fin_s...columns successfully')
        except Exception as e:
            print('add new columns fin_s....has problems')
            Logger.write("add new fin_s....columns has problems")
        ###rename them to desired names
        try:
            df_final = merged_df[['datetime', 'gvkey','username', 'id', 'tweet', 'date', 'time',
            'hashtags', 'mentions', 'replies', 'retweets', 'likes', 'link', 'RT',
            'countHA', 'countAT',  'financial_disclosure', 'crm','marketing_and_sales', 'jobs',
            'fin_s','crm_s','sm_s','jobs_s','nb_pos','cgvkey']]
            df_final = df_final.rename(columns={'marketing_and_sales': 'sm', 'financial_disclosure': 'fin'})
        except Exception as e:
            print('slice final columns has problems {}'.format(e))
            Logger.write('slice final columns has problems {}'.format(e))

        ''' if we want to store as excel
        try:
            writer = pd.ExcelWriter(os.path.join(inputParameters.store_directory ,(inputfilename.split('.csv')[0] +inputParameters.tail+'.xlsx')))
            df_final.to_excel(excel_writer = writer,sheet_name = 'sheet1',index = False, encoding='utf-8')
            writer.save()
            print('stored finished {} successfully '.format(inputfilename))
            Logger.write("stored finished successfully {} ".format(inputfilename))
        except Exception as e:
            print('save as excel has problems {}'.format(e))
            Logger.write('save as excel has problems {}'.format(e))'''
        ###store as csvs
        try:
            df_final.to_csv(os.path.join(inputParameters.store_directory ,(inputfilename.split('.csv')[0] +inputParameters.tail+'.csv')), index = False)
            print(inputfilename+' process successfully')
            Logger.write(inputfilename+' process successfully')
        except Exception as e:
            print('save as csvs has problems {}'.format(e))
            Logger.write_separator(2)
            print('--------------------------')

    except Exception as e:
        print(inputfilename, ' has problem in processing')
        Logger.write('{} has problem in processing'.format(inputfilename))
        print(e)
        Logger.write("Exceptions happened  {}".format(e))
        print('--------------------------')
        Logger.write_separator(2)
        pass
