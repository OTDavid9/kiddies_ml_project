from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model_path = "playkit_recommender.pkl"
similarity_matrix, label_encoders, play_kit_df, child_df = joblib.load(model_path)

# Initialize FastAPI
app = FastAPI(title="AI Play Kit Recommender", version="1.0")

# Define the request schema
class ChildRequest(BaseModel):
    Age: int
    Developmental_Stage: str
    Cognitive_Ability: str
    Interest: str
    Play_Style: str
    Special_Needs: str

# Recommendation function
async def recommend_play_kits(new_child: ChildRequest):
    """ Recommend play kits for a new child using the saved model """
    new_child_df = pd.DataFrame([new_child.dict()])  # Convert Pydantic object to dictionary

    # Encode categorical features
    for col in ["Developmental_Stage", "Cognitive_Ability", "Interest", "Play_Style", "Special_Needs"]:
        value = getattr(new_child, col)  # ✅ Correct way to access Pydantic attributes
        if value not in label_encoders[col].classes_:
            raise HTTPException(status_code=400, detail=f"Invalid value for {col}: {value}")
        new_child_df[col] = label_encoders[col].transform([value])[0]

    # Normalize Age
    new_child_df["Normalized_Age"] = (new_child_df["Age"] - child_df["Age"].min()) / (child_df["Age"].max() - child_df["Age"].min())

    # Compute similarity
    play_kit_features = play_kit_df[["Normalized_Age", "Stage", "Cognitive_Skill_Targeted", "Interest", "Min_Age", "Max_Age"]]
    similarity_scores = similarity_matrix[new_child_df.index[0]]
    top_kits = similarity_scores.argsort()[-3:][::-1]  # Get top 3 recommendations

    # Return recommendations
    recommended_play_kits = play_kit_df.iloc[top_kits]["Kit_Name"].values.tolist()
    return {"Recommended_Play_Kits": recommended_play_kits}

# API Endpoint for Play Kit Recommendation
@app.post("/recommend/")
async def get_recommendations(child: ChildRequest):
    try:
        recommendations = await recommend_play_kits(child)
        return recommendations
    except HTTPException as e:
        return {"error": e.detail}
    except Exception as e:
        return {"error": str(e)}

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to AI Play Kit Recommender API 🚀"}

