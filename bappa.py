import streamlit as st
from PIL import Image
import os
import random
import html

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
# SESSION STATE
# =========================================================

if "blessing" not in st.session_state:
    st.session_state.blessing = 0

if "count" not in st.session_state:
    st.session_state.count = 0

if "flower_animation" not in st.session_state:
    st.session_state.flower_animation = True

if "selected_message" not in st.session_state:
    st.session_state.selected_message = 0


# =========================================================
# IMAGE FILE
# =========================================================

IMAGE_FILE = "file_00000000a74482098265ae866f1a87d0.png"


# =========================================================
# BLESSINGS
# =========================================================

blessings = [
    "🙏 May Lord Ganesha remove every obstacle and fill your life with happiness, peace and success. 🙏",
    "🌸 May Bappa bring wisdom, prosperity and positivity into your life. 🌸",
    "✨ May every new beginning be blessed by Lord Ganesha. ✨",
    "🪔 May your home be filled with peace, love and divine blessings. 🪔",
    "🙏 May Ganpati Bappa guide you towards success and happiness. 🙏",
    "🌺 May Bappa bless you and your family with good health, peace and prosperity. 🌺"
]


# =========================================================
# MANTRAS
# =========================================================

mantras = [
    "ॐ गं गणपतये नमः",
    "ॐ श्री गणेशाय नमः",
    "गणपति बप्पा मोरया",
    "वक्रतुण्ड महाकाय"
]


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
<style>

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

/* ======================================================
   MAIN BACKGROUND
   ====================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 50% 8%,
            rgba(255, 193, 92, 0.40),
            transparent 24%
        ),
        radial-gradient(
            circle at 10% 45%,
            rgba(255, 166, 193, 0.28),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 70%,
            rgba(255, 190, 110, 0.25),
            transparent 28%
        ),
        linear-gradient(
            180deg,
            #fff8ec 0%,
            #fff1dc 45%,
            #ffe4c1 100%
        );

    color: #60351f;
    min-height: 100vh;
}


/* ======================================================
   PHONE WIDTH
   ====================================================== */

.block-container {
    max-width: 560px !important;

    padding-top: 18px !important;
    padding-left: 14px !important;
    padding-right: 14px !important;
    padding-bottom: 35px !important;

    margin: auto;
}


/* ======================================================
   TOP DECORATION
   ====================================================== */

.top-decoration {
    text-align: center;

    font-size: 22px;

    letter-spacing: 10px;

    color: #e8a51c;

    margin-bottom: 5px;
}


/* ======================================================
   MAIN TITLE
   ====================================================== */

.main-title {
    text-align: center;

    color: #a94d18;

    font-size: clamp(29px, 8vw, 43px);

    font-weight: 900;

    line-height: 1.12;

    margin-top: 4px;
    margin-bottom: 5px;

    text-shadow:
        0 2px 0 #fff,
        0 4px 12px rgba(173, 85, 20, 0.18);
}


/* ======================================================
   YEAR
   ====================================================== */

.year {
    text-align: center;

    color: #e39a0b;

    font-size: 44px;

    font-weight: 900;

    margin-bottom: 8px;

    text-shadow:
        0 2px 5px rgba(180, 100, 0, 0.18);
}


/* ======================================================
   SUBTITLE
   ====================================================== */

.subtitle {
    text-align: center;

    color: #70442e;

    font-size: 17px;

    font-weight: 700;

    line-height: 1.5;

    margin: 0 auto 10px auto;

    padding: 0 8px;
}


/* ======================================================
   SMALL DECORATION
   ====================================================== */

.divider {
    text-align: center;

    color: #e5a51d;

    font-size: 21px;

    letter-spacing: 9px;

    margin: 8px 0 13px 0;
}


/* ======================================================
   IMAGE FRAME
   ====================================================== */

