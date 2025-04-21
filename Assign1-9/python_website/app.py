import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Advanced Python Website", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Charts", "Upload Files", "Data Table", "Fun with AI"])

if page == "Home":
    st.title("Welcome to the Advanced Streamlit Website")
    st.write("""
    This website demonstrates how you can create interactive content using Python and Streamlit.
    Explore the sidebar to see more features!
    """)

elif page == "Charts":
    st.title("Dynamic Charts and Data Visualizations")

    data = np.random.randn(1000)
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color="blue", alpha=0.7)
    st.pyplot(fig)

    st.subheader("Line Chart")
    line_data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
    st.line_chart(line_data)

elif page == "Upload Files":
    st.title("File Upload")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            else:
                st.write(uploaded_file.read().decode("utf-8"))
                df = None

            if df is not None:
                st.write("File Uploaded Successfully!")
                st.dataframe(df)
        except Exception as e:
            st.error(f"Error: {e}")

elif page == "Data Table":
    st.title("Interactive Data Table")
    df = pd.DataFrame({
        "Name": ["Ali", "Danial", "Umar", "Sara"],
        "Age": [35, 39, 25, 46],
        "City": ["Karachi", "Lahore", "Abbotabad", "Islamabad"],
    })
    st.dataframe(df)

elif page=="Fun with AI":
    st.title("Chat with AI")
    st.write("Ask me anything and I'll try to answer!")
    user_input = st.text_input("Your Question:")
    st.button("Ask AI")
    st.success("The Message was sent successful!")

st.markdown("---")
st.markdown("**Created with ❤️ using Python and Streamlit**")
