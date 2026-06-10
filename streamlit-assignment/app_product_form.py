import streamlit as st

st.title("Product Form")

product_name = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Books", "Home Appliances", "Sports"]
)

price = st.sidebar.number_input(
    "Price",
    min_value=0.0,
    step=1.0
)

if st.sidebar.button("Add Product"):
    st.success("Product added successfully!")

    st.subheader("Product Details")
    st.write("**Product Name:**", product_name)
    st.write("**Category:**", category)
    st.write("**Price:** ₹", price)