.image-frame {
    width: 100%;

    padding: 7px;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            #fffdf8,
            #ffe5b8,
            #fff8ec
        );

    border: 3px solid #e4a625;

    box-shadow:
        0 8px 25px rgba(166, 91, 15, 0.20),
        0 0 35px rgba(255, 181, 55, 0.16);

    margin: 0 auto 13px auto;
}


/* ======================================================
   IMAGE
   ====================================================== */

.image-frame img {
    width: 100% !important;

    max-height: 620px !important;

    object-fit: contain !important;

    border-radius: 18px !important;

    display: block;

    margin: auto;
}


/* ======================================================
   DIYAS
   ====================================================== */

.diya-row {
    display: flex;

    justify-content: center;

    align-items: center;

    gap: 32px;

    margin: 8px 0 13px 0;
}

.diya {
    font-size: 28px;

    animation: diyaGlow 1.5s ease-in-out infinite alternate;
}

.diya:nth-child(2) {
    animation-delay: 0.4s;
}

.diya:nth-child(3) {
    animation-delay: 0.8s;
}

@keyframes diyaGlow {

    from {
        transform: scale(0.90);
        filter: brightness(0.95);
    }

    to {
        transform: scale(1.16);
        filter: brightness(1.35);
    }
}


/* ======================================================
   CARD
   ====================================================== */

.card {
    background: rgba(255, 255, 255, 0.78);

    border: 1px solid rgba(218, 157, 53, 0.30);

    border-radius: 22px;

    padding: 18px;

    margin-top: 14px;

    box-shadow:
        0 7px 22px rgba(144, 82, 24, 0.10);

    backdrop-filter: blur(6px);
}


/* ======================================================
   CARD TITLE
   ====================================================== */

.card-title {
    color: #71391f;

    font-size: 23px;

    font-weight: 900;

    margin-bottom: 12px;
}


/* ======================================================
   MANTRA DISPLAY
   ====================================================== */

.mantra-display {
    text-align: center;

    color: #b75b18;

    font-size: 20px;

    font-weight: 800;

    background:
        linear-gradient(
            90deg,
            #fff4dc,
            #ffe9c1,
            #fff4dc
        );

    border-radius: 14px;

    padding: 13px 8px;

    margin-top: 12px;

    border: 1px solid #edc56d;
}


/* ======================================================
   GREETING
   ====================================================== */

.greeting-box {
    background:
        linear-gradient(
            135deg,
            #fffaf2,
            #fff0d7
        );

    border-radius: 17px;

    padding: 18px;

    border: 1px solid #edca83;

    color: #633b27;

    font-size: 16px;

    line-height: 1.65;

    text-align: center;
}

.greeting-main {
    font-size: 19px;

    font-weight: 800;

    color: #b55418;

    margin-bottom: 10px;
}

.greeting-morya {
    color: #d1840c;

    font-size: 18px;

    font-weight: 900;

    margin-top: 10px;
}


/* ======================================================
   BUTTONS
   ====================================================== */

.stButton > button {
    width: 100%;

    min-height: 48px;

    border-radius: 15px;

    border: 1px solid #d99216;

    background:
        linear-gradient(
            135deg,
            #e48b16,
            #f4b52d
        );

    color: white;

    font-size: 16px;

    font-weight: 800;

    box-shadow:
        0 5px 14px rgba(180, 100, 15, 0.18);

    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    border-color: #c67509;

    color: white;

    box-shadow:
        0 8px 18px rgba(180, 100, 15, 0.25);
}


/* ======================================================
   PROGRESS BAR
   ====================================================== */

.stProgress > div > div > div {
    background-color: #e9a51e;
}


/* ======================================================
   SELECT BOX
   ====================================================== */

.stSelectbox label {
    color: #70442e !important;

    font-weight: 700 !important;
}

.stSelectbox > div > div {
    border-radius: 13px !important;
}


/* ======================================================
   COUNTER
   ====================================================== */

