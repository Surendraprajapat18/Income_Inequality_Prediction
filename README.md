# 💵 Income Inequality Prediction Machine Learning Project

# 🧾**Description:** 
Income inequality - when income is distributed unevenly among a population - is a growing problem in developing nations worldwide. With the rapid rise of AI and worker automation, this problem could continue to grow if steps are not taken to address the issue. This solution can potentially reduce the cost and improve the accuracy of monitoring key population indicators such as income level in between census years. This information will help policymakers to manage better and avoid income inequality globally.

# 🧭 **Problem Statement:** 
The target feature is **income_above_limit** which is a binary-class variable. This challenge aims to create a machine learning model to predict whether an individual earns above or below a certain amount. Your metric for evaluation will be **f1-score**

I followed these steps to complete the project.

**Project Flow**
_____➡️_____
**Data collection**
_____➡️_____
**EDA(Exploratory Data Analysis)**
_____➡️_____
**Data Preprocessing**
_____➡️_____
**Feature Engineering**
_____➡️_____
**Data Modelling**
________________

### Data Collection:
Gathered a dataset containing information about individuals, including features related to income and the binary target variable, "income_above_limit." The source of data is from The Machine Learning Company. (Confidential Not Disclosed)

## Data Preprocessing:
Cleaned and preprocessed the data, which involved handling missing values, and treating imbalanced Data.
![image](https://github.com/Surendraprajapat18/Income_Inequality_Prediction/assets/97840357/f0634602-f97e-4abd-90a7-56c7564be93c)

![image](https://github.com/Surendraprajapat18/Income_Inequality_Prediction/assets/97840357/580f324f-b774-46fa-8fd4-53170d839027)

### Feature Engineering:
Performed Feature Engineering, Which involved Encoding Techniques like hot Encoding for Categorical features, feature selection on numerical and categorical
columns

### Model Building:
Trained a few Supervised Machine Learning Algorithms namely Logistic Regression, K-Nearest Neighbors, and Decision Tree Classifier. Based on the F1 scores, the Random Forest Classifier (0.9059) outperformed other algorithms including Logistic Regression (0.8911), K-Nearest Neighbors (0.8884), and Decision Tree Classifier (0.8975). I made use of a Random Forest Classifier as My Final Model and Performed hyperparameter tunning, which resulted in a slight improvement from 90.59% to 90.77%.
![image](https://github.com/Surendraprajapat18/Income_Inequality_Prediction/assets/97840357/2e7ddc7d-e345-4260-8252-66b347e6d72b)

### Model Evaluation:
Used the F1-score as the primary evaluation metric to assess the model's performance on a test dataset. Confusion Matrix and ROC Curve are also used to check the Performance of the Model.
![image](https://github.com/Surendraprajapat18/Income_Inequality_Prediction/assets/97840357/414e37b3-43e1-4f6d-825b-22e80f44b271)


Model deployment:
Model deployed using AWS EC2 cloud service.
