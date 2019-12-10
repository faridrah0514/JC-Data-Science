import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig=plt.figure()
ax=fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax2=fig.add_axes([0.2,0.5,0.4,0.3])
x=np.linspace(-20,20,50)
x2=x*10
y=x**2 + 2*x -2

ax.plot(x,y)
# plt.plot(x,y,color='red', marker='o')
# plt.plot(x2,y, color='blue', linestyle='dashed')
# plt.xlabel('ini x')
# plt.ylabel('ini y')
# plt.legend(['test', 'anu'])
# plt.title('ini adalah judul')
plt.show()