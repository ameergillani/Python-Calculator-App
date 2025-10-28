
import streamlit as st

# App title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator App")
st.write("Perform basic arithmetic operations using this Streamlit app.")

# Input fields
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox(
    "Select operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
            st.success(f"The sum is: {result}")
        elif operation == "Subtraction (-)":
            result = num1 - num2
            st.success(f"The difference is: {result}")
        elif operation == "Multiplication (×)":
            result = num1 * num2
            st.success(f"The product is: {result}")
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                st.success(f"The quotient is: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")
