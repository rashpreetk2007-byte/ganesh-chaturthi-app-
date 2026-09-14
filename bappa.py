import streamlit as st
from PIL import Image
from pathlib import Path
import random
import time

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

if "count" not in st.session_state:
    st.session_state.count = 0

if "blessing" not in st.session_state:
    st.session_state.blessing = 0

if "show_about" not in st.session_state:
    st.session_state.show_about = False

if "animation" not in st.session_state:
    st.session_state.animation = True

# =========================================================
# COLORS
# =========================================================

BG_TOP = "#FFF4E6"
BG_MIDDLE = "#FFE0B8"
BG_BOTTOM = "#FFF8F0"

SAFFRON = "#D96B16"
GOLD = "#F0A51A"
DARK = "#713B20"
PINK = "#D94F87"
GREEN = "#3C8C68"
WHITE = "#FFFFFF"

# =========================================================
# CUSTOM CSS
# =========================================================

animation_css = ""

if st.session_state.animation:
    animation_css = """
    .flower {
        position: fixed;
        z-index: 1;
        pointer-events: none;
        font-size: 24px;
        animation: fall 8s linear infinite;
        opacity: 0.75;
    }

    .flower1 {
        left: 5%;
        animation-delay: 0s;
    }

    .flower2 {
        left: 20%;
        animation-delay: 2s;
    }

    .flower3 {
        left: 40%;
        animation-delay: 4s;
    }

    .flower4 {
        left: 65%;
        animation-delay: 1s;
    }

    .flower5 {
        left: 85%;
        animation-delay: 3s;
    }

    @keyframes fall {
        0% {
            top: -50px;
            transform: rotate(0deg);
            opacity: 0;
        }

        15% {
            opacity: 0.8;
        }

        50% {
            transform: rotate(180deg);
        }

        100% {
            top: 105vh;
            transform: rotate(360deg);
            opacity: 0;
        }
    }

    .sparkle {
        position: fixed;
        z-index: 1;
        pointer-events: none;
        color: #F0A51A;
        font-size: 20px;
        animation: sparkleMove 6s linear infinite;
    }

    .spark1 {
        left: 12%;
        animation-delay: 1s;
    }

    .spark2 {
        left: 50%;
        animation-delay: 3s;
    }

    .spark3 {
        left: 78%;
        animation-delay: 5s;
    }

    @keyframes sparkleMove {
        0% {
            bottom: -30px;
            opacity: 0;
        }

        20% {
            opacity: 1;
        }

        100% {
            bottom: 105vh;
            opacity: 0;
        }
    }
    """

