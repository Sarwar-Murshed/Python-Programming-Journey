import matplotlib.pyplot as plt

subjects = ['CSE', 'EEE', 'Math', 'English']
marks = [40, 25, 20, 15]

plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)

plt.title("Subject-wise Marks Distribution")

plt.show()
