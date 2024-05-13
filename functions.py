# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:00:16 2024

@author: klaus
"""

import numpy as np

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def string_split(to_split,delimiters):
    
    substrings = []
    used_delimiters = []
    new_string = ""
    for i in to_split:
        if i in delimiters:
            if len(new_string)>0:
                substrings.append(new_string)
                new_string=""
                used_delimiters.append(i)
        else:
            new_string += i
    if len(new_string)>0:
        substrings.append(new_string)
            
    return substrings,used_delimiters

def load_data(filename,xmin=-np.inf,xmax=np.inf):
    
    x = []
    y = []
    e = []
    
    with open(filename,'r') as inputfile:
        for line in inputfile:
            if not line.startswith('#'):
                data = list(line.strip().split())
                x.append(float(data[0]))
                y.append(float(data[1]))
                if len(data) == 3:
                    e.append(float(data[2]))
                else:
                    e.append(np.sqrt(float(data[1])))
         
    x = np.array(x)
    y = np.array(y)
    e = np.array(e)
         
    y = y[x>=xmin]
    e = e[x>=xmin]
    x = x[x>=xmin]
    
    y = y[x<=xmax]
    e = e[x<=xmax]
    x = x[x<=xmax]

    return x,y,e

def load_grasp_data(filename,xmin=-np.inf,xmax=np.inf):
    
    x = []
    y = []
    e = []
    eq = []
    
    with open(filename,'r') as inputfile:
        for line in inputfile:
            data = list(line.strip().split())
            if len(data) == 4:
                try:
                    x.append(float(data[0]))
                    y.append(float(data[1]))
                    e.append(float(data[2]))
                    eq.append(float(data[3]))
                except:
                    pass
            elif len(data) == 3:
                try:
                    x.append(float(data[0]))
                    y.append(float(data[1]))
                    e.append(float(data[2]))
                    eq.append(0.01*float(data[0]))
                except:
                    pass

            
    x = np.array(x)
    y = np.array(y)
    e = np.array(e)
    eq = np.array(eq)
         
    y = y[x>=xmin]
    e = e[x>=xmin]
    eq = eq[x>=xmin]
    x = x[x>=xmin]
    
    
    y = y[x<=xmax]
    e = e[x<=xmax]
    eq = eq[x<=xmax]
    x = x[x<=xmax]

    return x,y,e,eq