import streamlit as st

def convert_temperature(temp, unit):
    if unit == "Celsius to Fahrenheit":
        return (temp * 9/5) + 32
    elif unit == "Fahrenheit to Celsius":
        return (temp - 32) * 5/9
    elif unit == "Celsius to Kelvin":
        return temp + 273.15
    elif unit == "Kelvin to Celsius":
        return temp - 273.15
    elif unit == "Fahrenheit to Kelvin":
        return (temp - 32) * 5/9 + 273.15
    elif unit == "Kelvin to Fahrenheit":
        return (temp - 273.15) * 9/5 + 32
    return temp

st.title("Temperature Converter")

temp = st.number_input("Enter Temperature:", format="%.2f")
unit = st.selectbox("Conversion Type:", [
    "Celsius to Fahrenheit", "Fahrenheit to Celsius",
    "Celsius to Kelvin", "Kelvin to Celsius",
    "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"
])

if st.button("Convert"):
    converted_temp = convert_temperature(temp, unit)
    st.success(f"Converted Temperature: {converted_temp:.2f}")
