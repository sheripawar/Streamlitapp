st.markdown("""
    <style>
        .title {
            color: blue;
            font-size: 30px;
            font-weight: bold;
        }
        .header {
            color: green;
            font-size: 24px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">CALCULATOR</p>', unsafe_allow_html=True)
st.markdown('<p class="header">ENTER YOUR NUMBERS</p>', unsafe_allow_html=True)

num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)


operation = st.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("Division by zero is not allowed!")
