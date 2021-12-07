import csv
import plotly.express as px
import numpy as np

def showScatterChart():
    with open('C:/Users/C/OneDrive/Desktop/Coding/python/Correlation/TVSizeVsWatchingTime.csv') as f:
        data = csv.DictReader(f)
        scatterPlot = px.scatter(data, x="TVSize", y="AVGtime", title="Size of the TV vs. Hours spent watching the tv")
        scatterPlot.show()

def getData(data_path):
    tvSize = []
    avgTime = []

    with open(data_path) as f:
        data = csv.DictReader(f)
        for rows in data:
            tvSize.append(float(rows["TVSize"]))
            avgTime.append(float(rows["AVGtime"]))
        
    return{'x': tvSize, 'y': avgTime}

def getCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print('This is the correlation between the size of a TV and the hours spent watching it: ', correlation[0,1])

def setup():
    data_path = "C:/Users/C/OneDrive/Desktop/Coding/python/Correlation/TVSizeVsWatchingTime.csv"
    data_source = getData(data_path)
    
    getCorrelation(data_source)
    showScatterChart()

setup()