import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "x": ["ชอบ", "ดี", "สวย", "ใหญ่", "สะอาด"], 
  "y": ["24", "101", "34", "26", "1"], 
  "name": "Good keywords", 
  "orientation": "v", 
  "type": "bar", 
  "xsrc": "ksankaseam:6:691c40", 
  "ysrc": "ksankaseam:6:009ec7"
}
trace2 = {
  "x": ["ห้องน้ำ", "เดินทาง", "ไกล", "รถติด", "แพง"], 
  "y": ["1", "6", "6", "9", "4"], 
  "name": "Bad keywords", 
  "orientation": "v", 
  "type": "bar", 
  "xsrc": "ksankaseam:6:9531b3", 
  "ysrc": "ksankaseam:6:a8a063"
}
data = Data([trace1, trace2])
layout = {
  "autosize": True, 
  "colorway": ["#fbb4ae", "#b3cde3", "#ccebc5", "#decbe4", "#fed9a6", "#ffffcc", "#e5d8bd", "#fddaec", "#f2f2f2"], 
  "title": "Analysis of customer satisfaction from keywords", 
  "xaxis": {
    "autorange": True, 
    "range": [-0.5, 9.5], 
    "title": "Keywords", 
    "type": "category"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [0, 106.315789474], 
    "title": "Number of tweets", 
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
