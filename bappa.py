import streamlit as st
from PIL import Image
import os
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
    st.session_state.blessing = (
        "🙏 May Bappa bless you with happiness, peace and success. 🙏"
    )

if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = False

if "flower_count" not in st.session_state:
    st.session_state.flower_count = 0


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 50% 10%,
            rgba(255,190,60,0.25),
            transparent 30%
        ),
        linear-gradient(
            180deg,
            #080713 0%,
            #21142b 48%,
            #090812 100%
        );

    color: white;
}

.block-container {
    max-width: 500px !important;
    padding-top: 18px !important;
    padding-left: 12px !important;
    padding-right: 12px !important;
    padding-bottom: 30px !important;
}

.hero {
    text-align: center;
    padding: 8px 5px 14px 5px;
}

.hero-title {
    color: #ffd45c;
    font-size: clamp(29px, 8vw, 42px);
    font-weight: 900;
    line-height: 1.15;
    text-shadow:
        0 0 8px rgba(255,200,70,.45),
        0 0 25px rgba(255,150,30,.20);
}

.hero-year {
    color: #ffad32;
    font-size: 38px;
    font-weight: 900;
    margin-top: 2px;
}

.hero-subtitle {
    color: #fff;
    font-size: 16px;
    line-height: 1.5;
    margin-top: 8px;
}

.gold-line {
    text-align: center;
    color: #ffd45c;
    font-size: 21px;
    letter-spacing: 8px;
    margin: 5px 0 14px 0;
}

.image-box {
    padding: 8px;
    border-radius: 25px;

    background:
        linear-gradient(
            145deg,
            rgba(255,205,90,.18),
            rgba(255,255,255,.03)
        );

    border: 2px solid rgba(255,205,90,.55);

    box-shadow:
        0 0 20px rgba(255,180,40,.22),
        0 0 50px rgba(255,140,20,.10);
}

.image-box img {
    border-radius: 18px !important;
}

.diya-row {
    text-align: center;
    font-size: 28px;
    margin: 13px 0;
    letter-spacing: 22px;
}

.card {
    background: rgba(255,255,255,.055);
    border: 1px solid rgba(255,205,90,.20);
    border-radius: 18px;
    padding: 15px;
    margin-top: 12px;
}

.mantra-display {
    text-align: center;
    color: #ffe5aa;
    font-size: 20px;
    font-weight: 800;
    padding: 10px;
}

.counter {
    text-align: center;
    color: #ffd45c;
    font-size: 28px;
    font-weight: 900;
    margin: 8px;
}

.footer-main {
    text-align: center;
    color: #ffb52e;
    font-size: 21px;
    font-weight: 900;
    margin-top: 22px;
}

.footer-sub {
    text-align: center;
    color: #9294a2;
    font-size: 12px;
    margin-top: 8px;
}

