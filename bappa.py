import streamlit as st
from PIL import Image
import os

# =========================================================
# HAPPY GANESH CHATURTHI 2026
# Developed by Rashpreet Kaur Arora
# =========================================================

st.set_page_config(
    page_title="Happy Ganesh Chaturthi 2026",
    page_icon="🙏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# BEAUTIFUL PHONE DESIGN
# =========================================================

st.markdown("""
<style>

* {
    box-sizing: border-box;
}

.stApp {
    min-height: 100vh;

    background:
        radial-gradient(
            circle at 50% 18%,
            rgba(255, 190, 55, 0.25),
            transparent 28%
        ),
        radial-gradient(
            circle at 10% 75%,
            rgba(255, 100, 150, 0.12),
            transparent 25%
        ),
        linear-gradient(
            180deg,
            #070914 0%,
            #17182d 48%,
            #080a12 100%
        );

    color: white;
}

.block-container {
    max-width: 520px !important;

    padding-top: 18px !important;
    padding-left: 14px !important;
    padding-right: 14px !important;
    padding-bottom: 30px !important;

    margin: auto;
}

/* =========================================================
   FLOATING GOLDEN PARTICLES
   ========================================================= */

.particles {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;

    pointer-events: none;

    overflow: hidden;

    z-index: 0;
}

.particle {
    position: absolute;

    color: #ffd45c;

    font-size: 15px;

    animation: floatUp 8s linear infinite;

    opacity: 0;
}

.p1 {
    left: 8%;
    bottom: -20px;
    animation-delay: 0s;
}

.p2 {
    left: 23%;
    bottom: -20px;
    animation-delay: 1.5s;
}

.p3 {
    left: 39%;
    bottom: -20px;
    animation-delay: 3s;
}

.p4 {
    left: 55%;
    bottom: -20px;
    animation-delay: 2s;
}

.p5 {
    left: 72%;
    bottom: -20px;
    animation-delay: 4s;
}

.p6 {
    left: 89%;
    bottom: -20px;
    animation-delay: 5s;
}

@keyframes floatUp {

    0% {
        transform: translateY(0) scale(0.6);
        opacity: 0;
    }

    20% {
        opacity: 0.8;
    }

    80% {
        opacity: 0.7;
    }

    100% {
        transform: translateY(-105vh) scale(1.3);
        opacity: 0;
    }
}

/* =========================================================
   TITLE
   ========================================================= */

.title {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffd45c;

    font-size: clamp(28px, 8vw, 40px);

    font-weight: 800;

    line-height: 1.15;

    margin-top: 5px;
    margin-bottom: 6px;

    text-shadow:
        0 0 10px rgba(255, 195, 60, 0.35),
        0 0 25px rgba(255, 160, 30, 0.18);
}

/* =========================================================
   YEAR
   ========================================================= */

.year {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffb52e;

    font-size: 40px;

    font-weight: 800;

    line-height: 1;

    margin-bottom: 12px;
}

/* =========================================================
   BLESSING
   ========================================================= */

.blessing {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffffff;

    font-size: 17px;

    line-height: 1.45;

    padding: 0 12px;

    margin-bottom: 14px;
}

/* =========================================================
   DECORATION
   ========================================================= */

.decor {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffd05a;

    font-size: 18px;

    letter-spacing: 7px;

    margin-bottom: 12px;
}

/* =========================================================
   IMAGE CARD
   ========================================================= */

.image-card {
    position: relative;
    z-index: 2;

    width: 100%;

    max-width: 440px;

    margin: 0 auto;

    padding: 8px;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.09),
            rgba(255,255,255,0.025)
        );

    border: 2px solid rgba(255, 195, 60, 0.55);

    box-shadow:
        0 0 20px rgba(255, 180, 40, 0.18),
        0 0 55px rgba(255, 150, 30, 0.08);
}

/* =========================================================
   STREAMLIT IMAGE CONTAINER
   ========================================================= */

.image-card [data-testid="stImage"] {
    width: 100%;
    display: flex;
    justify-content: center;
}

.image-card [data-testid="stImage"] img {
    width: 100% !important;

    max-height: 430px !important;

    object-fit: contain !important;

    border-radius: 17px !important;

    display: block;

    margin: auto;
}

/* =========================================================
   DIYAS
   ========================================================= */

.diyas {
    position: relative;
    z-index: 2;

    display: flex;

    justify-content: center;

    gap: 42px;

    margin-top: 13px;

    margin-bottom: 8px;
}

.diya {
    font-size: 25px;

    animation: diyaGlow 1.7s ease-in-out infinite alternate;
}

.diya:nth-child(2) {
    animation-delay: 0.7s;
}

@keyframes diyaGlow {

    from {
        transform: scale(0.92);
        filter: brightness(0.9);
    }

    to {
        transform: scale(1.15);
        filter: brightness(1.4);
    }
}

/* =========================================================
   MANTRA
   ========================================================= */

.mantra {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffe4a5;

    font-size: 17px;

    font-weight: 600;

    line-height: 1.5;

    margin-top: 8px;
}

/* =========================================================
   BUTTON TITLE
   ========================================================= */

.button-title {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffffff;

    font-size: 17px;

    font-weight: 700;

    margin-top: 17px;

    margin-bottom: 8px;
}

/* =========================================================
   BUTTON
   ========================================================= */

.stButton > button {

    width: 100%;

    min-height: 48px;

    border-radius: 14px;

    border: 1px solid rgba(255, 205, 90, 0.55);

    background:
        linear-gradient(
            135deg,
            #8f531b,
            #d89125
        );

    color: white;

    font-size: 16px;

    font-weight: 700;

    box-shadow:
        0 5px 18px rgba(0,0,0,0.28);
}

.stButton > button:hover {

    border-color: #ffd45c;

    color: white;
}

/* =========================================================
   FOOTER
   ========================================================= */

.morya {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffb43b;

    font-size: 20px;

    font-weight: 800;

    margin-top: 18px;
}

.credit {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #858895;

    font-size: 12px;

    margin-top: 13px;
}

/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 400px) {

    .block-container {
        padding-left: 10px !important;
        padding-right: 10px !important;
    }

    .title {
        font-size: 29px;
    }

    .year {
        font-size: 37px;
    }

    .blessing {
        font-size: 16px;
    }

    .image-card {
        padding: 7px;
        border-radius: 20px;
    }

    .image-card [data-testid="stImage"] img {
        max-height: 390px !important;
    }

    .mantra {
        font-size: 15px;
    }

    .morya {
        font-size: 18px;
    }
}

/* Hide Streamlit default elements */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FLOATING PARTICLES
# =========================================================

st.markdown("""
<div class="particles">

<span class="particle p1">✦</span>
<span class="particle p2">✧</span>
<span class="particle p3">•</span>
<span class="particle p4">✦</span>
<span class="particle p5">✧</span>
<span class="particle p6">•</span>

</div>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
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
# GANESH JI IMAGE
# =========================================================

# IMPORTANT:
# This is your CURRENT GitHub filename.

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

    except Exception:

        st.error(
            "Ganesh Ji image could not be opened."
        )

else:

    st.error(
        "Ganesh Ji image not found."
    )

    st.info(
        "Make sure the PNG file is in the same GitHub folder as bappa.py."
    )


# =========================================================
# DIYAS
# =========================================================

st.markdown("""
<div class="diyas">

<div class="diya">🪔</div>

<div class="diya">🪔</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# MANTRA
# =========================================================

st.markdown(
    '<div class="mantra">'
    'ॐ गं गणपतये नमः'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# BLESSING BUTTON
# =========================================================

st.markdown(
    '<div class="button-title">'
    '🙏 Send Bappa\'s Blessings'
    '</div>',
    unsafe_allow_html=True
)

if st.button("✨ Receive Blessing"):

    st.success(
        "🙏 May Lord Ganesha remove every obstacle "
        "and fill your life with happiness, peace and success. 🙏"
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
