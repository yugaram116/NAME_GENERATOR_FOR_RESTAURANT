import streamlit as st
import re
from langchain_helper import generate_restaurant_name_and_items

# ── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="Flavor Hub",
    page_icon="🍽️",
    layout="centered"
)

# ── Styling ─────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Josefin+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Josefin Sans', sans-serif;
}

.stApp {
    background-color: #0a0c14;
}

section[data-testid="stSidebar"] {
    background-color: #0e1220;
    border-right: 1px solid #1e2a4a;
}

section[data-testid="stSidebar"] * {
    color: #f0e6c8 !important;
}

.stButton > button {
    width: 100%;
    background-color: #1a3368;
    color: #f0e6c8;
    border: 1px solid #2c4a8a;
    border-radius: 4px;
    font-size: 12px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    padding: 12px 28px;
}

.stButton > button:hover {
    background-color: #234280;
}
</style>
""", unsafe_allow_html=True)

# ── Data ────────────────────────────────────────────────────
CUISINE_EMOJI = {
    "Indian": ["🍛","🫓","🍢","🥘","🫕","🍲"],
    "Italian": ["🍝","🍕","🥗","🍷","🧀","🥩"],
    "Mexican": ["🌮","🌯","🥑","🌶️","🍹"],
    "Japanese": ["🍣","🍜","🍱","🍤"],
    "French": ["🥐","🍷","🧀","🥩"],
    "Greek": ["🫒","🥗","🐟","🍋"],
    "Chinese": ["🥟","🍜","🍚","🥡"],
}

PRICE_RANGE = ["₹320","₹450","₹395","₹520","₹480","₹290"]
REC_EMOJI = ["🌟","👨‍🍳","🏆"]

# ── Helpers ─────────────────────────────────────────────────
def section_header(label):
    st.markdown(f"""
    <div style="padding:1rem 0;">
        <p style="letter-spacing:0.25em;color:#4a7fd4;
                  text-transform:uppercase;font-size:10px;">
            {label}
        </p>
        <hr>
    </div>
    """, unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:2rem;">
    <h1 style="font-family:'Cormorant Garamond',serif;
               color:#f0e6c8;font-weight:300;">
        Flavor<span style="color:#4a7fd4;">Hub</span>
    </h1>
    <p style="color:#4a5a7a;letter-spacing:0.2em;font-size:10px;">
        Haute cuisine concept atelier
    </p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ─────────────────────────────────────────────────
st.sidebar.markdown("### Select Cuisine")

cuisine = st.sidebar.selectbox(
    "",
    ["Indian","Italian","Mexican","Japanese","French","Greek","Chinese"]
)

# ✅ Updated Button
generate = st.sidebar.button("Generate Restaurant")

# ── Generation ──────────────────────────────────────────────
if generate:
    with st.spinner("Curating your restaurant..."):
        result = generate_restaurant_name_and_items(cuisine)

    # ── Restaurant Name ─────────────────────────────────────
    st.markdown(f"""
    <div style="text-align:center;padding:1.5rem;">
        <p style="font-size:10px;letter-spacing:0.2em;color:#4a7fd4;">
            Establishment Name
        </p>
        <h2 style="font-family:'Cormorant Garamond',serif;
                   color:#f0e6c8;">
            {result.get("restaurant_name")}
        </h2>
    </div>
    """, unsafe_allow_html=True)

    # ── Concept Narrative (FIXED) ───────────────────────────
    section_header("Concept Narrative")

    raw_concept = result.get("concept", "")
    clean_concept = re.sub(r'<.*?>', '', raw_concept).strip()

    if not clean_concept:
        clean_concept = "A refined culinary experience crafted with artistic precision."

    st.markdown(f"""
    <div style="background:#0e1220;padding:18px;border-radius:6px;">
        <p style="color:#4a7fd4;text-transform:uppercase;
                  letter-spacing:0.2em;font-size:11px;">
            {result.get("tagline","")}
        </p>
        <p style="color:#b8c4e0;font-size:14px;">
            {clean_concept}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Signature Menu ──────────────────────────────────────
    section_header("Signature Menu")

    items = result.get("menu_items","").split(",")
    emojis = CUISINE_EMOJI.get(cuisine, ["🍽️"])

    cols = st.columns(3)

    for i, item in enumerate(items):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background:#0e1220;padding:12px;
                        text-align:center;border-radius:6px;">
                <div style="font-size:24px;">
                    {emojis[i % len(emojis)]}
                </div>
                <p style="color:#d4c8a8;font-size:13px;">
                    {item.strip()}
                </p>
                <p style="color:#4a7fd4;">
                    {PRICE_RANGE[i % len(PRICE_RANGE)]}
                </p>
            </div>
            """, unsafe_allow_html=True)

    # ── Chef's Selections ───────────────────────────────────
    section_header("Chef's Selections")

    recs = result.get("recommendation","").split("\n")

    for i, rec in enumerate(recs):
        name, desc = rec.split("-",1) if "-" in rec else (rec,"")

        st.markdown(f"""
        <div style="background:#0e1220;padding:15px;
                    margin-bottom:10px;border-radius:6px;">
            <strong style="color:#f0e6c8;">
                {REC_EMOJI[i % len(REC_EMOJI)]} {name.strip()}
            </strong>
            <p style="color:#8090b0;">
                {desc.strip()}
            </p>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:2rem;color:#6070a0;">
    <p><i>Where imagination meets fine dining</i></p>
</div>
""", unsafe_allow_html=True)
