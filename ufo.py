import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('scrubbed.csv', low_memory=False)
result= df['datetime'].str.split(' ')
time= [0]*24
for i in result:
    time[int(i[1].split(':')[0])%24] += 1
objects = ('0:00-0:59','1:00-1:59','2:00-2:59','3:00-3:59'
,'4:00-4:59','5:00-5:59','6:00-6:59','7:00-7:59','8:00-8:59'
,'9:00-9:59','10:00-10:59','11:00-11:59','12:00-12:59','13:00-13:59'
,'14:00-14:59','15:00-15:59','16:00-16:59','17:00-17:59','18:00-18:59'
,'19:00-19:59','20:00-20:59','21:00-21:59'
,'22:00-22:59','23:00-23:59')
#y_pos = ['0,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
y_pos = [i for i in range(24)]
#print y_pos
#y-pos = np.arange(len(objects))
#x= len(objects)
#print x 
#for i in y_pos:
#    i = float(i)
#for i in range(len(time)):
#    time[i]=str(time[i])
plt.bar(y_pos, time,width=0.5, align='center', alpha=0.5)
plt.xticks(y_pos, objects,rotation=40)
plt.ylabel('Frequency')
plt.title('eee')
plt.subplots_adjust(bottom= 0.15, top = 0.9)
for i in range(24):
    plt.text()

 
plt.show()
