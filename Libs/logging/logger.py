# -*- coding: utf-8 -*-
"""
Created @author: Qi
Catherine learn from Qi
"""
import datetime
import os

class Logging(object):
    def __init__(self, current_working_path, script_name, custom_name):
        log_pth = "{}_{}.txt".format(script_name, custom_name)
        self.log_pth = os.path.join(current_working_path, log_pth)

    def write(self, message):
        current_datetime_str = datetime.datetime.now().strftime("%H:%M:%S on %B %d, %Y")
        with open(self.log_pth, "a") as text_file:
            text_file.write("{}:   {}\n".format(current_datetime_str, message))

    def write_separator(self, num_of_break):
        breakline = "\n" * num_of_break
        with open(self.log_pth, "a") as text_file:
            text_file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------{}".format(breakline))
