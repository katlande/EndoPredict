import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier

# training data:
X = pd.read_csv("/Users/kathrynlande/Git_Repos/EndoPredictor/Model_Data/Training_Unscaled.csv")
y = pd.read_csv("/Users/kathrynlande/Git_Repos/EndoPredictor/Model_Data/Training_IDs.csv")
X2 = pd.read_csv("/Users/kathrynlande/Git_Repos/EndoPredictor/Model_Data/Training_Scaled.csv")

# testing data:
p = pd.read_csv("/Users/kathrynlande/Git_Repos/EndoPredictor/Model_Data/Testing_Unscaled.csv")
p2 = pd.read_csv("/Users/kathrynlande/Git_Repos/EndoPredictor/Model_Data/Testing_Scaled.csv")
p_true = pd.read_csv("/Users/kathrynlande/Git_Repos/EndoPredictor/Model_Data/Testing_IDs.csv")

# fit various models with the raw and scaled FPKMs and check predictions:
# Linear SVC classifier
model = LinearSVC(max_iter=10000)
model.fit(X, np.ravel(y))
p_true["rawFPKM_LinearSVC"] = model.predict(p)
model.fit(X2, np.ravel(y))
p_true["scaledFPKM_LinearSVC"] = model.predict(p2)

# SVC Ensemble classifier
model = SGDClassifier()
model.fit(X, np.ravel(y))
p_true["rawFPKM_SGDC"] = model.predict(p)
model.fit(X2, np.ravel(y))
p_true["scaledFPKM_SGDC"] = model.predict(p2)

# KNeighbors classifier
model = KNeighborsClassifier()
model.fit(X, np.ravel(y))
p_true["rawFPKM_KN"] = model.predict(p)
model.fit(X2, np.ravel(y))
p_true["scaledFPKM_KN"] = model.predict(p2)

# decision tree classifier
model = DecisionTreeClassifier()
model.fit(X, np.ravel(y))
p_true["rawFPKM_DTree"] = model.predict(p)
model.fit(X2, np.ravel(y))
p_true["scaledFPKM_DTree"] = model.predict(p2)

# logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X, np.ravel(y))
p_true["rawFPKM_logReg"] = model.predict(p)
model.fit(X2, np.ravel(y))
p_true["scaledFPKM_logReg"] = model.predict(p2)

# random forest
model = RandomForestClassifier()
model.fit(X, np.ravel(y))
p_true["rawFPKM_logReg"] = model.predict(p)
model.fit(X2, np.ravel(y))
p_true["scaledFPKM_logReg"] = model.predict(p2)

# Gaussian
model = RandomForestClassifier()
model.fit(X, np.ravel(y))
p_true["rawFPKM_gauss"] = model.predict(p)
model.fit(X2, np.ravel(y))
p_true["scaledFPKM_gauss"] = model.predict(p2)

model = MLPClassifier()
model.fit(X, np.ravel(y))
p_true["rawFPKM_MLPC"] = model.predict(p)
model.fit(X2, np.ravel(y))
p_true["scaledFPKM_MPLC"] = model.predict(p2)

# save prediction comparisons as csv:
p_true.to_csv("/Users/kathrynlande/Git_Repos/EndoPredictor/Model_Data/Predictions.csv", index=False)