import pandas as pd
import plotly.express as pe
import numpy
data=pd.read_csv("coffeVsleep.csv")
fig=pe.scatter(data,x="Coffee in ml",y="sleep in hours")
#fig.show()
ten=data["Coffee in ml"]
tep=data["sleep in hours"]
correlation=numpy.corrcoef(ten,tep)
print(correlation[0,1])