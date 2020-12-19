import numpy as np
import pandas as pd
import time 

from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, GridSearchCV, RandomizedSearchCV, validation_curve
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, f1_score, precision_score, auc, roc_curve, auc,plot_roc_curve

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

import numpy as np
import pandas as pd
import time 

from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, GridSearchCV, RandomizedSearchCV, validation_curve
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, f1_score, precision_score, auc, roc_curve, auc,plot_roc_curve
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

import pickle
#data = {'text':'Hola como estas?'}
# MATRIZ DISPERSA
text = ['sale offer product free']
modelo_tfidf_2=pickle.load(open('predict_model\modelo_tfidf_2.sav', 'rb'))
X_testing_2= pd.DataFrame(modelo_tfidf_2.transform(text).toarray())

print(X_testing_2)

#XGBOOST
model_GB_2 = pickle.load(open('predict_model\model_GB_2.sav', 'rb'))
y_pred_proba_testing_2 = model_GB_2.predict_proba(X_testing_2)
y_pred_testing_2=[1 if m > 0.367 else 0 for m in y_pred_proba_testing_2[:,1]]
print(y_pred_testing_2[0])