import streamlit as st

st.title("Price Calculator")

price=st.number_input("Enter Price :", min_value=0.0)
discount=st.slider("Select Discount % ", 0,50,10)

if st.button("Calculate"):
    final_price = price - (price * discount / 100)

    st.success(f"Final Price: {final_price}")

    st.table([
        ["Before Discount :", price],
        ["After Discount :", final_price]
    ])
