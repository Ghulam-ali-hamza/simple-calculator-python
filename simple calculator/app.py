import streamlit as st

st.set_page_config(page_title="Simple Calculator", layout="centered")

# Custom CSS for pink background and bordered box
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
    }
    .stApp {
        background-color: #ffe6f0;
    }
    .box {
        border: 2px solid #d63384;
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Simple Calculator")

# Bordered container with pink background
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)

    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
            st.success(f"Result: {result}")
        elif operation == "Subtract":
            result = num1 - num2
            st.success(f"Result: {result}")
        elif operation == "Multiply":
            result = num1 * num2
            st.success(f"Result: {result}")
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Result: {result}")
            else:
                st.error("Cannot divide by zero.")

    st.markdown('</div>', unsafe_allow_html=True)

