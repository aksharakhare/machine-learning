import pandas as pd
import numpy as np

og_data=pd.read_csv("../binder/adult.csv",names=["Age","Workclass","fnlwgt","Education","Education-num","Marital Status","Occupation","Relationship","Race","Gender","Capital Gain","Capital Loss","Hours per Week","Country","Target"],sep=r'\s*,\s*',engine='python',na_values="?")
og_data.head()

import matplotlib.pyplot as plt
import math

%matplotlib inline



fig=plt.figure(figsize=(20,20))
cols=3
rows=math.ceil(float(og_data.shape[1])/cols)

for i,column in enumerate(["Age","Workclass","Education","Occupation","Race","Gender"]):
    ax=fig.add_subplot(rows,cols,i+1)
    ax.set_title(column)
    if og_data.dtypes[column]==np.object:
        og_data[column].value_counts().plot(kind="bar",axes=ax)
    else:
        og_data[column].hist(axes=ax)
        plt.xticks(rotation="vertical")
plt.subplots_adjust(hspace=0.7,wspace=0.2)
plt.show()




import sklearn.preprocessing as skp

le=skp.LabelEncoder()
og_data["Occupation"]=le.fit_transform(og_data["Occupation"].astype(str))
og_data.head()

og_data["Target"]=le.fit_transform(og_data["Target"].astype(str))
og_data.tail()
og_data.Target.unique()

og_data.groupby("Education-num").Target.mean().plot(kind="bar")
plt.show()




from sklearn.model_selection import train_test_split

X=og_data[["Education-num","Occupation"]]
Y=og_data["Target"]

X_train,x_test,Y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.svm import SVC

classifier=SVC()

classifier.fit(X_train,Y_train)
score=classifier.score(x_test,y_test)
print(score)

from 

