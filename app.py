import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Titanic Dataset Chat Agent")

st.title("🚢 Titanic Dataset Chat Agent")
st.write("Ask questions about the Titanic dataset in plain English!")

# Load dataset
df = pd.read_csv("titanic.csv")

# Input box
question = st.text_input("Ask a question:")

if st.button("Ask") and question:

    try:
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )

        result = response.json()

        st.subheader("Answer:")
        st.write(result["answer"])

    except:
        st.error("Backend is not running. Please start FastAPI server.")

    # Visualizations
    if "age" in question.lower():
        st.subheader("Age Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df["Age"].dropna(), bins=20)
        st.pyplot(fig)

    if "embarked" in question.lower():
        st.subheader("Passengers by Embarked Port")
        st.bar_chart(df["Embarked"].value_counts())