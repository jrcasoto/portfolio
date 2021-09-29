# Pima Indians Diabetes Database - [Source](https://www.kaggle.com/jucasoto/pima-indians-diabetes-database/data)

### Context
This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

### Content
The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

### Acknowledgements
Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus. In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265). IEEE Computer Society Press.

### About this file (diabetes.csv)
The datasets consist of several medical predictor (independent) variables and one target (dependent) variable, Outcome. Independent variables include the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.

### Inspiration/problem to be solved
Can you build a machine learning model to accurately predict whether or not the patients in the dataset have diabetes or not?

### Solution
For this project it was developed a pipeline comparing three different classification models: KNN, Logistic Regression and Random Forest. All three models were tested using cross-validation (KFold) and Logistic regression model was chosen for this problem. In addition, two optimization approaches were done in order to check if there could be any improvements in our current model: Recursive Feature Elimination (or RFE) and Random Search Parameter Tuning (RandomizedSearchCV), but changes were insignificant.

You'll find the full-analysis in **Pima Indians Diabetes Database.ipynb** notebook and deployed model in /models/regrl_classifier.sav.

Enjoy! :smile:
