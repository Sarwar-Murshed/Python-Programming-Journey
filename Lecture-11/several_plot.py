import numpy as np

import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.1)
plt.figure(figsize=(8, 3))

plt.subplot(1, 2, 1) # 1 row, 2 columns, first plot

plt.plot(x, np.sin(x))
plt.title('sin(x)')

plt.subplot(1, 2, 2) # second plot

plt.hist(np.random.randn(500), bins=15) # histogram of random numbers
plt.title('Random data')
plt.tight_layout()
plt.show()