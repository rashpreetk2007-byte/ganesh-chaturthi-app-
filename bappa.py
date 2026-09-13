import streamlit as st
from PIL import Image
import os
import base64

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
# BACKGROUND + DESIGN
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
            circle at 50% 20%,
            rgba(255, 190, 60, 0.22),
            transparent 25%
        ),
        radial-gradient(
            circle at 20% 70%,
            rgba(180, 70, 120, 0.12),
            transparent 25%
        ),
        linear-gradient(
            180deg,
            #070914 0%,
            #15172b 48%,
            #080a12 100%
        );

    color: white;
}

/* PHONE CONTAINER */

.block-container {
    width: 100%;
    max-width: 520px !important;

    padding-top: 18px !important;
    padding-left: 14px !important;
    padding-right: 14px !important;
    padding-bottom: 30px !important;

    margin: auto;
}

/* =======================================================
   FLOATING PARTICLES
   ======================================================= */

.particles {
    position: fixed;
    inset: 0;

    pointer-events: none;
    overflow: hidden;

    z-index: 0;
}

.particle {
    position: absolute;

    color: #ffd45c;
    font-size: 14px;

    opacity: 0.75;

    animation: floatUp 7s linear infinite;
}

.p1 { left: 8%;  bottom: -20px; animation-delay: 0s; }
.p2 { left: 22%; bottom: -20px; animation-delay: 1.2s; }
.p3 { left: 38%; bottom: -20px; animation-delay: 2.4s; }
.p4 { left: 55%; bottom: -20px; animation-delay: 3.2s; }
.p5 { left: 72%; bottom: -20px; animation-delay: 1.7s; }
.p6 { left: 88%; bottom: -20px; animation-delay: 4s; }

@keyframes floatUp {

    0% {
        transform: translateY(0) scale(0.7);
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

/* =======================================================
   TITLE
   ======================================================= */

.title {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffd35a;

    font-size: clamp(28px, 8vw, 42px);

    font-weight: 800;

    line-height: 1.12;

    margin-top: 5px;
    margin-bottom: 6px;

    text-shadow:
        0 0 8px rgba(255, 200, 70, 0.30),
        0 0 22px rgba(255, 160, 30, 0.15);
}

/* =======================================================
   YEAR
   ======================================================= */

.year {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffb52e;

    font-size: 42px;

    font-weight: 800;

    line-height: 1;

    margin-bottom: 13px;
}

/* =======================================================
   BLESSING
   ======================================================= */

.blessing {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffffff;

    font-size: 18px;

    line-height: 1.4;

    margin: 0 auto 18px auto;

    padding: 0 10px;
}

/* =======================================================
   DECORATION
   ======================================================= */

.decor {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffca4d;

    font-size: 20px;

    letter-spacing: 8px;

    margin-bottom: 10px;
}

/* =======================================================
   GANESH IMAGE CARD
   ======================================================= */

.image-card {
    position: relative;
    z-index: 2;

    width: 100%;

    max-width: 460px;

    margin: auto;

    padding: 9px;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.08),
            rgba(255,255,255,0.025)
        );

    border: 2px solid rgba(255, 196, 65, 0.55);

    box-shadow:
        0 0 18px rgba(255, 180, 40, 0.16),
        0 0 45px rgba(255, 150, 30, 0.08);

    overflow: hidden;
}

/* =======================================================
   IMAGE
   ======================================================= */

.ganesh-image {
    display: block;

    width: 100%;

    max-height: 430px;

    object-fit: contain;

    border-radius: 17px;

    margin: auto;
}

/* =======================================================
   DIYA EFFECT
   ======================================================= */

.diyas {
    position: relative;

    z-index: 2;

    display: flex;

    justify-content: center;

    gap: 35px;

    margin-top: 12px;

    margin-bottom: 10px;
}

.diya {
    font-size: 24px;

    animation: diyaGlow 1.8s ease-in-out infinite alternate;
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
        transform: scale(1.12);
        filter: brightness(1.4);
    }
}

/* =======================================================
   MANTRA
   ======================================================= */

.mantra {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffe2a0;

    font-size: 16px;

    font-weight: 600;

    line-height: 1.5;

    margin-top: 8px;

    padding: 0 10px;
}

/* =======================================================
   BUTTON AREA
   ======================================================= */

.button-title {
    position: relative;
    z-index: 2;

    text-align: center;

    color: #ffffff;

    font-size: 17px;

    font-weight: 700;

    margin-top: 18px;

    margin-bottom: 8px;
}

/* Streamlit buttons */

.stButton > button {

    width: 100%;

    min-height: 48px;

    border-radius: 14px;

    border: 1px solid rgba(255, 200, 80, 0.5);

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
        0 4px 15px rgba(0,0,0,0.25);
}

.stButton > button:hover {

    border-color: #ffd15a;

    color: white;

    transform: translateY(-1px);
}

/* =======================================================
   FOOTER
   ======================================================= */

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

    margin-top: 14px;
}

/* =======================================================
   MOBILE
   ======================================================= */

@media (max-width: 400px) {

    .block-container {
        padding-left: 11px !important;
        padding-right: 11px !important;
    }

    .title {
        font-size: 29px;
    }

    .year {
        font-size: 38px;
    }

    .blessing {
        font-size: 17px;
    }

    .image-card {
        padding: 7px;
        border-radius: 20px;
    }

    .ganesh-image {
        max-height: 390px;
    }

    .mantra {
        font-size: 15px;
    }

    .morya {
        font-size: 18px;
    }

}

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
# IMAGE
# =========================================================

image_path = "GaneshJi.png"

if os.path.exists(image_path):

    try:

        img = Image.open(image_path)

        # Convert unusual image modes safely
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

    except Exception as error:

        st.error(
            "GaneshJi.png could not be opened."
        )

else:

    st.error(
        "GaneshJi.png not found."
    )

    st.info(
        "Put GaneshJi.png in the same GitHub folder as bappa.py."
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
# INTERACTIVE BUTTON
# =========================================================

st.markdown(
    '<div class="button-title">🙏 Send Bappa\'s Blessings</div>',
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
    '<div class="morya">Ganpati Bappa Morya 🙏</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="credit">'
    'Developed by Rashpreet Kaur Arora | BCA 2nd Year'
    '</div>',
    unsafe_allow_html=True
)
