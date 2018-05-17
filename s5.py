import matplotlib.pyplot as plt
import random

x = [i for i in range(13)]

y = [random.randint(0, 9) for i in range(13)]

#print (x, y)
plt.plot(x, y)
plt.savefig('result.png')
plt.show()

print (0b0101000)
