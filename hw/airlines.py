# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

airlines=[]
with open('airlines.csv','rU') as f:
    airlines = [row.split(',') for row in f]

reader=csv.DictReader(open('airlines.csv','rU'))
airlines=[i for i in reader]
for i in reader:
    airlines.append(i)

airlines[0:10]
maximum=0
for i in airlines:
    if i['incidents_00_14']>maximum:
        maximum = i['incidents_00_14']
        max_airline = i['airline']

avg_incidents=[]
for i in airlines:
    incidents=int(i['incidents_00_14'])+int(i['incidents_85_99'])
    print incidents    
    avg= incidents/29.
    print avg
    avg_incidents.append(avg)
    
clean_names=[i['airline'].strip('*') for i in airlines]
    
stars=['*' in i['airline'] for i in airlines]