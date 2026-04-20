# 🍽️ FlavorGen AI / FlavorHub

**AI-powered restaurant concept generator** that instantly creates a complete culinary brand — including a **restaurant name, curated menu, and chef recommendations** — based on selected cuisine.

Built using **Streamlit + LangChain + Groq LLM**, this project transforms a simple input into a refined dining concept.

---

## 🚀 Features

* 🎨 **Elegant UI** with modern dark-theme design (custom CSS)
* 🍛 **Cuisine Selection** (Indian, Italian, Mexican, Japanese, etc.)
* 🏷️ **AI-Generated Restaurant Name**
* 📜 **Signature Menu Creation** (8 curated dishes)
* 👨‍🍳 **Chef’s Recommendations** with descriptions
* ⚡ **Fast LLM responses** powered by Groq (LLaMA 3.3)

---

## 🖼️ Preview

![App Screenshot](./assets/screenshot.png)

> Replace the path with your actual screenshot file

---

## 🧠 Tech Stack

* **Frontend/UI**: Streamlit
* **LLM Framework**: LangChain
* **Model Provider**: Groq (LLaMA 3.3 70B)
* **Environment Management**: python-dotenv

---

## 📂 Project Structure

```
├── app.py                  # Main Streamlit app
├── langchain_helper.py     # LLM logic (LangChain + Groq)
├── requirements.txt        # Dependencies
├── .env                    # API keys (not committed)
└── assets/
    └── screenshot.png      # App preview image
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flavorgen-ai.git
cd flavorgen-ai
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧩 How It Works

1. User selects a cuisine from the sidebar
2. App calls `generate_restaurant_name_and_items()`
3. LangChain pipelines:

   * Generates **restaurant name**
   * Generates **menu items**
   * Generates **chef recommendation**
4. Results are displayed in a styled UI

---

## 💡 Example Output

* **Restaurant Name**: *Tandoor Mahal*
* **Menu Items**:

  * Chicken Tikka Masala
  * Garlic Naan
  * Lamb Korma
  * Vegetable Biryani
* **Chef’s Pick**:

  * Signature seasonal dish with description

---

## 📦 Dependencies

From `requirements.txt`:

* langchain
* langchain-groq
* huggingface_hub
* streamlit
* python-dotenv

---

## 🔮 Future Improvements

* 🍽️ Add **image generation for dishes**
* 🌍 Support **more cuisines & fusion concepts**
* 💰 Dynamic pricing using AI
* 📊 Save/export restaurant concepts
* 🧾 PDF menu generation

---

## 🤝 Contributing

Contributions are welcome!

```bash
fork → create branch → commit → push → pull request
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Yugaram**
Crafting AI-powered creative applications 🚀

---
