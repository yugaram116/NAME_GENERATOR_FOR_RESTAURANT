import streamlit as st

st.set_page_config(
    page_title="Flavor Hub",
    page_icon="🍽️",
    layout="centered"
)

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
    font-family: 'Josefin Sans', sans-serif !important;
}

.stSelectbox > div > div {
    background-color: #0e1220;
    border: 1px solid #2c4a8a;
    color: #f0e6c8;
    border-radius: 4px;
    font-family: 'Josefin Sans', sans-serif;
}

.stButton > button {
    width: 100%;
    background-color: #1a3368;
    color: #f0e6c8;
    border: 1px solid #2c4a8a;
    border-radius: 4px;
    font-family: 'Josefin Sans', sans-serif;
    font-size: 12px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    padding: 12px 28px;
    transition: all 0.2s;
}

.stButton > button:hover {
    background-color: #234280;
    border-color: #4a7fd4;
    color: #f0e6c8;
}

.stSpinner > div {
    border-top-color: #4a7fd4 !important;
}

hr {
    border-color: #1a2340;
}
</style>
""", unsafe_allow_html=True)


# ── Cuisine emoji map ─────────────────────────────────────────────────────────

CUISINE_EMOJI = {
    "Indian":   ["🍛", "🫓", "🍢", "🥘", "🫕", "🍲"],
    "Italian":  ["🍝", "🍕", "🥗", "🍷", "🧀", "🥩"],
    "Mexican":  ["🌮", "🌯", "🥑", "🫔", "🌶️", "🍹"],
    "Japanese": ["🍣", "🍜", "🍱", "🍤", "🥟", "🍶"],
    "French":   ["🥐", "🧅", "🍷", "🥩", "🧁", "🫕"],
    "Greek":    ["🫒", "🥗", "🧆", "🍋", "🐟", "🫙"],
    "Chinese":  ["🥟", "🍜", "🦆", "🍚", "🥡", "🍵"],
}

PRICE_RANGE = ["₹320", "₹450", "₹395", "₹520", "₹480", "₹290"]

REC_EMOJI = ["🌟", "👨‍🍳", "🏆"]


# ── Helpers ───────────────────────────────────────────────────────────────────

def rule_divider(width=60):
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:12px;
                justify-content:center;margin:8px 0 16px;">
        <div style="width:{width}px;height:1px;background:#2c4a8a;"></div>
        <div style="width:6px;height:6px;background:#4a7fd4;
                    transform:rotate(45deg);"></div>
        <div style="width:{width}px;height:1px;background:#2c4a8a;"></div>
    </div>
    """, unsafe_allow_html=True)


def section_header(label):
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:14px;padding:1.5rem 0 1rem;">
        <span style="font-size:10px;letter-spacing:0.25em;text-transform:uppercase;
                     color:#4a7fd4;white-space:nowrap;
                     font-family:'Josefin Sans',sans-serif;">
            {label}
        </span>
        <div style="flex:1;height:1px;background:#1a2340;"></div>
    </div>
    """, unsafe_allow_html=True)


# ── Hero Header ───────────────────────────────────────────────────────────────

st.markdown("""
<div style="text-align:center;padding:2.5rem 2rem 2rem;
            border-bottom:1px solid #1a2340;margin-bottom:1.5rem;">
""", unsafe_allow_html=True)

rule_divider(60)

st.markdown("""
    <div style="display:flex;align-items:baseline;justify-content:center;margin-bottom:4px;">
        <span style="font-family:'Cormorant Garamond',serif;font-size:40px;
                     font-weight:300;letter-spacing:0.1em;color:#f0e6c8;
                     text-transform:uppercase;">
            Flavor<span style="color:#4a7fd4;">Hub</span>
        </span>
    </div>
    <p style="font-size:10px;letter-spacing:0.28em;color:#4a5a7a;
              text-transform:uppercase;margin:8px 0 0;
              font-family:'Josefin Sans',sans-serif;font-weight:300;">
        Haute cuisine concept atelier
    </p>
</div>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────

st.sidebar.markdown("""
<p style="font-size:10px;letter-spacing:0.22em;text-transform:uppercase;
          color:#4a7fd4;font-family:'Josefin Sans',sans-serif;margin-bottom:6px;">
    Select cuisine
</p>
""", unsafe_allow_html=True)

cuisine = st.sidebar.selectbox(
    label="",
    options=["Indian", "Italian", "Mexican", "Japanese", "French", "Greek", "Chinese"],
    label_visibility="collapsed"
)

st.sidebar.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
generate = st.sidebar.button("Compose Concept")


# ── Generation ────────────────────────────────────────────────────────────────

