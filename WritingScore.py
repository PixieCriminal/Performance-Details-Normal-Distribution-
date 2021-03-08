import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
df = pd.read_csv("StudentsPerformance.csv")
data = df['reading score'].tolist()
mean = sum(data)/len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
fig = ff.create_distplot([data], ["Writing Score"])
fig.show()
