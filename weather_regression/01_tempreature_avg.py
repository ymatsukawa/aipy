import pandas as pd
import matplotlib.pyplot as plot

kion = pd.read_csv('kion.csv', encoding='utf-8')

"""
# get average tempreature per a day
ta_data = {}
for index, row in kion.iterrows():
    month, day, tempreature = row['month'], row['day'], row['tempreature']
    format_day = str(int(month)) + '/' + str(int(day))
    if not(format_day in ta_data):
        ta_data[format_day] = []
    ta_data[format_day] += [float(tempreature)]

avgs = {}
for day in ta_data:
    avg = ( sum(ta_data[day]) / len(ta_data[day]) )
    print("{0} : {1}".format(day, avg))
"""

# get tempreature average of each month
ta_month_group = kion.groupby(['month'])['tempreature']
ta_month_group_avg = (ta_month_group.sum() / ta_month_group.count())
print(ta_month_group_avg)

"""
month
1      6.043824
2      6.725266
3      9.833226
4     14.870889
5     19.306882
6     22.441333
7     26.347527
8     27.553548
9     24.128444
10    18.838817
11    13.517556
12     8.628602
"""

ta_month_group_avg.plot()
plot.savefig('01_tempreature_avg.png')
