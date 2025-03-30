# 🧠 AI Play Kit Recommendation System  

## 📌 Overview  
This project builds an AI-powered recommendation system that suggests **cognitive play kits** for children aged **6 months to 16 years**. The system uses **content-based filtering** with **cosine similarity** to match children’s attributes to suitable play kits.  

---

## 📂 Project Structure  


---

## 📊 Data Description  

### **1️⃣ Child Data (`child_data.csv`)**
| Column Name            | Description                                     |
|------------------------|-------------------------------------------------|
| Age                   | Child's age in years                            |
| Developmental_Stage   | Growth stage (e.g., Toddler, Pre-Teen)         |
| Cognitive_Ability     | Cognitive skill level (e.g., Logical Thinking) |
| Interest             | Child’s interest (e.g., STEM, Art)              |
| Play_Style           | Preferred play type (e.g., Solo, Group)         |
| Special_Needs        | Any special learning needs                      |

---

### **2️⃣ Play Kit Data (`play_kit_data.csv`)**
| Column Name               | Description                                    |
|---------------------------|------------------------------------------------|
| Kit_Name                 | Name of the play kit                           |
| Stage                    | Suitable developmental stage                   |
| Cognitive_Skill_Targeted | Cognitive skill it improves                   |
| Interest                 | Targeted interests (e.g., Robotics, Arts)     |
| Recommended_Age          | Age range (e.g., 3-6, 10-12 years)            |

---

## 🚀 Training the AI Model  

The `train_model.py` script:  
1️⃣ Loads **child and play kit data**  
2️⃣ **Encodes categorical features** using `LabelEncoder`  
3️⃣ Computes **cosine similarity** to measure compatibility  
4️⃣ Saves the trained model using `joblib`  

### **🔹 Train and Save the Model**
```python
from train_model import train_and_save_model

train_and_save_model()  # Trains and saves the model
