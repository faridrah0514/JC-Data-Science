# import matplotlib.pyplot as plt
import sys
import numpy as np

# import matplotlib.pyplot as plt

from matplotlib import pyplot as plt
x, y = np.loadtxt('misc/data.txt', delimiter=',', unpack=True)
# np.loadtxt bisa jg dipakai utk CSV

plt.plot(x, y, label='Data dari file')
plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend()
plt.show()

np.swapaxes