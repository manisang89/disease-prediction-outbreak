# **AI-Based Disease Prediction Using Machine Learning**

## **1. Introduction**  

### **Problem Statement**  
The increasing prevalence of **Diabetes, Heart Disease, and Parkinson’s Disease** demands **early detection** for better treatment outcomes. Traditional methods require expert analysis, whereas **Machine Learning (ML)** can provide fast and accurate predictions.  

### **Motivation**  
Early diagnosis can **reduce mortality rates and improve treatment success**. This project aims to build ML models that assist in predicting diseases efficiently.  

### **Objectives**  
- Develop **ML models** for disease prediction.  
- Compare different ML techniques and improve performance.  
- Deploy a **user-friendly web application** using Streamlit.  

## **2. Literature Survey**  
Machine learning has shown significant potential in medical diagnosis. Research has explored algorithms such as **SVM, Decision Trees, and Random Forest** for disease classification. A key challenge is handling **imbalanced datasets**, which can lead to biased predictions.  

To tackle this, resampling techniques like **SMOTE (oversampling) and Tomek Links (undersampling)** were explored. These methods improve model reliability, ensuring minority class cases (disease cases) are not overlooked.  

## **3. Proposed Methodology**  

### **System Design**  
The system follows these steps:  
1. **Data Collection:** Medical datasets for diabetes, heart disease, and Parkinson’s.  
2. **Preprocessing:** Handling missing values, feature scaling, and balancing data.  
3. **Model Selection:** Training models using **SVM, Decision Trees, Random Forest, and Logistic Regression**.  
4. **Evaluation:** Comparing accuracy, precision, and recall.  
5. **Deployment:** Hosting on **Streamlit** for real-time predictions.  

### **Tools & Technologies Used**  
- **Programming Language:** Python 3.x  
- **Libraries:** Scikit-learn, Pandas, NumPy, Streamlit, Imbalanced-learn  
- **Model Storage:** Pickle  

## **4. Implementation and Results**  

### **Model Performance Summary**  

| Disease    | Model             | Resampling Technique | Accuracy | Precision | Recall  |
|-----------|------------------|----------------------|----------|-----------|---------|
| Diabetes  | SVM              | None                 | 77.0%    | 80.0%     | 53.9%   |
| Diabetes  | Decision Tree    | None                 | 70.9%    | 58.4%     | 63.4%   |
| Diabetes  | Random Forest    | None                 | 78.7%    | 61.7%     | 78.5%   |
| Heart     | Decision Tree    | Tomek Links          | 76.9%    | 68.6%     | 87.5%   |
| Heart     | Logistic Regression | None              | 91.2%    | 96.0%     | 89.1%   |
| Parkinson | SVM              | None                 | 88.1%    | 97.7%     | 87.8%   |
| Parkinson | SVM              | SMOTE                | 86.5%    | 80.0%     | 95.2%   |
| Parkinson | Random Forest    | SMOTE                | 95.5%    | 94.0%     | 97.9%   |

### **Key Observations:**  
- **Logistic Regression performed best for Heart Disease (91.2% accuracy).**  
- **Random Forest (SMOTE) had the highest accuracy for Parkinson’s (95.5%).**  
- **SMOTE improved recall for Parkinson’s detection.**  


## **5. Discussion and Conclusion**  

### **Future Work:**  
- Expand dataset diversity for better generalization.  
- Explore deep learning models for improved accuracy.  
- Extend the system to predict additional diseases.  

### **Conclusion:**  
This project successfully developed an **ML-based disease prediction system** with high accuracy. The integration of **SMOTE and Tomek Links** improved prediction reliability for minority class cases. The deployment on **Streamlit** makes it accessible for real-time medical predictions. Future improvements will focus on **deep learning** and **real-world validation with healthcare professionals**.  

## **References**  
- **Scikit-learn Documentation:** [https://scikit-learn.org/](https://scikit-learn.org/)  
- **Streamlit Documentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)  
- **SMOTE (Oversampling) Reference:** [https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)  
- **Tomek Links (Undersampling) Reference:** [https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.TomekLinks.html](https://imbalanced-learn.org/stable/references/generated/imblearn.under_sampling.TomekLinks.html)  
