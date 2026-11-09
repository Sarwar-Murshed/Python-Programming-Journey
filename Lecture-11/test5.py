import numpy as np

import matplotlib.pyplot as plt

x = np.arange(-5, 6)
plt.plot(x, x ** 2, 'b-o')
plt.xlabel('x')
plt.ylabel('x squared')
plt.title('y = x^2')

plt.show()