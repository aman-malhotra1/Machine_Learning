# I want to know the total "returns" for all rows-ranges that start with "status" 1 followed by "status" 2 till status = 0 again.
# Some ranges start with "status" 2, in those cases I'm not interested. It should only count "returns" values if the range starts with 1 followed by 2.
# It should also set "position" column to 1 if the above is true.

import numpy as np
import pandas as pd

mylist = pd.read_csv("list.csv")
status_ = []
returns_ =[]
total = []
def myfunction(status,returns):
    status_.append(status)
    returns_.append(returns)
    if status_[len(status_)-1] == 0:
        if status_[len(status_)-2] == 2:
            if 1 in status_[len(status_)-3:0:-1]:
                total.extend(returns_[status_.index(1):len(status_)-1])
                status_.clear()
                returns_.clear()

mylist.apply(lambda x : myfunction(x['status'], x['returns']), axis=1)
print(total)
print(np.sum(total))