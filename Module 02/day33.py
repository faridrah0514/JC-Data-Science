import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

x = np.array([1,2,3,4,5])
y = x

myFig=go.Figure(
    data=go.Bar(x=x, y=y)
)
myFig.show()