.counter-number {
    text-align: center;

    color: #c66d12;

    font-size: 31px;

    font-weight: 900;

    margin: 12px 0 4px 0;
}


/* ======================================================
   BLESSING MESSAGE
   ====================================================== */

.blessing-box {
    background:
        linear-gradient(
            135deg,
            #e8f7ec,
            #d9f1e3
        );

    border-radius: 16px;

    padding: 16px;

    color: #26724c;

    font-size: 16px;

    font-weight: 700;

    line-height: 1.55;

    text-align: center;

    border: 1px solid #b9dfc8;
}


/* ======================================================
   FESTIVAL MESSAGE
   ====================================================== */

.message-box {
    background:
        linear-gradient(
            135deg,
            #fff5df,
            #ffe8bb
        );

    border-radius: 16px;

    padding: 16px;

    text-align: center;

    color: #8b4b20;

    font-size: 17px;

    font-weight: 700;

    line-height: 1.5;

    border: 1px solid #eac477;
}


/* ======================================================
   ANIMATION
   ====================================================== */

.falling {
    position: fixed;

    inset: 0;

    pointer-events: none;

    overflow: hidden;

    z-index: 1;
}

.fall {
    position: absolute;

    top: -50px;

    font-size: 21px;

    opacity: 0.80;

    animation: fallDown linear infinite;
}

.f1 {
    left: 5%;
    animation-duration: 8s;
    animation-delay: 0s;
}

.f2 {
    left: 18%;
    animation-duration: 10s;
    animation-delay: 1s;
}

.f3 {
    left: 31%;
    animation-duration: 7s;
    animation-delay: 2s;
}

.f4 {
    left: 45%;
    animation-duration: 9s;
    animation-delay: 0.5s;
}

.f5 {
    left: 59%;
    animation-duration: 11s;
    animation-delay: 3s;
}

.f6 {
    left: 73%;
    animation-duration: 8s;
    animation-delay: 1.5s;
}

.f7 {
    left: 87%;
    animation-duration: 10s;
    animation-delay: 2.5s;
}

@keyframes fallDown {

    0% {
        transform:
            translateY(-60px)
            rotate(0deg);

        opacity: 0;
    }

    15% {
        opacity: 0.85;
    }

    50% {
        transform:
            translateY(50vh)
            translateX(18px)
            rotate(160deg);
    }

    100% {
        transform:
            translateY(115vh)
            translateX(-20px)
            rotate(320deg);

        opacity: 0;
    }
}


/* ======================================================
   FOOTER
   ====================================================== */

.morya {
    text-align: center;

    color: #b85717;

    font-size: 25px;

    font-weight: 900;

    margin-top: 25px;

    margin-bottom: 8px;
}

.credit {
    text-align: center;

    color: #8b7567;

    font-size: 12px;

    margin-bottom: 5px;
}


/* ======================================================
   MOBILE
   ====================================================== */

@media (max-width: 400px) {

    .block-container {
        padding-left: 10px !important;
        padding-right: 10px !important;
    }

    .main-title {
        font-size: 28px;
    }

    .year {
        font-size: 38px;
    }

    .subtitle {
        font-size: 15px;
    }

    .image-frame {
        padding: 5px;
        border-radius: 20px;
    }

    .image-frame img {
        max-height: 520px !important;
        border-radius: 15px !important;
    }

    .card {
        padding: 14px;
        border-radius: 18px;
    }

    .card-title {
        font-size: 21px;
    }

    .greeting-box {
        font-size: 15px;
        padding: 14px;
    }

    .morya {
        font-size: 22px;
    }
}


/* ======================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
   ====================================================== */

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
""",
    unsafe_allow_html=True
)


# =========================================================
# FALLING FLOWERS
# =========================================================

if st.session_state.flower_animation:

    st.markdown(
        """
        <div class="falling">

            <div class="fall f1">🌸</div>
            <div class="fall f2">🌺</div>
            <div class="fall f3">🌼</div>
            <div class="fall f4">✦</div>
            <div class="fall f5">🌸</div>
            <div class="fall f6">🌺</div>
            <div class="fall f7">✦</div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# ANIMATION SWITCH
