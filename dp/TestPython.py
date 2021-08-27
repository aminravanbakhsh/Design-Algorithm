import numpy as np
import random

if __name__ == '__main__':

   x = 0
   for i in range(1,9):
      x += 1/i

   z = 1/x

   print(z)

   h = 0
   for i in range(1,9):
      h += z / i * np.log(z/i)

   print(h)