st.markdown(
    f"""
    <style>

    /* =====================================================
       MAIN BACKGROUND
       ===================================================== */

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 15%,
                rgba(255,255,255,0.95),
                transparent 25%
            ),
            linear-gradient(
                180deg,
                {BG_TOP} 0%,
                {BG_MIDDLE} 52%,
                {BG_BOTTOM} 100%
            );

        min-height: 100vh;
    }}

    .block-container {{
        max-width: 520px !important;
        padding-top: 15px !important;
        padding-left: 13px !important;
        padding-right: 13px !important;
        padding-bottom: 35px !important;
        margin: auto;
    }}

    /* =====================================================
       HEADER
       ===================================================== */

    .main-title {{
        text-align: center;
        color: {SAFFRON};
        font-size: clamp(30px, 8vw, 43px);
        font-weight: 900;
        line-height: 1.1;
        margin-top: 5px;
        margin-bottom: 3px;

        text-shadow:
            0 2px 0 #ffffff,
            0 4px 12px rgba(217,107,22,0.25);
    }}

    .year {{
        text-align: center;
        color: {GOLD};
        font-size: 42px;
        font-weight: 900;
        margin-bottom: 8px;
    }}

    .top-message {{
        text-align: center;
        color: {DARK};
        font-size: 17px;
        font-weight: 600;
        line-height: 1.45;
        margin-bottom: 10px;
    }}

    .stars {{
        text-align: center;
        color: {GOLD};
        font-size: 22px;
        letter-spacing: 7px;
        margin-bottom: 13px;
    }}

    /* =====================================================
       IMAGE
       ===================================================== */

    .image-card {{
        position: relative;
        z-index: 3;

        width: 100%;
        padding: 8px;

        border-radius: 25px;

        background:
            linear-gradient(
                145deg,
                #FFFFFF,
                #FFF0D7
            );

        border: 3px solid {GOLD};

        box-shadow:
            0 7px 25px rgba(180,100,20,0.22),
            0 0 35px rgba(240,165,26,0.20);

        margin-bottom: 12px;
    }}

    .image-card img {{
        width: 100% !important;
        height: auto !important;
        max-height: 500px !important;
        object-fit: contain !important;
        border-radius: 18px !important;
        display: block;
    }}

    /* =====================================================
       DIYAS
       ===================================================== */

    .diyas {{
        position: relative;
        z-index: 4;

        display: flex;
        justify-content: center;
        gap: 40px;

        font-size: 28px;

        margin: 8px 0 8px 0;
    }}

    .diya {{
        animation: diyaGlow 1.4s ease-in-out infinite alternate;
    }}

    @keyframes diyaGlow {{
        from {{
            transform: scale(0.90);
            filter: brightness(0.9);
        }}

        to {{
            transform: scale(1.18);
            filter: brightness(1.4);
        }}
    }}

    /* =====================================================
       CARDS
       ===================================================== */

    .card {{
        position: relative;
        z-index: 4;

        background: rgba(255,255,255,0.88);

        border: 1px solid rgba(217,107,22,0.18);

        border-radius: 20px;

        padding: 15px;

        margin-top: 14px;

        box-shadow:
            0 5px 18px rgba(120,70,30,0.10);
    }}

    .card-title {{
        color: {DARK};
        font-size: 23px;
        font-weight: 900;
        margin-bottom: 8px;
    }}

    .mantra-display {{
        text-align: center;

        background:
            linear-gradient(
                135deg,
                #FFF7E8,
                #FFE5C0
            );

        color: {SAFFRON};

        border-radius: 15px;

        padding: 13px;

        font-size: 20px;
        font-weight: 800;

        margin-top: 10px;
    }}

    /* =====================================================
       BLESSING
       ===================================================== */

    .blessing-box {{
        background:
            linear-gradient(
                135deg,
                #E7F7EC,
                #FFF9E8
            );

        border-left: 5px solid {GREEN};

        border-radius: 15px;

        padding: 14px;

        color: #28714E;

        font-size: 16px;

        line-height: 1.55;

        margin-top: 10px;
    }}

    /* =====================================================
       GREETING CARD
       ===================================================== */

    .greeting {{
        background:
            linear-gradient(
                135deg,
                #FFF0F6,
                #FFF8E9
            );

        border-radius: 18px;

        padding: 17px;

        color: {DARK};

        font-size: 16px;

        line-height: 1.65;

        border: 1px solid #F1C8D7;
    }}

    /* =====================================================
       COUNTER
       ===================================================== */

    .counter {{
        text-align: center;
        color: {SAFFRON};
        font-size: 32px;
        font-weight: 900;
        margin: 10px 0;
    }}

    /* =====================================================
       BUTTONS
       ===================================================== */

    .stButton > button {{
        width: 100% !important;

        min-height: 48px;

        border-radius: 15px !important;

        border: 2px solid #E39A20 !important;

        background:
            linear-gradient(
                135deg,
                #E88A17,
                #F4B72D
            ) !important;

        color: white !important;

        font-size: 16px !important;

        font-weight: 800 !important;

        box-shadow:
            0 5px 13px rgba(180,100,20,0.18) !important;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        border-color: {SAFFRON} !important;
    }}

    /* =====================================================
       FOOTER
       ===================================================== */

    .morya {{
        text-align: center;
        color: {SAFFRON};
        font-size: 23px;
        font-weight: 900;
        margin-top: 25px;
    }}

    .credit {{
        text-align: center;
        color: #896F60;
        font-size: 12px;
        margin-top: 10px;
        margin-bottom: 10px;
    }}

    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 400px) {{

        .block-container {{
            padding-left: 10px !important;
            padding-right: 10px !important;
        }}

        .main-title {{
            font-size: 29px;
        }}

        .year {{
            font-size: 38px;
        }}

        .top-message {{
            font-size: 16px;
        }}

        .image-card {{
            padding: 6px;
            border-radius: 21px;
        }}

        .image-card img {{
            max-height: 440px !important;
        }}

        .card-title {{
            font-size: 21px;
        }}

    }}

    /* =====================================================
       HIDE STREAMLIT DEFAULT
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

    {animation_css}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# ANIMATION ELEMENTS
# =========================================================

if st.session_state.animation:

    st.markdown(
        """
        <div class="flower flower1">🌸</div>
        <div class="flower flower2">🌺</div>
        <div class="flower flower3">🌼</div>
        <div class="flower flower4">🌸</div>
        <div class="flower flower5">🌺</div>

        <div class="sparkle spark1">✦</div>
        <div class="sparkle spark2">✧</div>
        <div class="sparkle spark3">✦</div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="main-title">
        🙏 Happy Ganesh Chaturthi
    </div>

    <div class="year">
        2026
    </div>

    <div class="top-message">
        🌸 May Bappa bless you with joy, peace & prosperity 🌸
    </div>

    <div class="stars">
        ✦ ✦ ✦
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# IMAGE
# =========================================================

image_file = Path("file_00000000a74482098265ae866f1a87d0.png")

if image_file.exists():

    try:
        img = Image.open(image_file)

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
        st.error("Ganesh Ji image could not be opened.")

else:
    st.error(
        "Ganesh Ji image not found. "
        "Check the PNG filename in GitHub."
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
# MANTRA
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="card-title">
            🕉️ Divine Mantra
        </div>
    """,
    unsafe_allow_html=True
)

mantra = st.selectbox(
    "Choose a mantra",
    [
        "ॐ गं गणपतये नमः",
        "ॐ श्री गणेशाय नमः",
        "गणपति बप्पा मोरया",
        "वक्रतुण्ड महाकाय"
    ],
    label_visibility="visible"
)

st.markdown(
    f"""
    <div class="mantra-display">
        {mantra}
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# 108 COUNTER
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="card-title">
            🔢 108 Mantra Counter
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    if st.button("🙏 Chant +1", use_container_width=True):

        if st.session_state.count < 108:
            st.session_state.count += 1

        st.rerun()

with col2:

    if st.button("🔄 Reset", use_container_width=True):

        st.session_state.count = 0

        st.rerun()

st.progress(
    st.session_state.count / 108
)

st.markdown(
    f"""
    <div class="counter">
        {st.session_state.count} / 108
    </div>
    </div>
    """,
    unsafe_allow_html=True
        )
# =========================================================
# BLESSINGS
# =========================================================

blessings = [
    "🙏 May Lord Ganesha remove every obstacle and fill your life with happiness, peace and success. 🙏",

    "🌸 May Bappa bring wisdom, prosperity and positivity into your life. 🌸",

    "✨ May every new beginning be blessed by Lord Ganesha. ✨",

    "🪔 May your home be filled with peace, love and divine blessings. 🪔",

    "🌺 May Ganpati Bappa guide you towards success and happiness. 🌺",

    "🙏 May Bappa bless you and your family with good fortune and peace. 🙏"
]

st.markdown(
    """
    <div class="card">
        <div class="card-title">
            🙏 Bappa's Blessings
        </div>
    """,
    unsafe_allow_html=True
)

if st.button(
    "✨ Receive New Blessing",
    use_container_width=True
):

    st.session_state.blessing = random.randrange(
        len(blessings)
    )

    st.rerun()

st.markdown(
    f"""
    <div class="blessing-box">
        {blessings[st.session_state.blessing]}
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# ABOUT GANESH CHATURTHI
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="card-title">
            📖 About Ganesh Chaturthi
        </div>
    """,
    unsafe_allow_html=True
)

if st.button(
    "📚 Read About the Festival",
    use_container_width=True
):

    st.session_state.show_about = not st.session_state.show_about

if st.session_state.show_about:

    st.info(
        "Ganesh Chaturthi is a Hindu festival celebrating "
        "the birth of Lord Ganesha. It is associated with "
        "wisdom, new beginnings, prosperity and the removal "
        "of obstacles."
    )

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================================
# GREETING CARD
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="card-title">
            📱 Bappa's Greeting
        </div>

        <div class="greeting">

        🙏 Happy Ganesh Chaturthi 2026! 🙏

        <br><br>

        May Lord Ganesha bless you and your family
        with happiness, peace, prosperity and success.

        <br><br>

        🌺 Ganpati Bappa Morya! 🌺

        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# ANIMATION SWITCH
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="card-title">
            ✨ Animation
        </div>
    """,
    unsafe_allow_html=True
)

new_animation = st.toggle(
    "🌸 Falling Flowers & Sparkles",
    value=st.session_state.animation
)

if new_animation != st.session_state.animation:

    st.session_state.animation = new_animation

    st.rerun()

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="morya">
        🌺 Ganpati Bappa Morya 🙏
    </div>

    <div class="credit">
        Developed by Rashpreet Kaur Arora | BCA 2nd Year
    </div>
    """,
    unsafe_allow_html=True
)
