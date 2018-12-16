import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "labels": ["Twitter  for Android", "Twitter for iPad", "Twitter for iPhone", "Twitter Media Studio", "Twitter Web Client", "Others Application"], 
  "labelssrc": "ksankaseam:8:accb89", 
  "type": "pie", 
  "values": ["276", "4", "195", "2", "76", "215"], 
  "valuessrc": "ksankaseam:8:4dfe45"
}
data = Data([trace1])
layout = {
  "autosize": True, 
  "colorway": ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"], 
  "title": "Percentages of direct and indirect tweets from Twitter", 
  "xaxis": {
    "autorange": True, 
    "range": [-0.5, 4.5], 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [0, 290.526315789], 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
