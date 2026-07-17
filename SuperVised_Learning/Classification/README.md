

# Mathematical Explanation of Logistic Regression

Logistic Regression is a **Supervised Machine Learning Classification Algorithm** used to predict the probability of an observation belonging to a particular class.

Unlike Linear Regression, which predicts continuous values, Logistic Regression predicts probabilities between **0 and 1**.

---

# Step 1: Linear Combination

The first step in Logistic Regression is to compute a linear combination of the input features.

Mathematical Equation

    \[
    z = w_1x_1 + w_2x_2 + w_3x_3 + \cdots + w_nx_n + b
    \]

or in vector form,

    \[
    z = W^TX + b
    \]

Where:

    - **x₁, x₂, ..., xₙ** → Input Features
    - **w₁, w₂, ..., wₙ** → Model Weights (Coefficients)
    - **b** → Bias (Intercept)
    - **z** → Linear Score

---

## Example

Suppose we have two features:

- Age = 30
- Salary = 50000

Weights learned by the model:

- Weight for Age = 0.08
- Weight for Salary = 0.00003

      Bias = -4

Then,

    \[
    z=(0.08\times30)+(0.00003\times50000)-4
    \]

    \[
    z=2.4+1.5-4
    \]
    
    \[
    z=-0.1
    \]

This value can be any real number.

For example:

- -100
- -2
- 0
- 5
- 100

Since this is **not a probability**, we need another function.

---

# Step 2: Sigmoid Function

The Sigmoid Function converts any real number into a probability between **0 and 1**.

The mathematical formula is

    \[
    \sigma(z)=\frac{1}{1+e^{-z}}
    \]

Where
    
    - **σ(z)** = Probability
    - **e** = Euler's Number (≈2.718)
    - **z** = Linear Score

---

## Example

Suppose

    \[
    z=2
    \]

Then

    \[
    P=\frac{1}{1+e^{-2}}
    \]

    \[
    P=\frac{1}{1+0.1353}
    \]

    \[
    P=0.881
    \]

This means there is an **88.1% probability** that the sample belongs to the positive class.

---

Another Example

Suppose

    \[
    z=-3
    \]

Then

    \[
    P=\frac{1}{1+e^3}
    \]
    
    \[
    P=0.047
    \]

Only **4.7% probability**.

---

# Why Sigmoid?

The Sigmoid Function has several useful properties:

- Output always lies between **0 and 1**
- Smooth and continuous curve
- Differentiable (important for optimization)
- Converts linear scores into probabilities

Its graph is S-shaped.

        ```
        Probability
        
        1.0           ********
                    ***
                 ***
        0.5  ****
             **
           **
         **
        0----------------------------
              Negative      Positive
        ```
        
        ---

# Step 3: Decision Threshold

After obtaining the probability, the model converts it into a class label.

Usually,

    Threshold = 0.5

Decision Rule

If
  
      \[
      P \ge 0.5
      \]

Predict

Class = 1

Otherwise

Class = 0

Example

| Probability | Prediction |
|-------------|------------|
| 0.92 | Purchased |
| 0.81 | Purchased |
| 0.45 | Not Purchased |
| 0.18 | Not Purchased |

---

# Step 4: Cost Function (Log Loss)

To measure prediction error, Logistic Regression uses **Binary Cross-Entropy Loss**, also called **Log Loss**.

The loss function is

    \[
    J(\theta)=
    -\frac{1}{m}
    \sum_{i=1}^{m}
    \left[
    y_i\log(h_\theta(x_i))
    +
    (1-y_i)\log(1-h_\theta(x_i))
    \right]
    \]

Where

- **m** = Number of training samples
- **y** = Actual class
- **h(x)** = Predicted probability

### Why not Mean Squared Error (MSE)?

Although MSE works well for Linear Regression, it is not suitable for Logistic Regression because:

- The Sigmoid function is non-linear.
- Using MSE creates a non-convex optimization problem with multiple local minima.
- Log Loss provides a smooth, convex optimization surface, making Gradient Descent more reliable.

---

# Step 5: Gradient Descent

The objective is to minimize the Log Loss by updating the model parameters.

Weight Update Rule

    \[
    w=w-\alpha\frac{\partial J}{\partial w}
    \]

Bias Update Rule

    \[
    b=b-\alpha\frac{\partial J}{\partial b}
    \]

Where

    - **α** = Learning Rate
    - **J** = Cost Function
    - **∂J/∂w** = Gradient of the Cost Function

Gradient Descent repeats the following steps:

1. Compute predictions.
2. Calculate Log Loss.
3. Compute gradients.
4. Update weights and bias.
5. Repeat until the loss converges.

---

# Step 6: Prediction Process

The complete mathematical workflow is

```
Input Features
       │
       ▼
Linear Equation

z = WᵀX + b
       │
       ▼
Sigmoid Function

P = 1 / (1 + e⁻ᶻ)
       │
       ▼
Probability
       │
       ▼
Threshold (0.5)
       │
       ▼
Class Prediction
```

---

# Numerical Example

Suppose

Age = 35

Estimated Salary = 60000

Weights

w₁ = 0.05

w₂ = 0.00004

Bias = -3

### Step 1

    \[
    z=(0.05\times35)+(0.00004\times60000)-3
    \]
    
    \[
    z=1.75+2.4-3
    \]
    
    \[
    z=1.15
    \]

### Step 2

Apply Sigmoid

    \[
    P=\frac{1}{1+e^{-1.15}}
    \]
    
    \[
    P=0.759
    \]

### Step 3

Since

    \[
    0.759>0.5
    \]

The prediction is

**Purchased (Class = 1)**

---

# Summary

The mathematical steps in Logistic Regression are:

1. Compute the linear score:

        \[
        z=W^TX+b
        \]

2. Convert the score into a probability using the Sigmoid Function:

        \[
        P=\frac{1}{1+e^{-z}}
        \]

3. Compute the prediction error using Log Loss.

4. Update the model parameters using Gradient Descent.

5. Apply a threshold (usually 0.5) to convert the probability into the final class label.

This combination of a linear model, Sigmoid function, Log Loss, and Gradient Descent makes Logistic Regression one of the most effective and interpretable algorithms for binary classification problems.
