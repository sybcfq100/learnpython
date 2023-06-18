import numpy as np
import matplotlib.pyplot as plt

print('被除数为：')
a = input()
print('除数为：')
b = input()
c = int(a)//int(b)
d = int(a)%int(b)
print('%s 除 %s 商为 %d 余 %d' %(a,b,c,d))
