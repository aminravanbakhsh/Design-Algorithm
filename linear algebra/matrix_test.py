import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    a = np.random.randint(0, 10, (3,3))
    at = a.T
    a_inv = np.linalg.inv(a)
    print(a)
    print(np.linalg.inv(at))
    print(a_inv.T)