import streamlit as st
from utils import load_dataset, find_recipes_by_ingredients, get_random_recipes, format_recipe

# -------------------------------------------------
# App setup
# -------------------------------------------------
st.set_page_config(page_title="SmartChef AI", page_icon="🍳", layout="wide")

st.title("🍳 SmartChef AI")
st.markdown("### Discover delicious recipes using the ingredients you already have at home!")

# Load dataset
@st.cache_data
def get_data():
    return load_dataset()

df = get_data()

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.header("🔧 Options")
mode = st.sidebar.radio("Choose mode:", ["Find Recipes by Ingredients", "Random Recipes"])

# -------------------------------------------------
# Ingredient-based search
# -------------------------------------------------
if mode == "Find Recipes by Ingredients":
    st.subheader("Enter your ingredients (comma-separated):")
    user_input = st.text_input("Example: tomato, onion, garlic, rice")

    if st.button("Search Recipes 🍽️"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter at least one ingredient!")
        else:
            with st.spinner("Finding the best recipes for you..."):
                results = find_recipes_by_ingredients(df, user_input)
                if len(results) == 0:
                    st.error("No recipes found! Try adding more ingredients or using common items.")
                else:
                    st.success(f"Found {len(results)} matching recipes!")
                    for recipe in results:
                        with st.expander(f"🍲 {recipe['name']} ({recipe['cuisine']})"):
                            if recipe.get("image_url"):
                                st.image(recipe["image_url"], use_container_width=True)
                            st.markdown(format_recipe(recipe))

# -------------------------------------------------
# Random recipe discovery
# -------------------------------------------------
elif mode == "Random Recipes":
    st.subheader("🎲 Explore random recipes from around the world!")
    if st.button("Show Me Recipes"):
        random_recipes = get_random_recipes(df, n=5)
        for recipe in random_recipes:
            with st.expander(f"🍛 {recipe['name']} ({recipe['cuisine']})"):
                if recipe.get("image_url"):
                    st.image(recipe["image_url"], use_container_width=True)
                st.markdown(format_recipe(recipe))

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.markdown("Made with ❤️ by Nadeem & Rehan | SmartChef AI | Powered by Streamlit")
