import numpy as np, seaborn as sns, matplotlib.pyplot as plt

x = np.random.normal(size=500)
sns.histplot(x, kde=True)
plt.show()
