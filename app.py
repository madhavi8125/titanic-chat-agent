import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Titanic Chat Agent")
st.title("🚢 Titanic Dataset Chat Agent")
st.write("Ask questions about the Titanic dataset in plain English!")

df = pd.read_csv("titanic.csv")

question = st.text_input("Ask a question:")

if st.button("Ask") and question:
    q = question.lower()

    if "survived" in q:
        survived = int(df["Survived"].sum())
        st.write(f"**Answer:** {survived} passengers survived.")

    elif "male" in q:
        percent = (df["Sex"] == "male").mean() * 100
        st.write(f"**Answer:** {percent:.2f}% of passengers were male.")

    elif "fare" in q:
        avg = df["Fare"].mean()
        st.write(f"**Answer:** The average ticket fare was {avg:.2f}.")

    elif "embarked" in q:
        st.write("**Passengers by Embarked Port:**")
        st.bar_chart(df["Embarked"].value_counts())

    elif "age" in q or "histogram" in q:
        st.write("**Age Distribution Histogram:**")
        fig, ax = plt.subplots()
        sns.histplot(df["Age"].dropna(), bins=20)
        st.pyplot(fig)

    else:
        st.write("Please ask a Titanic dataset related question.")