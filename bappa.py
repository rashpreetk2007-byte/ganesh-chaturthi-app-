import streamlit as st
from PIL import Image
import os
import random

# =========================================================
# HAPPY GANESH CHATURTHI 2026
# Developed by Rashpreet Kaur Arora
# =========================================================

st.set_page_config(
    page_title="Happy Ganesh Chaturthi 2026",
    page_icon="🙏",
    layout="centered"
)

# =========================================================
# SESSION STATE
# =========================================================

if "blessing" not in st.session_state:
    st.session_state.blessing = 0

if "count" not in st.session_state:
    st.session_state.count = 0

if "animation" not in st.session_state:
    st.session_state.animation = True


# =========================================================
# THEME SETTINGS
# =========================================================

theme = st.selectbox(
    "🎨 Choose Theme",
    [
        "Royal Gold",
        "Divine Pink",
        "Temple Blue",
        "Festive Orange"
    ]
)

themes = {

    "Royal Gold": {
        "top": "#070914",
        "middle": "#18172c",
        "bottom": "#080a12",
        "gold": "#ffd45c",
        "accent": "#ffb52e"
    },

    "Divine Pink": {
        "top": "#170914",
        "middle": "#301426",
        "bottom": "#10070d",
        "gold": "#ffd0dc",
        "accent": "#ff8eae"
    },

    "Temple Blue": {
        "top": "#050b18",
        "middle": "#101f3d",
        "bottom": "#050914",
        "gold": "#b9dcff",
        "accent": "#66b7ff"
    },

    "Festive Orange": {
        "top": "#160b05",
        "middle": "#32170b",
        "bottom": "#0e0703",
        "gold": "#ffd08a",
        "accent": "#ff8c32"
    }
}

current = themes[theme]


# =========================================================
# ANIMATION CONTROL
# =========================================================

st.session_state.animation = st.toggle(
    "✨ Enable Animation",
    value=st.session_state.animation
)
# =========================================================
# CSS
# =========================================================

