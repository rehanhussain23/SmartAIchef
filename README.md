---

## 🧠 SmartChef AI

**Your Personal AI-Powered Recipe Assistant 🍳**

SmartChef AI helps users discover delicious recipes using ingredients they already have at home.
Just type what’s in your kitchen, and SmartChef instantly finds matching dishes, suggests creative new ones, and even estimates calories — all powered by AI and smart data filtering.

---

### 🚀 Features

✅ **Ingredient-Based Recipe Search** — Find recipes using what you have
✅ **AI-Style Recipe Ideas** — Generate creative dishes on the fly
✅ **Smart Similarity Matching** — Uses fuzzy logic to find near matches
✅ **Calorie Estimation** — Get quick, rough calorie estimates
✅ **Random Recipe Discovery** — Explore new dishes just for fun
✅ **Simple, Beautiful UI** — Powered by Streamlit

---

### 🗂 Project Structure

```
SmartChef_AI/
│
├── smartchef_streamlit.py     # Streamlit UI frontend
├── smartchef_gui.py           # Bridge between UI and logic
├── utils.py                   # Core backend functions (recipe logic)
├── recipes.csv                # Dataset of recipes
├── main_code.py               # (Optional) Backend testing file
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

---

### ⚙️ Installation & Setup

#### 1️⃣ Clone or Download the Project

```bash
git clone https://github.com/yourusername/SmartChef-AI.git
cd SmartChef-AI
```

#### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Add Your Recipe Dataset

Make sure a CSV file named **`recipes.csv`** exists in the same folder.
It should include at least these columns:

```
name, ingredients, instructions
```

*(You can use your own dataset or download one from Kaggle — e.g., “Indian Recipes Dataset” or “All-Cuisine Recipes.”)*

#### 4️⃣ Run the App

```bash
streamlit run smartchef_streamlit.py
```

#### 5️⃣ Open in Browser

After launching, Streamlit will show a local URL like:
👉 `http://localhost:8501`
Open it in your browser to use SmartChef!

---

### 🧩 How It Works

| Component                  | Description                                                                                                    |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **utils.py**               | Handles core logic: dataset loading, ingredient cleaning, recipe filtering, fuzzy matching, calorie estimation |
| **smartchef_gui.py**       | Connects logic with the frontend, prepares formatted recipe cards                                              |
| **smartchef_streamlit.py** | Streamlit interface that displays results interactively                                                        |
| **recipes.csv**            | Your dataset — the heart of SmartChef                                                                          |

---

### 💡 Example Usage

**Input:**

```
egg, tomato, onion
```

**Output:**

* Egg Tomato Curry 🍛
* Quick Omelette Wrap 🥚
* Spicy Breakfast Mix 🌶️

SmartChef will also show:

* Match %
* Estimated Calories
* Step-by-step Instructions

---

### 🧰 Future Enhancements

🚧 Planned features:

* 🗣️ Voice-based ingredient input
* 📱 Mobile-friendly responsive design
* 🧾 Nutritional breakdown using real data
* 🤖 ChatGPT integration for dynamic recipe generation

---

### 👨‍💻 Developed By

**Nadeem Khan**
*Computer & Data Science Student | Passionate about AI, ML, and Smart Automation*

---

### 📝 License

This project is open-source and free to use for educational and research purposes.

---