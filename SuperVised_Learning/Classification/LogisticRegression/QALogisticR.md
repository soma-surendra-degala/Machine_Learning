📘 Logistic Regression Interview Questions and Answers (Beginner to Advanced)

1. What is Logistic Regression?

        Logistic Regression is a Supervised Machine Learning Classification Algorithm used to predict the probability that an observation belongs to a particular class.
        Although its name contains Regression, it is primarily used for classification problems, especially Binary Classification.
   
        Examples:
        Spam / Not Spam
        Pass / Fail
        Purchased / Not Purchased
        Disease / No Disease

2. Why is it called Logistic Regression?

        It is called Logistic Regression because it uses the Logistic (Sigmoid) Function to model the probability of the target class.
        The algorithm first computes a linear equation and then passes the result through the Sigmoid Function.
        
        Linear Equation:  z=XW^T+b
        
        Sigmoid Function:  P=1/1+e^-z
	​

3. Is Logistic Regression a Regression or Classification algorithm?

        Although its name includes "Regression," it is a Classification Algorithm.
        
        Reason:
        Linear Regression predicts continuous values.
        Logistic Regression predicts probabilities and class labels.


4. Why can't we use Linear Regression for Classification?

        Linear Regression predicts values from −∞ to +∞.
   
        Example:
                  -2.5
                  1.8
                  5.2
        
        These are not valid probabilities.
        Logistic Regression uses the Sigmoid Function to ensure predictions are always between 0 and 1.

5. What is the Sigmoid Function?

        The Sigmoid Function converts a linear score into a probability.
        
        Formula:
                Sigmoid Function:  P=1/1+e^-z
   
        Properties:
                Output ranges from 0 to 1
                Smooth S-shaped curve
                Differentiable
                Used to calculate probabilities

6. Why do we use the Sigmoid Function?
        
        The Sigmoid Function:
                Converts any real number into a probability
                Makes outputs easy to interpret
                Enables binary classification
                Supports gradient-based optimization
   
7. What is the output of Logistic Regression?

        Logistic Regression produces:
   
        Probability: 0.83
        Class Prediction: 1
   
        The probability is converted to a class using a threshold, usually 0.5.

8. What is a Decision Threshold?

       A Decision Threshold converts predicted probabilities into class labels.
    
        Default threshold: 0.5
   
        Rule:
        Probability ≥ 0.5 → Class 1
        Probability < 0.5 → Class 0
       

10. What is the Cost Function used in Logistic Regression?

        Logistic Regression uses Log Loss (Binary Cross-Entropy Loss).
    
        Formula: J(θ) = -1/m(∑[ylog(h)+(1−y)log(1−h)])
        
        The objective is to minimize this loss during training.

10. Why doesn't Logistic Regression use Mean Squared Error (MSE)?

        MSE is not suitable because:     
                  The Sigmoid Function is non-linear.
                  MSE results in a non-convex optimization problem.
                  Gradient Descent may converge slowly or get stuck.

        Log Loss provides a smoother optimization surface for classification.

11. What optimization algorithm is used?
Answer

        Logistic Regression commonly uses optimization algorithms such as:
         1. Gradient Descent
         2. Stochastic Gradient Descent (SGD)
         3. LBFGS (default in scikit-learn)
         4. Newton-CG
         5. SAG
         6. SAGA

        These algorithms update the model weights to minimize Log Loss.

12. What is Gradient Descent?

        Gradient Descent is an optimization algorithm used to minimize the cost function by updating the model parameters.
        
        Update Rule: w=w−α∂w/∂J
    
        Where:
        α = Learning Rate
        J = Cost Function
    
14. What is a Decision Boundary?

        A Decision Boundary separates different classes in the feature space.
        For example:
    
                  Purchased | Not Purchased
                  -----------|--------------
        Everything on one side belongs to one class, and everything on the other side belongs to the other class.

15. What assumptions does Logistic Regression make?
    
            Independent observations
            Little or no multicollinearity
            Large sample size
            Linear relationship between features and the log-odds of the outcome
            Minimal influence of extreme outliers

