import matplotlib.pyplot as plot
import pandas as pd

kion = pd.read_csv('kion.csv', encoding='utf-8')

over_30deg = kion[ kion['tempreature'] > 30 ]
over_30deg_year = over_30deg.groupby(['year'])['year'].count()

over_30deg_year.plot()
plot.savefig('02_over_30deg_year.png')
