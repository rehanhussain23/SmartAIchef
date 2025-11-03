import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
import random
import os
import streamlit as st  # added for caching support

# -------------------------------------------------
# Load dataset (Optimized + Cached)
# -------------------------------------------------
@st.cache_data(show_spinner=True)
def load_dataset(path="data/recipes_dataset.csv"):
    """
    Load and cache the recipe dataset.
    Prevents reloading the CSV on every Streamlit re-run.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}")

    df = pd.read_csv(path)

    # Normalize column names for consistency
    df.columns = [c.strip().lower() for c in df.columns]

    # Detect main columns
    possible_name_cols = ["translatedrecipename", "recipename", "name"]
    possible_ing_cols = ["cleaned-ingredients", "translatedingredients", "ingredients"]
    possible_cuisine_cols = ["cuisine"]
    possible_time_cols = ["totaltimeinmins", "time", "cook_time"]

    df["recipe_name"] = None
    df["ingredients"] = None
    df["cuisine"] = None
    df["time"] = None

    for c in possible_name_cols:
        if c in df.columns:
            df["recipe_name"] = df[c]
            break

    for c in possible_ing_cols:
        if c in df.columns:
            df["ingredients"] = df[c]
            break

    for c in possible_cuisine_cols:
        if c in df.columns:
            df["cuisine"] = df[c]
            break

    for c in possible_time_cols:
        if c in df.columns:
            df["time"] = df[c]
            break

    # Optional columns
    df["instructions"] = df["translatedinstructions"] if "translatedinstructions" in df.columns else ""
    df["image_url"] = df["image-url"] if "image-url" in df.columns else ""
    df["url"] = df["url"] if "url" in df.columns else ""

    # Drop incomplete rows
    df = df.dropna(subset=["recipe_name", "ingredients"]).reset_index(drop=True)

    return df

# -------------------------------------------------
# Find matching recipes by ingredients (Optimized)
# -------------------------------------------------
def find_recipes_by_ingredients(df, user_ingredients, min_score=40):
    """
    Fuzzy matches user ingredients with dataset ingredients.
    """
    user_ingredients = user_ingredients.lower().split(",")
    user_ingredients = [u.strip() for u in user_ingredients if u.strip()]

    results = []
    for _, row in df.iterrows():
        recipe_ings = str(row["ingredients"]).lower()
        score = np.mean([fuzz.partial_ratio(ui, recipe_ings) for ui in user_ingredients])
        if score >= min_score:
            results.append({
                "name": row["recipe_name"],
                "cuisine": row.get("cuisine", "Unknown"),
                "time": row.get("time", "N/A"),
                "ingredients": row.get("ingredients", ""),
                "instructions": row.get("instructions", ""),
                "url": row.get("url", ""),
                "image_url": row.get("image_url", "")
            })

    return sorted(results, key=lambda x: x["name"])[:15]  # limit top 15 results

# -------------------------------------------------
# Random recipe suggestions
# -------------------------------------------------
def get_random_recipes(df, n=5):
    """
    Returns a random selection of recipes.
    """
    if len(df) == 0:
        return []
    samples = df.sample(min(n, len(df))).to_dict(orient="records")
    result = []
    for s in samples:
        result.append({
            "name": s.get("recipe_name", "Unknown"),
            "cuisine": s.get("cuisine", "Unknown"),
            "time": s.get("time", "N/A"),
            "ingredients": s.get("ingredients", ""),
            "instructions": s.get("instructions", ""),
            "url": s.get("url", ""),
            "image_url": s.get("image_url", "")
        })
    return result

# -------------------------------------------------
# Display formatting
# -------------------------------------------------
def format_recipe(recipe):
    """
    Nicely formats recipe details for Streamlit display.
    """
    out = f"### 🍽️ {recipe['name']}\n"
    if recipe.get("cuisine"): 
        out += f"**Cuisine:** {recipe['cuisine']}\n\n"
    if recipe.get("time"): 
        out += f"**Time:** {recipe['time']} minutes\n\n"
    if recipe.get("ingredients"): 
        out += f"**Ingredients:**\n{recipe['ingredients']}\n\n"
    if recipe.get("instructions"): 
        out += f"**Instructions:**\n{recipe['instructions']}\n\n"
    if recipe.get("url"): 
        out += f"[🔗 View Full Recipe]({recipe['url']})\n"
    return out