# =========================================================

st.session_state.flower_animation = st.toggle(
    "🌸 Falling Flowers & Sparkles",
    value=st.session_state.flower_animation
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="top-decoration">✦ 🌸 ✦ 🌼 ✦</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">🙏 Happy Ganesh Chaturthi</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="year">2026</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        🌸 May Bappa bless you with joy, peace & prosperity 🌸
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="divider">✦ ✦ ✦</div>',
    unsafe_allow_html=True
)


# =========================================================
# GANESH IMAGE
# =========================================================

if os.path.exists(IMAGE_FILE):

    try:

        img = Image.open(IMAGE_FILE)

        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")

        st.markdown(
            '<div class="image-frame">',
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

        st.error("Ganesh Ji image could not be opened.")

else:

    st.error("Ganesh Ji image not found.")

    st.info(
        "Keep the PNG file in the same GitHub folder as bappa.py."
    )


# =========================================================
# DIYAS
# =========================================================

st.markdown(
    """
    <div class="diya-row">

        <div class="diya">🪔</div>
        <div class="diya">🪔</div>
        <div class="diya">🪔</div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MANTRA CARD
# =========================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">🕉️ Divine Mantra</div>',
    unsafe_allow_html=True
)

selected_mantra = st.selectbox(
    "Choose a mantra",
    mantras,
    label_visibility="visible"
)

st.markdown(
    f"""
    <div class="mantra-display">
        {html.escape(selected_mantra)}
    </div>
    """,
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
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">🔢 108 Mantra Counter</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🙏 Chant +1",
        use_container_width=True
    ):

        if st.session_state.count < 108:
            st.session_state.count += 1


with col2:

    if st.button(
        "🔄 Reset",
        use_container_width=True
    ):

        st.session_state.count = 0


st.progress(
    st.session_state.count / 108
)

st.markdown(
    f"""
    <div class="counter-number">
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
# BAPPA'S BLESSING
# =========================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">🙏 Bappa\'s Blessings</div>',
    unsafe_allow_html=True
)

if st.button(
    "✨ Receive New Blessing",
    use_container_width=True
):

    st.session_state.blessing = random.randrange(
        len(blessings)
    )

st.markdown(
    f"""
    <div class="blessing-box">
        {html.escape(blessings[st.session_state.blessing])}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# BAPPA'S GREETING
# =========================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">📱 Bappa\'s Greeting</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="greeting-box">

        <div class="greeting-main">
            🙏 Happy Ganesh Chaturthi 2026! 🙏
        </div>

        May Lord Ganesha bless you and your family
        with happiness, peace, prosperity and success.

        <div class="greeting-morya">
            🌺 Ganpati Bappa Morya! 🙏
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FESTIVAL MESSAGE
# =========================================================

messages = [
    "🙏 Happy Ganesh Chaturthi 2026!",
    "🌺 Ganpati Bappa Morya!",
    "🪔 May Bappa bless your family!",
    "✨ Wishing you peace and prosperity!",
    "🌸 Celebrate with devotion and happiness!"
]

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card-title">🎉 Festival Message</div>',
    unsafe_allow_html=True
)

selected_message = st.selectbox(
    "Choose a festival message",
    messages
)

st.markdown(
    f"""
    <div class="message-box">
        {html.escape(selected_message)}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)
# =========================================================
# FINAL FOOTER
# =========================================================
st.markdown(
    """
    <div class="morya">
        🌺 Ganpati Bappa Morya 🙏
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="credit">
        Developed by Rashpreet Kaur Arora | BCA 2nd Year
    </div>
    """,
    unsafe_allow_html=True
)
