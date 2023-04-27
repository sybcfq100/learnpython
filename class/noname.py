import numpy as np
import matplotlib.pyplot as plt
f = (lambda x: x * np.sin(x))(range(40))
#x = list(range(0, 4))
plt.plot(f)
plt.show()
#print (f)
