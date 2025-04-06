import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_scores.csv")

df = df.drop("Unnamed: 0", axis = 1)

df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct", "5-10")

#Gender Distribution
plt.figure(figsize= (5, 5))
ax = sns.countplot(data = df, x = "Gender")
ax.bar_label(ax.containers[0])
#plt.show()

# number of females is more than the number of males

gb = df.groupby("ParentEduc").aggregate({"MathScore" : 'mean', "ReadingScore" : 'mean', "WritingScore": 'mean'})
plt.figure(figsize= (4, 4))
sns.heatmap(gb, annot = True)
#plt.show()

#education of parents has good impact on student's scores

gb1 = df.groupby("ParentMaritalStatus").aggregate({"MathScore" : 'mean', "ReadingScore" : 'mean', "WritingScore": 'mean'})
plt.figure(figsize= (4, 4))
sns.heatmap(gb1, annot = True)
#plt.show()

# martial status of parents has negligible impact on student's scores

sns.boxplot(data = df, x = "ReadingScore")
sns.boxplot(data = df, x = "WritingScore")
sns.boxplot(data = df, x = "MathScore")
#plt.show()

#print(df["EthnicGroup"].unique())

groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()

l = ["groupA", "groupB", "groupC", "groupD", "groupE"]
mlist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
plt.pie(mlist, labels = l, autopct= "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
#plt.show()


