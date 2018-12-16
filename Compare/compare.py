
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "x": ["27-Nov", "28-Nov", "29-Nov", "30-Nov", "01-Dec", "02-Dec", "03-Dec", "04-Dec", "05-Dec", "06-Dec", "07-Dec", "08-Dec"], 
  "y": ["8", "44", "73", "100", "134", "47", "40", "56", "104", "48", "75", "40"], 
  "name": "#ICONSIAM", 
  "orientation": "v", 
  "type": "bar", 
  "xsrc": "ksankaseam:4:ff4c99", 
  "ysrc": "ksankaseam:4:120177"
}
trace2 = {
  "x": ["27-Nov", "28-Nov", "29-Nov", "30-Nov", "01-Dec", "02-Dec", "03-Dec", "04-Dec", "05-Dec", "06-Dec", "07-Dec", "08-Dec"], 
  "y": ["1", "2", "1", "", "4", "2", "1", "", "5", "2", "3"], 
  "name": "Apple Store", 
  "orientation": "v", 
  "type": "bar", 
  "xsrc": "ksankaseam:4:ff4c99", 
  "ysrc": "ksankaseam:4:b5fe42"
}
data = Data([trace1, trace2])
layout = {
  "autosize": True, 
  "colorway": ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"], 
  "dragmode": "pan", 
  "hovermode": "x", 
  "title": "Compare a number of tweets between #ICONSIAM and 'Apple Store'", 
  "xaxis": {
    "autorange": True, 
    "range": [-0.5, 11.5], 
    "title": "Date", 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [0, 141.052631579], 
    "title": "Number of tweets", 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
