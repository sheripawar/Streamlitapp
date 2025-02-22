import streamlit as st

def convert_currency(amount, currency):
    exchange_rates = {
        "INR": 1,
        "USD": 0.012,
        "GBP": 0.0095,
        "EUR": 0.011,
        "Pounds": 0.0095
    }
    return amount * exchange_rates.get(currency, 1)

st.title("Currency Converter")

amount = st.number_input("Enter amount in Rupees:", min_value=0.0, format="%.2f")
currency = st.selectbox("Convert to:", ["INR", "USD", "GBP", "EUR", "Pounds"])

if st.button("Convert"):
    converted_amount = convert_currency(amount, currency)
    st.success(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
