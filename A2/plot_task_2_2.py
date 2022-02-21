import matplotlib.pyplot as plt
import pandas as pd

# convert file to pandas data frame
df = pd.read_csv('results_22', delim_whitespace=True, header=None, index_col=0)

# Easier to work with dicts
values = (df.to_dict())[1]
nr_tweets = df[1].sum()

# Normalize
for (k,v) in values.items():
    values[k] = v / nr_tweets

# Convert to two lists
to_list = values.items()
(x,y) = zip(*to_list)

# Plot
plt.bar(x,y)
plt.xlabel("Pronoun")
plt.ylabel("Normalized nr of pronouns")
plt.show()
