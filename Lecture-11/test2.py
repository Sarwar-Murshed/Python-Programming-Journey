import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [20,30,40,60,110]

plt.figure(figsize = (4,3))  # figure size

plt.plot(x,y,color = 'blue', marker = 'o', linestyle = 'dashed', linewidth = 2, markersize = 10)

plt.show()