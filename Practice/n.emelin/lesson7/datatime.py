from datetime import date
import numpy as np

a = date(2019, 3, 1)
b = date(2019, 4, 9)
days = np.busday_count(a, b)
print(days)