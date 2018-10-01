import pandas as pd
import numpy as np
import re
from collections import Counter
import matchdic#this is the new enriched dict
import getngrams#this is the ngram input function

'''given text input , clean and output the classification output based on 3-grams matching '''

dict_match_re = {}
for k,value in matchdic.enricheddic.items():
    for v in value:
        dict_match_re.setdefault(v,k)#.append(k)
# text cleaning part-----------------------------
dict_match_set_dict = {}
for k,value in matchdic.enricheddic.items():
    dict_match_set_dict.update({k:set(value)})
set_finan = dict_match_set_dict.get('financial_disclosure')
set_crm = dict_match_set_dict.get('crm')
set_mkt = dict_match_set_dict.get('marketing_and_sales')
set_jobs = dict_match_set_dict.get('jobs')

def replace_AT_HASH(text):
    """  """
    #Replaces AT and HASH to splited ones
    text = re.sub('@','@ ',text)
    text = re.sub('$',' $',text)
    text = re.sub(r'#', r'# ', text)
    counterinput = getngrams.get123gram(text)
    textdict = dict(Counter(counterinput))
    return textdict

#Replace Contractions#web search #this can be replaced in the future by a list
contraction_patterns = [ (r'won\'t', 'will not'), (r'can\'t', 'cannot'), (r'i\'m', 'i am'), (r'ain\'t', 'is not'), (r'(\w+)\'ll', '\g<1> will'), (r'(\w+)n\'t', '\g<1> not'),
                         (r'(\w+)\'ve', '\g<1> have'), (r'(\w+)\'s', '\g<1> is'), (r'(\w+)\'re', '\g<1> are'), (r'(\w+)\'d', '\g<1> would'), (r'&', 'and'), (r'dammit', 'damn it'), (r'dont', 'do not'), (r'wont', 'will not') ]
def replaceContraction(text):
    """ Replaces contractions from a string to their equivalents
    """
    patterns = [(re.compile(regex), repl) for (regex, repl) in contraction_patterns]
    for (pattern, repl) in patterns:
        (text, count) = re.subn(pattern, repl, text)
    return text

def get_match(sentence):
    """using the set method get the count result
    """
    #input the cleaned text and output the list of 4
    sentence = sentence.lower()
    aftercontarction = replaceContraction(sentence)
    d = replace_AT_HASH(aftercontarction)

    single_d = {key:value for key, value in d.items() if value == 1}
    #set that only contains one count and can be used for intersection manipulation
    single_set = set(single_d.keys())
    #the nums which generated from set manipulating
    global set_finan
    global set_crm
    global set_mkt
    global set_jobs
    num_finan = len(single_set & set_finan)
    num_crm =  len(single_set & set_crm)
    num_mkt =  len(single_set & set_mkt)
    num_jobs =  len(single_set & set_jobs)
    #no single set, which can be used to to use dictionary
    n_single_d = {key:value for key, value in d.items() if value != 1}
    for word in n_single_d.keys():
        if word in set_finan:
            num_finan +=  n_single_d.get(word)
        elif word in set_crm:
            num_crm +=   n_single_d.get(word)
        elif word in set_mkt:
            num_mkt +=  n_single_d.get(word)
        else:
            num_jobs +=  n_single_d.get(word)

    return [num_finan,num_crm,num_mkt,num_jobs]

# classificatin part-----------------------------
def getTheClassificaton(listofFour):
    """input the list of 4 and output the class defined
    """
    maxvalue = max(listofFour)
    if listofFour[0] == maxvalue:
        return 'financial_disclosure'
    elif listofFour[1] == maxvalue:
        return 'crm'
    elif listofFour[2] == maxvalue:
        return 'marketing_and_sales'
    else:
        return 'jobs'

def allforClassification(sentence):
    """ this combines all the functions togehter: from text in df to the classification output
    """
    listofFour = get_match(sentence)
    classification = getTheClassificaton(listofFour)
    return classification
