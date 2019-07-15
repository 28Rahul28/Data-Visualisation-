import matplotlib.pyplot as plt

names = ['RAM', 'SURESH', 'RAMESH']
marks = [98, 54, 80]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, marks)
plt.subplot(132)
plt.scatter(names, marks)
plt.subplot(133)
plt.plot(names, marks)
plt.suptitle('Internal Marks')
plt.show()

