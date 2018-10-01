#paramers is the file which you edit to adjust the test
#where stores a lot of .csv files #please use '/'as ending
#current_working_path
import os
import sys

current_working_path = os.path.dirname(os.path.abspath(__file__))
for directory in os.listdir(os.path.join(current_working_path, "Libs")):
    sys.path.insert(0, os.path.join(os.path.join(current_working_path, "Libs"), directory))
import general_functions
###ONLY thing you need to Change below line
read_directory = '/Users/chenchuqiao/Downloads/12_Internship/TwitterSentiment_project/TextProcessing_0831_multiprocess/testerrrorfiles/'
#what will be added to the csv after processing
tail=''
###ONLY thing you need to Change above


#where you want to automatically create a folder in the same directory as your input folder named _output in the end
#store the desired csv output #please use '/'as ending
store_directory = '/'.join(read_directory.split('/')[:-1])+"_output/"
general_functions.check_create_folder(store_directory)
#'/Users/chenchuqiao/Downloads/12_Internship/Financial/training_prototype/data_output/'
