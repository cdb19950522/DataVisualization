import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('scrubbed.csv', low_memory=False)
duration = df['duration (seconds)']
count = [0]*8
#print count
##print duration[1]
for i in range(803):
    duration[i]= float(duration[i])
    if duration[i]<=1800:
        count[0] +=1
        
    #elif duration[i] >1800 and duration[i]<=3600:
    #    count[1] +=1
    #    continue
    #elif duration[i] >3600 and duration[i]<=5400:
    #    count[2] +=1
    #    continue
    #elif duration[i] >5400 and duration[i]<=7200:
    #    count[3] +=1
    #    continue
    #elif duration[i] >7200 and duration[i]<=9000:
     #   count[4] +=1
    #    continue
    #elif duration[i] >9000 and duration[i]<=10800:
    #    count[5] +=1
    #    continue
    #elif duration[i] >10800 and duration[i]<=12600:
    #    count[6] +=1
    #    continue
    else:
        #print duration[i]
        #print count
        count [7] +=1

print count