st.markdown(
    f"""
<style>

* {{
    box-sizing: border-box;
}}

.stApp {{

    min-height: 100vh;

    background:
        radial-gradient(
            circle at 50% 18%,
            rgba(255,190,60,0.24),
            transparent 28%
        ),

        linear-gradient(
            180deg,
            {current["top"]} 0%,
            {current["middle"]} 50%,
            {current["bottom"]} 100%
        );

    color: white;
}}


/* =====================================================
   PHONE WIDTH
   ===================================================== */

.block-container {{

    max-width: 520px !important;

    padding-top: 18px !important;

    padding-left: 13px !important;

    padding-right: 13px !important;

    padding-bottom: 30px !important;

    margin: auto;
}}


/* =====================================================
   TITLE
   ===================================================== */

.title {{

    text-align: center;

    color: {current["gold"]};

    font-size: clamp(29px, 8vw, 41px);

    font-weight: 900;

    line-height: 1.12;

    margin-bottom: 5px;

    text-shadow:
        0 0 10px rgba(255,200,70,0.35),
        0 0 25px rgba(255,160,30,0.20);
}}
/* =====================================================
   YEAR
   ===================================================== */

.year {{

    text-align: center;

    color: {current["accent"]};

    font-size: 40px;

    font-weight: 900;

    line-height: 1;

    margin-bottom: 12px;
}}


/* =====================================================
   BLESSING
   ===================================================== */

.blessing {{

    text-align: center;

    color: white;

    font-size: 17px;

    line-height: 1.45;

    padding: 0 10px;

    margin-bottom: 13px;
}}


/* =====================================================
   DECORATION
   ===================================================== */

.decor {{

    text-align: center;

    color: {current["gold"]};

    font-size: 20px;

    letter-spacing: 7px;

    margin-bottom: 12px;
}}


/* =====================================================
   IMAGE CARD
   ===================================================== */

.image-card {{

    width: 100%;

    max-width: 440px;

    margin: auto;

    padding: 8px;

    border-radius: 25px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.10),
            rgba(255,255,255,0.025)
        );

    border: 2px solid rgba(255,200,80,0.55);

    box-shadow:
        0 0 20px rgba(255,180,40,0.20),
        0 0 55px rgba(255,150,30,0.10);
}}


/* =====================================================
   IMAGE
   ===================================================== */

.image-card img {{

    width: 100% !important;

    max-height: 430px !important;

    object-fit: contain !important;

    border-radius: 18px !important;

    display: block;

    margin: auto;
}}


/* =====================================================
   DIYAS
   ===================================================== */

.diyas {{

    display: flex;

    justify-content: center;

    gap: 45px;

    margin-top: 12px;

    margin-bottom: 10px;
}}

.diya {{

    font-size: 27px;

    animation:
        diyaGlow 1.5s ease-in-out infinite alternate;
}}

@keyframes diyaGlow {{

    from {{
        transform: scale(0.90);
        filter: brightness(0.9);
    }}

    to {{
        transform: scale(1.18);
        filter: brightness(1.5);
    }}
}}


/* =====================================================
   MANTRA
   ===================================================== */

.mantra {{

    text-align: center;

    color: #ffe4a5;

    font-size: 18px;

    font-weight: 700;

    margin: 10px 0 16px 0;
}}


/* =====================================================
   SECTION CARD
   ===================================================== */

.section-card {{

    padding: 14px;

    margin-top: 12px;

    border-radius: 18px;

    background: rgba(255,255,255,0.045);

    border: 1px solid rgba(255,205,90,0.18);
}}


/* =====================================================
   FOOTER
   ===================================================== */

.morya {{

    text-align: center;

    color: {current["accent"]};

    font-size: 21px;

    font-weight: 900;

    margin-top: 20px;
}}

.credit {{

    text-align: center;

    color: #9a9ca8;

    font-size: 12px;

    margin-top: 12px;
}}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width:400px) {{

    .block-container {{

        padding-left: 10px !important;

        padding-right: 10px !important;
    }}

    .title {{
        font-size: 29px;
    }}

    .year {{
        font-size: 37px;
    }}

    .blessing {{
        font-size: 16px;
    }}

    .image-card {{
        padding: 7px;
    }}

    .image-card img {{
        max-height: 390px !important;
    }}

    .mantra {{
        font-size: 16px;
    }}

}}


/* =====================================================
   HIDE DEFAULT STREAMLIT UI
   ===================================================== */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

</style>
""",
    unsafe_allow_html=True
)
# =========================================================
# FLOATING PARTICLES
# =========================================================

