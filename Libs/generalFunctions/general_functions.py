# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:38:11 2018

@author: Qi

This script contains many small functions. Most of them were called from the main function which inside
main_function.py. They are designed for different purposes. For each detailed documentation please go to
individual functions and check from there using __doc__ attribute
"""
#from libs import *
import os

## Requiried: a string of whole path
## Dependency: NONE
## General use was for create a folder by the given path if the folder is not exist, otherwise skip
## Main usage is for creating folder at the begining of the main script for store data
def check_create_folder(path):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except Exception as e:
        print("Original error message: {}".format(e))
        raise RuntimeError("ERROR GF002 - 1: create folder if not exist")
        #raise the errors 


## Requiried: a string containing some string format digits
## Dependency: NONE
## General use was for extracting pure number part from a string
## Main usage is the same as general usage, e.g. we need to know the number of articles from "newspapers(401)"
def Search_number_String(String):
    index_list = []
    for i, x in enumerate(String):
        if x.isdigit() == True:
            index_list.append(i)
    if len(index_list) == 0:
        return ""
    else:
        start = index_list[0]
        end = index_list[-1] + 1
        number = String[start:end]
        return number

## Requiried: a string whole folder path
## Dependency: NONE
## General use was for deleting everything(both file and sub-folder) within a folder, but not delete that folder
## Main usage in LN project is for prepare a clean folder to re-download some wrongly downloaded company's articles
def delete_folder_content(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

## Requiried: a string of target files
## Dependency: NONE
## General use was for storing JSON file and Text file to connect to google drive and google sheet
## Main usage is for third party machines.

#FileNameFor_PathFinder = 'mycreds.txt'
class Construct_relative_paths(object):
    def __init__(self, current_path, script_name):
        check_create_folder(current_path)
        self.main_path = current_path

        working_path = os.path.join(current_path, script_name + "_wd")
        check_create_folder(working_path)
        self.working_path = working_path

        rawdata_path = os.path.join(working_path, "rawdata")
        check_create_folder(rawdata_path)
        self.rawdata_path = rawdata_path

        processing_path = os.path.join(working_path, "processing")
        check_create_folder(processing_path)
        self.processing_path = processing_path

        output_path = os.path.join(working_path, "output")
        check_create_folder(output_path)
        self.output_path = output_path

    def add_path(self, input_path, folder_name):
        creating_path = os.path.join(input_path, folder_name)
        check_create_folder(creating_path)
        return creating_path