if generate:
    from langchain_helper import generate_restaurant_name_and_items

    with st.spinner("Curating your concept..."):
        result = generate_restaurant_name_and_items(cuisine)

    # ── Restaurant Name ───────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="padding:2rem 0 1.75rem;border-bottom:1px solid #1a2340;text-align:center;">
        <p style="font-size:10px;letter-spacing:0.25em;text-transform:uppercase;
                  color:#4a7fd4;margin-bottom:10px;
                  font-family:'Josefin Sans',sans-serif;">
            Establishment name
        </p>
        <p style="font-family:'Cormorant Garamond',serif;font-size:30px;
                  font-weight:400;color:#f0e6c8;letter-spacing:0.06em;margin:0;">
            {result['restaurant_name']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Signature Menu ────────────────────────────────────────────────────────
    section_header("Signature Menu")

    menu_items = [item.strip() for item in result["menu_items"].split(",")]
    emojis     = CUISINE_EMOJI.get(cuisine, ["🍽️"] * 6)
    prices     = PRICE_RANGE

    cols = st.columns(3)
    for i, item in enumerate(menu_items):
        emoji = emojis[i] if i < len(emojis) else "🍽️"
        price = prices[i] if i < len(prices) else "₹399"
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background:#0e1220;border:1px solid #1e2a4a;
                        border-top:2px solid #2c4a8a;
                        border-radius:0 0 4px 4px;
                        padding:14px 16px;margin-bottom:10px;
                        font-family:'Josefin Sans',sans-serif;
                        text-align:center;">
                <div style="font-size:26px;margin-bottom:8px;line-height:1;">
                    {emoji}
                </div>
                <div style="font-size:12px;color:#d4c8a8;letter-spacing:0.06em;
                            font-weight:300;margin-bottom:8px;line-height:1.4;">
                    {item}
                </div>
                <div style="display:inline-block;background:#0a1428;
                            border:1px solid #2c4a8a;border-radius:20px;
                            padding:3px 12px;">
                    <span style="font-size:11px;color:#4a7fd4;
                                 letter-spacing:0.1em;font-weight:400;">
                        {price}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── Chef's Selections ─────────────────────────────────────────────────────
    section_header("Chef's Selections")

    rec_lines = [r for r in result["recommendation"].strip().split("\n") if r.strip()]
    for idx, rec in enumerate(rec_lines):
        dish_name, description = rec.split("-", 1) if "-" in rec else (rec, "")
        rec_emoji = REC_EMOJI[idx] if idx < len(REC_EMOJI) else "✨"
        st.markdown(f"""
        <div style="background:#0e1220;border:1px solid #1e2a4a;
                    border-radius:4px;padding:16px 18px;
                    display:flex;gap:16px;align-items:flex-start;
                    margin-bottom:10px;">
            <div style="text-align:center;min-width:36px;">
                <div style="font-size:22px;line-height:1;margin-bottom:4px;">
                    {rec_emoji}
                </div>
                <div style="font-family:'Cormorant Garamond',serif;font-size:18px;
                            font-weight:300;color:#1e3060;line-height:1;">
                    0{idx + 1}
                </div>
            </div>
            <div style="flex:1;">
                <div style="display:flex;align-items:center;
                            justify-content:space-between;margin-bottom:6px;
                            flex-wrap:wrap;gap:8px;">
                    <p style="font-size:12px;font-weight:500;color:#f0e6c8;
                              letter-spacing:0.12em;text-transform:uppercase;
                              margin:0;font-family:'Josefin Sans',sans-serif;">
                        {dish_name.strip()}
                    </p>
                    <span style="background:#0a1428;border:1px solid #2c4a8a;
                                 border-radius:20px;padding:3px 12px;
                                 font-size:11px;color:#4a7fd4;
                                 letter-spacing:0.1em;white-space:nowrap;">
                        ₹{480 + idx * 65}
                    </span>
                </div>
                <p style="font-size:12px;color:#8090b0;letter-spacing:0.04em;
                          margin:0;line-height:1.65;font-weight:300;
                          font-family:'Josefin Sans',sans-serif;">
                    {description.strip()}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────

st.markdown("""
<div style="text-align:center;padding:2rem 0 0;
            border-top:1px solid #1a2340;margin-top:2rem;">
""", unsafe_allow_html=True)

rule_divider(40)

st.markdown("""
    <p style="font-family:'Cormorant Garamond',serif;font-size:16px;
              font-weight:300;color:#6070a0;letter-spacing:0.06em;
              font-style:italic;margin:0 0 14px;line-height:1.7;">
        Where <span style="color:#8898c8;font-style:normal;">imagination</span>
        meets the art of fine dining &mdash;<br>
        every concept a masterpiece, every menu a story.
    </p>
""", unsafe_allow_html=True)

rule_divider(24)

st.markdown("""
    <p style="font-size:10px;letter-spacing:0.22em;color:#3a4a6a;
              text-transform:uppercase;font-family:'Josefin Sans',sans-serif;
              margin:10px 0 0;">
        Conceived with passion by
        <span style="color:#4a7fd4;">Yugaram</span>
        &nbsp;&middot;&nbsp;
        Flavor<span style="color:#4a7fd4;">Hub</span>
    </p>
    <p style="font-size:10px;letter-spacing:0.18em;color:#2c3a5a;
              text-transform:uppercase;font-family:'Josefin Sans',sans-serif;
              margin:6px 0 0;">
        Crafting culinary dreams, one concept at a time
    </p>
</div>
""", unsafe_allow_html=True)