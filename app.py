import streamlit as st # type: ignore
import pandas as pd
from joblib import load
from sklearn.preprocessing import LabelEncoder

# Load the trained Random Forest model
model = load('./model/products_campaign_sales.joblib')

st.sidebar.success("Products Campaign Sales Pridiction.")
st.image('./image/mg.png')
st.write("# Welcome to Yash Patoliya's Machine Learning Projects!! 👋")

st.markdown(
        """

        **👈 Select a demo from the dropdown on the left to see some examples of the ML models I've built!

        ### Want to learn more?

        - Check out my [GitHub](https://github.com/yashpatoliya)
        - Follow me on [LinkedIn](https://www.linkedin.com/in/yash-patoliya-1a19b021a)
    """
    )

# Create a Streamlit app
st.title("Product Campaign Sales Prediction")

# Input fields for feature values on the main screen
st.header("Enter Limit Info For")
limit_infor = st.number_input("limit_infor", min_value=0, max_value=1, value=0)

st.header("Enter Campaign Type")
campaign_type = st.number_input("campaign_type", min_value=0, max_value=6, value=0)

st.header("Enter Campaign Level")
campaign_level = st.number_input("campaign_level", min_value=0, max_value=6, value=0)

st.header("Enter Product Level")
product_level = st.number_input("product_level", min_value=0, max_value=6, value=0)

st.header("Enter Resource Amount")
resource_amount = st.number_input("resource_amount", min_value=0, max_value=6, value=0)

st.header("Enter Email Rate")
email_rate = st.number_input("email_rate", min_value=0, max_value=1, value=0)

st.header("Enter Price")
price = st.number_input("price", min_value=0, max_value=9999, value=0)

st.header("Enter Discount Rate")
discount_rate = st.number_input("discount_rate", min_value=0, max_value=1, value=0)

st.header("Enter Hour Resource")
hour_resouces = st.number_input("hour_resouces", min_value=0, max_value=9999, value=0)

st.header("Enter Campaign Fee")
campaign_fee = st.number_input("campaign_fee", min_value=0, max_value=9999, value=0)

# Make a prediction using the model
prediction = model.predict([[limit_infor ,campaign_type,campaign_level,product_level,resource_amount,email_rate,price,discount_rate,hour_resouces,campaign_fee]])
print(prediction)

# Display the prediction result on the main screen
st.header("Prediction Sales Result")
if prediction[0] :
    st.balloons()
    st.success(prediction[0])
else:
    st.error(prediction)