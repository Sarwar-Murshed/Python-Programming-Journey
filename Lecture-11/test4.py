import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 30, 25]
y2 = [20,30,40,60,110]

plt.plot(x, y1, label = 'Sales 2025')  #y1 plot data
plt.plot(x, y2, label = 'Sales 2026')  #y2 plot data

plt.title("YoY sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()
plt.show()