import numpy as np

prices = np.array([100,200,300])
disount = 10 #scalar vlaue 

final_prices = prices - (prices * disount / 100)
print(final_prices)