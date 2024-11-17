from numpy import arange
from pandas import read_csv
from pandas import read_csv
import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.metrics import roc_auc_score
from joblib import Parallel, delayed
import joblib

###### Load New dataset on which you want to predict ##########

test_url = 'test.csv'
dataframe = read_csv(test_url, header=None)
data_test = dataframe.values
X_test, y_test = data_test[:, :-1], data_test[:, -1]


##### Load the model ################

loaded_model = joblib.load('RF_model.sav')        ### User can change 'RF_model.sav' to 'SVM_model.sav' if they want to use the SVM based model

# Make predictions on the test set
y_pred_prob = loaded_model.predict_proba(X_test)[:, 1]

# Calculate AUROC
auroc = roc_auc_score(y_test, y_pred_prob)

# Print AUROC
print(f'AUROC: {auroc}')
