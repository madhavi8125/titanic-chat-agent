from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# Load Titanic dataset
df = pd.read_csv("titanic.csv")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    q = query.question.lower()

    if "survived" in q:
        survived = int(df["Survived"].sum())
        return {"answer": f"{survived} passengers survived."}

    elif "male" in q:
        percent = (df["Sex"] == "male").mean() * 100
        return {"answer": f"{percent:.2f}% of passengers were male."}

    elif "fare" in q:
        avg = df["Fare"].mean()
        return {"answer": f"The average ticket fare was {avg:.2f}."}

    elif "embarked" in q:
        counts = df["Embarked"].value_counts().to_dict()
        return {"answer": f"Passengers by port: {counts}"}

    elif "age" in q:
        return {"answer": "Here is the age distribution histogram."}

    else:
        return {"answer": "Please ask a Titanic dataset related question."}