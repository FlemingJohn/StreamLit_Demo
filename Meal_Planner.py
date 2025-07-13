import streamlit as st
import pandas as pd
import numpy as np

# title of the app
st.title("🥗 Healthy Meal Planner")

# inpit calorie goal 
calorie_goal = st.number_input("Enter your daily caloreies goal")

# Sample meals
meals = pd.DataFrame({
    "Meal": ["Oatmeal", "Grilled Chicken Salad", "Fruit Smoothie", "Paneer Wrap", "Veggie Stir Fry"],
    "Calories": [250, 350, 180, 400, 300]
})

# show meals on the goal 
st.write("Meals that fit within your goal")

filtered_meals = meals[meals["Calories"] <= calorie_goal]
st.dataframe(filtered_meals)

