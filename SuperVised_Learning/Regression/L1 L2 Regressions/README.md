
Ridge (L2) and Lasso (L1) Regression

Machine Learning models sometimes overfit the training data.

Overfitting happens when the model learns the training data too well, including noise. As a result, the model performs very well on training data but performs poorly on new unseen data.

One main reason for overfitting is that the model learns very large coefficients.

To control this problem, we use a technique called Regularization.

Two common regularization methods are:

    Ridge Regression (L2)
    Lasso Regression (L1)

1. Linear Regression Mathematical Form

Linear Regression models the relationship between input features and output using a linear equation.

General form:

    y = b0 + b1x1 + b2x2 + ... + bnxn

Where

y = predicted value
x = input features
b0 = intercept
b1, b2, ... bn = coefficients

The model learns these coefficients by minimizing the error between actual and predicted values.

The most common error function used is Mean Squared Error (MSE).

Loss Function:

    Loss = Sum of (actual value − predicted value)²

The goal of linear regression is to find coefficients that minimize this loss.

2. Ridge Regression (L2 Regularization)

Ridge Regression modifies the loss function by adding a penalty for large coefficients.

Ridge Loss Function:

    Loss = Sum of (y − y_pred)² + lambda × Sum of (coefficient²)

Where

lambda = regularization parameter
coefficient² = square of model coefficients

So the model now tries to minimize:

Error + penalty for large coefficients

Why this works:

If coefficients become large, the squared value becomes large, increasing the penalty. This forces the model to keep coefficients small.

Effect of Ridge Regression:

• Reduces coefficient size
• Reduces model complexity
• Helps prevent overfitting

Important point:

Ridge shrinks coefficients but never makes them exactly zero.

3. Ridge Regression Mathematical Solution

The normal solution for Linear Regression is:

    beta = (XᵀX)⁻¹ Xᵀy

Ridge modifies it to:

    beta = (XᵀX + lambda I)⁻¹ Xᵀy

Where

I = identity matrix

Adding lambda × I stabilizes the matrix and prevents extreme coefficient values.

4. Lasso Regression (L1 Regularization)

Lasso Regression also adds a penalty term but in a different way.

Lasso Loss Function:

    Loss = Sum of (y − y_pred)² + lambda × Sum of |coefficient|

Instead of squaring the coefficients, Lasso uses the absolute value of coefficients.

Effect of Lasso:

• Shrinks coefficients
• Can make some coefficients exactly zero

When a coefficient becomes zero, that feature is effectively removed from the model.

Because of this, Lasso automatically performs feature selection.

5. Simple Numerical Example

Suppose we have a simple dataset.

    Size | Price
      1 | 2
      2 | 4
      3 | 6

The real relationship is:

    Price = 2 × Size

Now imagine the model learned:

    Price = 3 × Size

    Coefficient = 3

This coefficient is larger than necessary.

Example with Ridge

Suppose:

    Error = 5
    lambda = 1
    coefficient = 3

    Penalty term = coefficient²

    Penalty = 3² = 9

    Total Loss = 5 + 9 = 14

Now try a smaller coefficient:

    coefficient = 2

    Penalty = 2² = 4

    Total Loss = 5 + 4 = 9

Since the loss is smaller, the model prefers smaller coefficients.

    This is how Ridge shrinks coefficients.

Example with Lasso

Suppose we have two features:

    y = 5x1 + 0.2x2

Feature x2 has very little importance.

    Because Lasso penalizes coefficients, it may shrink x2's coefficient to zero.

New model:

    y = 5x1 + 0x2

    So the feature x2 is removed.

    This is why Lasso performs feature selection.

6. Key Differences

       Linear Regression
       Minimizes only prediction error.

Ridge Regression
    
    Minimizes error + squared coefficient penalty.

Lasso Regression

    Minimizes error + absolute coefficient penalty.

7. Final Intuition

Regularization tells the model:

    Fit the data well, but keep coefficients small.

This prevents the model from memorizing the training data and helps it perform better on unseen data.