if st.session_state.animation:

    st.markdown(
        """
        <div style="
            position:fixed;
            inset:0;
            pointer-events:none;
            overflow:hidden;
            z-index:0;
        ">

        <div style="
            position:absolute;
            left:8%;
            bottom:-20px;
            color:#ffd45c;
            font-size:16px;
            animation: float1 7s linear infinite;
        ">✦</div>

        <div style="
            position:absolute;
            left:25%;
            bottom:-20px;
            color:#ffd45c;
            font-size:13px;
            animation: float2 8s linear infinite;
        ">✧</div>

        <div style="
            position:absolute;
            left:45%;
            bottom:-20px;
            color:#ffd45c;
            font-size:17px;
            animation: float1 9s linear infinite;
        ">•</div>

        <div style="
            position:absolute;
            left:65%;
            bottom:-20px;
            color:#ffd45c;
            font-size:15px;
            animation: float2 7s linear infinite;
        ">✦</div>

        <div style="
            position:absolute;
            left:87%;
            bottom:-20px;
            color:#ffd45c;
            font-size:14px;
            animation: float1 8s linear infinite;
        ">✧</div>

        </div>

        <style>

        @keyframes float1 {

            0% {
                transform:translateY(0);
                opacity:0;
            }

            20% {
                opacity:0.8;
            }

            100% {
                transform:translateY(-105vh);
                opacity:0;
            }
        }

        @keyframes float2 {

            0% {
                transform:translateY(0) rotate(0deg);
                opacity:0;
            }

            20% {
                opacity:0.8;
            }

            100% {
                transform:translateY(-105vh) rotate(180deg);
                opacity:0;
            }
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# MAIN TITLE
# =========================================================

st.markdown(
    '<div class="title">Happy Ganesh Chaturthi</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="year">2026</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="blessing">'
    '🙏 May Bappa bless you with joy &amp; peace 🙏'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="decor">✦ ✦ ✦</div>',
    unsafe_allow_html=True
)
# =========================================================
# GANESH IMAGE
# =========================================================

image_path = "file_00000000a74482098265ae866f1a87d0.png"

if os.path.exists(image_path):

    try:

        img = Image.open(image_path)

        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")

        st.markdown(
            '<div class="image-card">',
            unsafe_allow_html=True
        )

        st.image(
            img,
            use_container_width=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error("Ganesh Ji image could not be opened.")

else:

    st.error("Ganesh Ji image not found.")

    st.info(
        "Make sure the PNG file is in the same GitHub folder as bappa.py."
    )


# =========================================================
# DIYAS
# =========================================================

st.markdown(
    """
    <div class="diyas">

        <div class="diya">🪔</div>

        <div class="diya">🪔</div>

        <div class="diya">🪔</div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MANTRA SELECTOR
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🕉️ Divine Mantra")

mantra = st.selectbox(
    "Choose a mantra",
    [
        "ॐ गं गणपतये नमः",
        "गणपति बप्पा मोरया",
        "ॐ श्री गणेशाय नमः",
        "वक्रतुण्ड महाकाय"
    ]
)

st.markdown(
    f'<div class="mantra">{mantra}</div>',
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# 108 MANTRA COUNTER
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🔢 108 Mantra Counter")

col1, col2 = st.columns(2)

with col1:

    if st.button("🙏 Chant +1", use_container_width=True):

        if st.session_state.count < 108:

            st.session_state.count += 1

        else:

            st.session_state.count = 108


with col2:

    if st.button("🔄 Reset", use_container_width=True):

        st.session_state.count = 0


st.progress(
    st.session_state.count / 108
)

st.markdown(
    f"""
    <div style="
        text-align:center;
        color:{current["gold"]};
        font-size:25px;
        font-weight:800;
        margin-top:8px;
    ">
        {st.session_state.count} / 108
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)
# =========================================================
# BLESSING MESSAGES
# =========================================================

blessings = [

    "🙏 May Lord Ganesha remove every obstacle and fill your life with happiness, peace and success. 🙏",

    "🌸 May Bappa bring wisdom, prosperity and positivity into your life. 🌸",

    "✨ May every new beginning be blessed by Lord Ganesha. ✨",

    "🪔 May your home be filled with peace, love and divine blessings. 🪔",

    "🙏 May Ganpati Bappa guide you towards success and happiness. 🙏"
]


st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🙏 Bappa's Blessings")

if st.button(
    "✨ Receive New Blessing",
    use_container_width=True
):

    st.session_state.blessing = random.randint(
        0,
        len(blessings) - 1
    )

st.success(
    blessings[st.session_state.blessing]
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FESTIVAL MESSAGE
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🎉 Festival Message")

message = st.selectbox(
    "Choose message",
    [
        "Happy Ganesh Chaturthi! 🙏",
        "Ganpati Bappa Morya! 🌺",
        "May Bappa bless your family! 🪔",
        "Wishing you peace and prosperity! ✨",
        "Celebrate with devotion and happiness! 🌸"
    ]
)

st.info(message)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="morya">'
    'Ganpati Bappa Morya 🙏'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="credit">'
    'Developed by Rashpreet Kaur Arora | BCA 2nd Year'
    '</div>',
    unsafe_allow_html=True
)
