import csv
import plotly.express as px
import numpy as np

def showScatterChart():
    with open('C:/Users/C/OneDrive/Desktop/Coding/python/Correlation/StudentMarksVsDaysPresent.csv') as f:
        data = csv.DictReader(f)
        scatterPlot = px.scatter(data, x="DaysPresent", y="Marks(%)", title="Marks VS. Days Present")
        scatterPlot.show()

def getData(data_path):
    daysPresent = []
    marks = []

    with open(data_path) as f:
        data = csv.DictReader(f)
        for rows in data:
            daysPresent.append(float(rows["DaysPresent"]))
            marks.append(float(rows["Marks(%)"]))
        
    return{'x': daysPresent, 'y': marks}

def getCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print('This is the correlation between the days present and the marks earned: ', correlation[0,1])

def setup():
    data_path = "C:/Users/C/OneDrive/Desktop/Coding/python/Correlation/StudentMarksVsDaysPresent.csv"
    data_source = getData(data_path)
    
    getCorrelation(data_source)
    showScatterChart()

setup()