import pandas as pd
import random

# Define age categories and their characteristics
age_categories = [
    {"min_age": 0.5, "max_age": 2, "stage": "Infant", "cognitive_skills": ["Sensory Exploration", "Grasping"], "interests": ["Soft Toys", "Rattles", "Music"]},
    {"min_age": 2, "max_age": 5, "stage": "Toddler", "cognitive_skills": ["Basic Problem Solving", "Shape Recognition"], "interests": ["Puzzles", "Building Blocks", "Drawing"]},
    {"min_age": 5, "max_age": 8, "stage": "Early Childhood", "cognitive_skills": ["Logical Thinking", "Memory"], "interests": ["Board Games", "STEM Kits", "Storytelling"]},
    {"min_age": 8, "max_age": 12, "stage": "Middle Childhood", "cognitive_skills": ["Analytical Thinking", "Creativity"], "interests": ["Robotics", "Strategy Games", "Coding"]},
    {"min_age": 12, "max_age": 16, "stage": "Adolescence", "cognitive_skills": ["Critical Thinking", "Abstract Reasoning"], "interests": ["AI & ML Kits", "Engineering", "Advanced Puzzles"]}
]

# Generate 15,000 children data
children_data = []
for _ in range(15000):
    category = random.choice(age_categories)
    age = round(random.uniform(category["min_age"], category["max_age"]), 1)
    cognitive_ability = random.choice(category["cognitive_skills"])
    interest = random.choice(category["interests"])
    play_style = random.choice(["Solo", "Group", "Interactive Digital"])
    special_needs = random.choice(["None", "Autism", "ADHD", "Dyslexia", "None", "None"])  # More children without special needs

    children_data.append([age, category["stage"], cognitive_ability, interest, play_style, special_needs])

# Convert to DataFrame and save
child_df = pd.DataFrame(children_data, columns=["Age", "Developmental_Stage", "Cognitive_Ability", "Interest", "Play_Style", "Special_Needs"])
child_df.to_csv("child_data.csv", index=False)

# Define 10 play kits with suitable age range and cognitive skills targeted
play_kits = [
    ["Soft Sensory Mat", "0.5-2", "Infant", "Sensory Exploration", "Soft Toys"],
    ["Colorful Stacking Blocks", "2-5", "Toddler", "Basic Problem Solving", "Building Blocks"],
    ["Shape Sorting Cube", "2-5", "Toddler", "Shape Recognition", "Puzzles"],
    ["STEM Learning Kit", "5-8", "Early Childhood", "Logical Thinking", "STEM Kits"],
    ["Memory Card Game", "5-8", "Early Childhood", "Memory", "Board Games"],
    ["Coding Robot", "8-12", "Middle Childhood", "Analytical Thinking", "Robotics"],
    ["Strategy Board Game", "8-12", "Middle Childhood", "Creativity", "Strategy Games"],
    ["DIY Engineering Set", "12-16", "Adolescence", "Critical Thinking", "Engineering"],
    ["AI & ML Learning Kit", "12-16", "Adolescence", "Abstract Reasoning", "AI & ML Kits"],
    ["Advanced Puzzle Set", "12-16", "Adolescence", "Critical Thinking", "Advanced Puzzles"],
]

# Convert to DataFrame and save
play_kit_df = pd.DataFrame(play_kits, columns=["Kit_Name", "Recommended_Age", "Stage", "Cognitive_Skill_Targeted", "Interest"])
play_kit_df.to_csv("play_kit_data.csv", index=False)

# Return file paths
print("child_data.csv and play_kit_data.csv generated successfully.")
