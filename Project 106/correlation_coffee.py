import csv
import numpy as np 
import plotly.express as px

def setup():
    path='cups of coffee vs hours of sleep.csv'
    dataSrc=getDataSource(path)
    findCorrelation(dataSrc)
    plotfigure(path)


def getDataSource(path):
    with open(path) as f:
        read=csv.DictReader(f)

        marks=[]
        days_present=[]
        
        for x in read:
            marks.append(float(x['Coffee in ml']))
            days_present.append(float(x['sleep in hours']))

            return({
                "x":marks,
                "y":days_present
            })
def findCorrelation(dataSrc):
    corr=np.corrcoef(dataSrc['x'],dataSrc['y'])
    print("The correaltion between mls of coffee and no. of hours of sleep is: "+str(corr[0,1]))

def plotfigure(path):
    with open(path) as f:
        read=csv.DictReader(f)
        fig=px.scatter(read,x='Coffee in ml',y='sleep in hours',color="week",title="Correlation b/w coffee and hours of sleep")
        fig.show()

setup()





