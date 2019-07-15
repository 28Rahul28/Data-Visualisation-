
import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(1000),
        'c': np.random.randint(50, 1000, 1000),
        'd': np.random.randn(1000)}
data['b'] = data['a'] + 10 * np.random.randn(1000)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
