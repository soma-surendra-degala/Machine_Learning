import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

# ── Train model on startup (avoids pickle version issues) ──────────────
@st.cache_resource
def load_model():
    df = pd.read_csv("Bengaluru_House_Data.csv")

    # Handle missing values
    df['bath'] = df['bath'].fillna(df['bath'].median())
    df['balcony'] = df['balcony'].fillna(0)

    # Create BHK feature
    df['BHK'] = df["size"].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else 0)

    # Clean total_sqft
    def sqt_ft(x):
        try:
            if '-' in x:
                a, b = x.split('-')
                return (float(a) + float(b)) / 2
            return float(x)
        except:
            return np.nan

    df['total_sqft'] = df['total_sqft'].apply(sqt_ft)
    df = df.dropna(subset=['total_sqft'])

    # Price per sqft & remove outliers
    df["price_per_sqft"] = df['price'] * 1e5 / df['total_sqft']
    df = df[(df['price_per_sqft'] > 300) & (df['price_per_sqft'] <= 25000)]

    # Clean locations
    df = df.dropna(subset=['location'])
    df["location"] = df["location"].str.strip()
    loc_counts = df["location"].value_counts()
    rare_loc = loc_counts[loc_counts <= 10].index
    df['location'] = df["location"].apply(lambda x: 'Others' if x in rare_loc else x)

    # Features & target
    X = df[['location', 'total_sqft', 'bath', 'BHK']]
    y = df['price'] * 1e5

    # Pipeline
    preprocessor = ColumnTransformer([
        ('onehot', OneHotEncoder(handle_unknown='ignore'), ['location']),
        ('scaler', StandardScaler(), ['total_sqft', 'bath', 'BHK'])
    ])
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])
    pipe.fit(X, y)

    # Get sorted location list for dropdown
    locations = sorted([loc for loc in df['location'].unique() if isinstance(loc, str)])
    return pipe, locations


model, locations = load_model()
# ── Streamlit UI ─────────────────────────────────────────────
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="",
    layout="centered"
)

st.title("🏠 Bengaluru House Price Predictor")
st.write("Enter the property details to estimate the house price.")

st.divider()

# ---- Inputs ----
col1, col2 = st.columns(2)

with col1:
    location = st.selectbox("Location", locations)
    sqft = st.number_input("Total Square Feet", 300, 10000, 1200)

with col2:
    bath = st.number_input("Bathrooms", 1, 10, 2)
    bhk = st.number_input("BHK", 1, 10, 2)

st.write("")

predict = st.button("Predict Price")

# ---- Prediction ----
if predict:
    input_data = pd.DataFrame(
        [[location, sqft, bath, bhk]],
        columns=['location','total_sqft','bath','BHK']
    )

    prediction = model.predict(input_data)[0]
    price_lakhs = prediction / 1e5

    st.success(f"Estimated Price: ₹ {prediction:,.0f}")
    st.write(f"Approx **{price_lakhs:.2f} Lakhs**")