16. What are Odds and Log-Odds?

        Odds
                  Odds =  P/1−P
        Example
        
            Probability = 0.80
        
            Odds = 0.8/0.2 = 4
        
        Meaning:
            The event is 4 times more likely to occur than not occur.
        
        Log-Odds (Logit)
              log(P/1−P)
        
        Logistic Regression models the log-odds as a linear combination of the input features.

17. What evaluation metrics are used?

          Common evaluation metrics: 
                    Accuracy
                    Precision
                    Recall
                    F1-Score
                    Confusion Matrix
                    ROC-AUC

                          Predicted positive     Predicted negative
        Actual positive          TP 32                  FN 12
        Actual negative          FP 8                   TN 48

        Accuracy: (TP + TN) ÷ (TP + FP + FN + TN) = (80) ÷ (100) = 80%
        Precision: (TP) ÷ (TP + FP) = (32) ÷ (40) = 80%
        Recall: (TP) ÷ (TP + FN) = (32) ÷ (44) = 72.7%
        Specificity: (TN) ÷ (TN + FP) = (48) ÷ (56) = 85.7%
        F1 score: (2TP) ÷ (2TP + FP + FN) = (64) ÷ (84) = 76.2%
    
17. What is Precision?

        Precision answers:
                "Out of all predicted positives, how many were actually positive?"
        Formula:
                  Precision: (TP) ÷ (TP + FP)
    
        Use when False Positives are costly, such as spam filtering.

19. What is Recall?

        Recall answers:
                "Out of all actual positives, how many did the model correctly identify?"
        Formula:
               Recall: (TP) ÷ (TP + FN)	​

        Use when False Negatives are costly, such as disease detection.

19. What is the F1 Score?

        The F1 Score is the harmonic mean of Precision and Recall.
        
        Formula
        
        F1=2×(Precision + Recall / Precision × Recall)
        	
        Useful when classes are imbalanced.

20. What is ROC-AUC?
    
        ROC Curve plots the True Positive Rate against the False Positive Rate across different thresholds.
        AUC (Area Under the Curve) summarizes how well the model distinguishes between classes.
        General interpretation:
              1.0 → Perfect
              0.9 → Excellent
              0.8 → Good
              0.5 → Random guessing

21. What are the advantages of Logistic Regression?
    
        Simple and easy to understand
        Fast to train
        Highly interpretable
        Produces probabilities
        Performs well on linearly separable data
        Works well as a baseline model
    
22. What are the limitations of Logistic Regression?
    
        Assumes a linear relationship in the log-odds
        Cannot naturally capture complex non-linear patterns
        Sensitive to multicollinearity
        Performance depends on feature engineering
        May underperform compared to more flexible models on complex datasets

23. What is the difference between predict() and predict_proba()?

        predict()
              Returns the predicted class label.
        Example:
            model.predict(X_test)
        Output:
              [0 1 1 0]
        
        predict_proba()
        Returns the probability for each class.
        
        Example:
        model.predict_proba(X_test)
        Output:
        [[0.92 0.08]
         [0.10 0.90]]
    
24. How do you handle imbalanced datasets?

        Common approaches include:
            Using class_weight='balanced'
            Oversampling (e.g., SMOTE)
            Undersampling
            Adjusting the decision threshold
            Evaluating with Precision, Recall, F1, and ROC-AUC instead of Accuracy alone

25. When would you choose Logistic Regression over Decision Trees?

        Choose Logistic Regression when:
              The relationship is approximately linear in the log-odds.
              You need an interpretable model.
              You want probability estimates.
              The dataset is relatively small or medium-sized.
              Fast training and inference are important.
        
        Choose Decision Trees when:
              Relationships are highly non-linear.
              Complex feature interactions are expected.
              Interpretability through decision rules is preferred.
    
26. Real Interview Question
Interviewer

Suppose your Logistic Regression model gives 95% Accuracy, but your client says the model is poor. How is that possible?

      Accuracy alone can be misleading for imbalanced datasets. 
      Example:
      95 healthy patients
      5 patients with a disease
      If the model predicts every patient as healthy, it achieves:
      Accuracy = 95%

However, it detects none of the diseased patients, making the model ineffective.

In such cases, metrics like Precision, Recall, F1-Score, and ROC-AUC provide a more complete evaluation than Accuracy alone.
