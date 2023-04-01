import panda as pd
imprt numpy as np
data = pd.read_csv("data.csv")
print(data)
concepts = np.array(data)[:,:-1]
print("\ninstances are\n\n",concepts)
target = np.array(data)[:,-1]
print("\nTarget values are: ",target)

def train(con, tar):
    for i, val in enumurate(tar):
	if val == 'yes':
	    specific_h=con[i].copy()
	    break
	for i, val in enumurate(con):
	    for x in range (len(specific_h)):
		if val[x] != specific_h[x]:
		    specific_h[x] = '?'
		else:
		    pass
		return specific_h
print("Most specific Hypothesis : \n\n",train(concepts,target))

