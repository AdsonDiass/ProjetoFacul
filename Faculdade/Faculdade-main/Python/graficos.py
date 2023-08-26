import matplotlib.pyplot as plt
import random
import seaborn as sns

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.plot(dados1,dados2)


#countplot
df = sns.load_dataset("titanic")
sns.countplot(x=df["class"])
#scartterplot
sns.scatterplot(data=tips,x="total_bill",y="tip")


