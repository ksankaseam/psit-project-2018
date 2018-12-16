import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "x": ["11/27/2018", "11/28/2018", "11/28/2018", "11/29/2018", "12/1/2018", "12/1/2018", "12/1/2018", "12/1/2018", "12/2/2018", "12/2/2018", "12/3/2018", "12/5/2018", "12/5/2018", "12/5/2018", "12/5/2018", "12/5/2018", "12/6/2018", "12/6/2018", "12/7/2018", "12/7/2018", "12/7/2018"], 
  "type": "histogram", 
  "xsrc": "ksankaseam:2:d00d9e"
}
data = Data([trace1])
layout = {
  "autosize": True, 
  "colorway": ["#fbb4ae", "#b3cde3", "#ccebc5", "#decbe4", "#fed9a6", "#ffffcc", "#e5d8bd", "#fddaec", "#f2f2f2"], 
  "title": "Number of tweets about 'Apple Store' on a #ICONSIAM before Grand opening", 
  "xaxis": {
    "autorange": True, 
    "range": [-0.5, 8.5], 
    "title": "Date", 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [0, 5.26315789474], 
    "title": "Number of tweets"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
