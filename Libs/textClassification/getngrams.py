#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 21:18:49 2018

@author: chenchuqiao
"""
def get123gram(sentence):
            
    '''input a list of word and output 1gram, 2 gram, 3 gram output combined'''
    input_list =  sentence.split()
    #get our two and tri grame list
    z2 = zip(input_list, input_list[1:])
    twogramlist = [z[0]+' '+z[1] for z in z2]
    z3 = zip(input_list, input_list[1:], input_list[2:])
    trigramlist = [z[0]+' '+z[1]+' '+z[2] for z in z3]
    input_list.extend(twogramlist)
    input_list.extend(trigramlist)
    #finallist= finallist.extend(trigramlist)
    return input_list

#test case
#sentence = 'I like writing code and eating'
#get123gram(sentence)
