import matplotlib.pyplot as plt
import pandas as pd

# convert file to pandas data frame
df = pd.read_csv('words_that_start_with_a_or_A', delim_whitespace=True, header=None, index_col=0)

# Easier to work with dicts
values = (df.to_dict())[1]

# Convert to two lists
to_list = values.items()
(x,y) = zip(*to_list)

plt.bar(x,y)
plt.xlabel("different words starting on letter")
plt.ylabel("Occurences of word")
plt.show()
