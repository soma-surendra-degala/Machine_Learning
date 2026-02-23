📈 Linear Regression — Mathematical Explanation 

This project explains Simple Linear Regression mathematically (without ML libraries).

Independent Variable (X): Years of Experience
Dependent Variable (Y): Salary

1️⃣ Linear Regression Equation

    Y_hat = b0 + b1 * X

Where:

Y_hat = Predicted Salary

b0 = Intercept

b1 = Slope

X = Years of Experience

2️⃣ Step-by-Step Mathematical Formulas
Step 1: Calculate Mean

    X_mean = (Sum of X values) / n
    Y_mean = (Sum of Y values) / n

Step 2: Calculate Slope (b1)

             [ Σ (Xi − X_mean)(Yi − Y_mean) ]
     b1 =   ------------------------------------
                     [Σ (Xi − X_mean)²]
  
This tells how much Salary increases for every 1 year increase in Experience.

Step 3: Calculate Intercept (b0)

     b0 = Y_mean − (b1 * X_mean)

3️⃣ Calculated Values (From Dataset)

    b1 = 9449.96
    b0 = 25792.20

4️⃣ Final Regression Model

    Salary = 25792.20 + 9449.96 * (Years of Experience)

📊 5️⃣ Error Measurement
Sum of Squared Errors (SSE)

    SSE = Σ (Yi − Y_hat_i)²

Where:

    Y_hat_i = b0 + b1 * Xi

Mean Squared Error (MSE)

    MSE = (1 / n) * Σ (Yi − Y_hat_i)²

    MSE ≈ 31,250,000

Lower MSE = Better model performance.

📌 6️⃣ Example Prediction
For 7.5 Years of Experience

    Salary = 25792.20 + 9449.96 * 7.5
  
    Salary = 25792.20 + 70874.70

    Salary = 96666.90

Final Predicted Salary ≈ ₹96,667


🎯 Key Takeaway

Machine Learning models always use:

Full precision floating-point numbers

That’s why:

    Manual Rounded ≠ Exact Model Output