.small-note {
    text-align: center;
    color: #c5c5ca;
    font-size: 13px;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-title">
        ✨ Happy Ganesh Chaturthi ✨
    </div>

    <div class="hero-year">
        2026
    </div>

    <div class="hero-subtitle">
        🙏 May Bappa bless you with joy, peace & prosperity 🙏
    </div>

</div>

<div class="gold-line">
    ✦ ✦ ✦
</div>
""", unsafe_allow_html=True)


# =========================================================
# GANESH IMAGE
# =========================================================

# IMPORTANT:
# Put your actual image file in the SAME GitHub folder
# as bappa.py.

possible_images = [
    "GaneshJi.png",
    "GaneshJi.jpg",
    "file_00000000a74482098265ae866f1a87d0.png"
]

image_path = None

for filename in possible_images:
    if os.path.exists(filename):
        image_path = filename
        break

if image_path:

    try:

        img = Image.open(image_path)

        st.markdown(
            '<div class="image-box">',
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

    st.warning(
        "Ganesh Ji image is not found. "
        "Add GaneshJi.png or GaneshJi.jpg to your GitHub repository."
    )


# =========================================================
# DIYAS
# =========================================================

st.markdown(
    """
    <div class="diya-row">
        🪔 🪔 🪔
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FEATURE 1 - DAILY BLESSING
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🙏 Bappa's Blessing")

blessings = [
    "🙏 May Bappa remove every obstacle from your path. 🙏",

    "🌸 May your life be filled with happiness and peace. 🌸",

    "✨ May Lord Ganesha bless your new beginnings. ✨",

    "🪔 May your home be filled with prosperity and positivity. 🪔",

    "🌺 May Bappa give you wisdom, strength and success. 🌺",

    "🙏 May every difficulty become easier with Bappa's blessings. 🙏"
]

if st.button(
    "✨ Get New Blessing",
    use_container_width=True
):

    st.session_state.blessing = random.choice(blessings)

st.success(st.session_state.blessing)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FEATURE 2 - MANTRA
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🕉️ Divine Mantra")

mantras = [
    "ॐ गं गणपतये नमः",
    "ॐ श्री गणेशाय नमः",
    "गणपति बप्पा मोरया",
    "वक्रतुण्ड महाकाय"
]

selected_mantra = st.selectbox(
    "Select Mantra",
    mantras
)

st.markdown(
    f"""
    <div class="mantra-display">
        {selected_mantra}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FEATURE 3 - 108 MANTRA COUNTER
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🔢 108 Mantra Counter")

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

st.markdown(
    f"""
    <div class="counter">
        {st.session_state.count} / 108
    </div>
    """,
    unsafe_allow_html=True
)

st.progress(
    st.session_state.count / 108
)

if st.session_state.count == 108:

    st.success(
        "🌺 108 Mantra Complete! Ganpati Bappa Morya! 🙏"
    )

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FEATURE 4 - FESTIVAL GREETING
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🎉 Festival Greeting")

greetings = [
    "Happy Ganesh Chaturthi! 🙏",

    "Ganpati Bappa Morya! 🌺",

    "May Bappa bless your family! 🪔",

    "Wishing you peace, prosperity and happiness! ✨",

    "May every new beginning be blessed by Lord Ganesha! 🌸"
]

selected_greeting = st.selectbox(
    "Choose Greeting",
    greetings
)

st.info(selected_greeting)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FEATURE 5 - FLOWER CELEBRATION
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🌸 Flower Celebration")

if st.button(
    "🌺 Offer Flowers to Bappa",
    use_container_width=True
):

    st.session_state.flower_count += 1

    st.balloons()

st.markdown(
    f"""
    <div class="small-note">
        🌸 Flowers offered: {st.session_state.flower_count}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FEATURE 6 - WELCOME MESSAGE
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🪔 Bappa Welcome")

if st.button(
    "🙏 Welcome Bappa",
    use_container_width=True
):

    st.session_state.show_welcome = True

if st.session_state.show_welcome:

    st.success(
        "🌺 गणपति बप्पा मोरया! 🌺\n\n"
        "Welcome Lord Ganesha with devotion, "
        "peace and happiness. 🙏"
    )

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FEATURE 7 - FESTIVAL INFORMATION
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

with st.expander("📖 About Ganesh Chaturthi"):

    st.write(
        "Ganesh Chaturthi is a festival dedicated to "
        "Lord Ganesha. Devotees worship Ganesha as the "
        "remover of obstacles and the symbol of wisdom "
        "and new beginnings."
    )

    st.write(
        "🙏 गणपति बप्पा मोरया 🙏"
    )

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FEATURE 8 - SHARE MESSAGE
# =========================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📱 Share Message")

share_text = (
    "🙏 Happy Ganesh Chaturthi 2026! 🙏\n\n"
    "May Lord Ganesha bless you and your family "
    "with happiness, peace, prosperity and success.\n\n"
    "🌺 Ganpati Bappa Morya! 🌺"
)

st.code(
    share_text,
    language=None
)

st.caption(
    "Copy this message and share it with your family and friends."
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer-main">
        Ganpati Bappa Morya 🙏
    </div>

    <div class="footer-sub">
        Developed by Rashpreet Kaur Arora | BCA 2nd Year
    </div>
    """,
    unsafe_allow_html=True
)
