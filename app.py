import streamlit as st

# Title
st.title("Simple Calculator App")

# User input
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Operation selection
operation = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    st.success(f"Result: {result}")
