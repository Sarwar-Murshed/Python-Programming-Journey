# bar chart

import matplotlib.pyplot as plt 

x = ['A','B','C','D','E']
y = [10,20,17,25,5]

plt.bar(x,y, color = 'green')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bar Diagram")
plt.show()