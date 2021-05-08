import csv
import numpy as np 
import plotly.express as px

def setup():
    path='Student Marks vs Days Present.csv'
    dataSrc=getDataSource(path)
    findCorrelation(dataSrc)
    plotfigure(path)


def getDataSource(path):
    with open(path) as f:
        read=csv.DictReader(f)

        marks=[]
        days_present=[]
        
        for x in read:
            marks.append(float(x['Marks In Percentage']))
            days_present.append(float(x['Days Present']))

            return({
                "x":marks,
                "y":days_present
            })
def findCorrelation(dataSrc):
    corr=np.corrcoef(dataSrc['x'],dataSrc['y'])
    print("The correaltion between marks and no. of days present is: "+str(corr[0,1]))

def plotfigure(path):
    with open(path) as f:
        read=csv.DictReader(f)
        fig=px.scatter(read,x='Marks In Percentage',y='Days Present',color="Roll No",title="Correlation b/w marks and days present")
        fig.show()

setup()





