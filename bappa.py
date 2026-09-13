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

if "flowers" not in st.session_state:
    st.session_state.flowers = 0


# =========================================================
# COMPLETE LIGHT FESTIVE DESIGN
# =========================================================

st.markdown("""
<style>

/* ========================================================
   MAIN PAGE
   ======================================================== */

.stApp {

    min-height: 100vh;

    background:
        radial-gradient(
            circle at 50% 8%,
            rgba(255, 196, 70, 0.42),
            transparent 28%
        ),

        radial-gradient(
            circle at 8% 65%,
            rgba(255, 150, 180, 0.25),
            transparent 25%
        ),

        radial-gradient(
            circle at 92% 70%,
            rgba(255, 210, 90, 0.28),
            transparent 25%
        ),

        linear-gradient(
            180deg,
            #fffaf0 0%,
            #fff0d5 45%,
            #ffe5c4 100%
        );

    color: #5b321c;
}


/* ========================================================
   PHONE CONTAINER
   ======================================================== */

.block-container {

    max-width: 500px !important;

    padding-top: 15px !important;

    padding-left: 12px !important;

    padding-right: 12px !important;

    padding-bottom: 35px !important;

    margin: auto;
}


/* ========================================================
   TITLE
   ======================================================== */

.main-title {

    text-align: center;

    color: #b84f08;

    font-size: clamp(
        28px,
        8vw,
        41px
    );

    font-weight: 900;

    line-height: 1.12;

    margin-top: 4px;

    margin-bottom: 4px;

    text-shadow:
        0 2px 5px rgba(150, 75, 0, 0.15);
}


/* ========================================================
   YEAR
   ======================================================== */

.year {

    text-align: center;

    color: #d87908;

    font-size: 39px;

    font-weight: 900;

    margin-bottom: 8px;
}


/* ========================================================
   SUBTITLE
   ======================================================== */

.subtitle {

    text-align: center;

    color: #63391f;

    font-size: 16px;

    font-weight: 600;

    line-height: 1.5;

    padding: 0 10px;

    margin-bottom: 12px;
}


/* ========================================================
   DECORATION
   ======================================================== */

.decor {

    text-align: center;

    color: #d88916;

    font-size: 20px;

    letter-spacing: 7px;

    margin-bottom: 13px;
}


/* ========================================================
   IMAGE CARD
   ======================================================== */

.image-card {

    width: 100%;

    max-width: 445px;

    margin: auto;

    padding: 8px;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            #fffdf7,
            #fff1d7
        );

    border: 3px solid #e0a52f;

    box-shadow:
        0 5px 20px rgba(150, 85, 20, 0.15),
        0 0 25px rgba(230, 165, 50, 0.25);

    overflow: hidden;
}


/* ========================================================
   IMAGE
   ======================================================== */

.image-card img {

    width: 100% !important;

    max-height: 440px !important;

    object-fit: contain !important;

    border-radius: 17px !important;

    display: block;

    margin: auto;
}


/* ========================================================
   DIYAS
   ======================================================== */

.diya-row {

    text-align: center;

    font-size: 27px;

    margin-top: 13px;

    margin-bottom: 12px;

    letter-spacing: 14px;
}


/* ========================================================
   SECTION CARDS
   ======================================================== */

.section-card {

    background:
        rgba(
            255,
            255,
            255,
            0.78
        );

    border:

        1px solid
        rgba(
            205,
            130,
            35,
            0.25
        );

    border-radius: 19px;

    padding: 14px;

    margin-top: 13px;

    box-shadow:
        0 5px 18px
        rgba(
            140,
            75,
            20,
            0.09
        );
}


/* ========================================================
   SECTION HEADINGS
   ======================================================== */

.section-card h3 {

    color: #9b470c !important;

    font-weight: 800 !important;
}


/* ========================================================
   MANTRA
   ======================================================== */

.mantra {

    text-align: center;

    color: #a94e08;

    font-size: 20px;

    font-weight: 800;

    padding: 10px 5px;
}


/* ========================================================
   COUNTER
   ======================================================== */

.counter {

    text-align: center;

    color: #c46308;

    font-size: 29px;

    font-weight: 900;

    margin: 7px 0;
}


/* ========================================================
   BUTTONS
   ======================================================== */

.stButton > button {

    width: 100%;

    min-height: 48px;

    border-radius: 14px;

    border: 2px solid #d99327;

    background:
        linear-gradient(
            135deg,
            #e08a18,
            #f2b632
        );

    color: white;

    font-size: 15px;

    font-weight: 800;

    box-shadow:
        0 4px 10px
        rgba(
            170,
            90,
            15,
            0.15
        );

    transition: 0.2s;
}


.stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #d97508,
            #eda929
        );

    color: white;

    transform: translateY(-1px);
}


/* ========================================================
   SELECTBOX
   ======================================================== */

.stSelectbox label {

    color: #63391f !important;

    font-weight: 700 !important;
}


/* ========================================================
   TOGGLE
   ======================================================== */

.stCheckbox label {

    color: #63391f !important;

    font-weight: 700 !important;
}


/* ========================================================
   INFO / SUCCESS
   ======================================================== */

.stSuccess {

    border-radius: 14px;
}

.stInfo {

    border-radius: 14px;
}


/* ========================================================
   FOOTER
   ======================================================== */

.footer-main {

    text-align: center;

    color: #b65308;

    font-size: 21px;

    font-weight: 900;

    margin-top: 23px;
}


.footer-credit {

    text-align: center;

    color: #795c4b;

    font-size: 12px;

    margin-top: 9px;
}


/* ========================================================
   MOBILE
   ======================================================== */

@media (max-width: 400px) {

    .block-container {

        padding-left: 9px !important;

        padding-right: 9px !important;
    }

    .main-title {

        font-size: 29px;
    }

    .year {

        font-size: 36px;
    }

    .subtitle {

        font-size: 15px;
    }

    .image-card {

        padding: 6px;

        border-radius: 20px;
    }

    .image-card img {

        max-height: 390px !important;
    }

    .diya-row {

        font-size: 24px;

        letter-spacing: 9px;
    }

}


/* ========================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
   ======================================================== */

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
# TOP TITLE
# =========================================================

st.markdown(
    '<div class="main-title">'
    '🙏 Happy Ganesh Chaturthi 🙏'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="year">2026</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🌸 May Bappa bless you with joy, peace & prosperity 🌸'
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

image_files = [
    "GaneshJi.png",
    "GaneshJi.jpg",
    "file_00000000a74482098265ae866f1a87d0.png"
]

image_path = None

for file_name in image_files:

    if os.path.exists(file_name):

        image_path = file_name
        break


if image_path is not None:

    try:

        ganesh_image = Image.open(image_path)

        if ganesh_image.mode not in ["RGB", "RGBA"]:

            ganesh_image = ganesh_image.convert("RGB")

        st.markdown(
            '<div class="image-card">',
            unsafe_allow_html=True
        )

        st.image(
            ganesh_image,
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

    st.warning(
        "Ganesh Ji image not found."
    )

    st.info(
        "Upload GaneshJi.png in the same GitHub folder as bappa.py."
    )


# =========================================================
# DIYAS
# =========================================================

st.markdown(
    '<div class="diya-row">🪔 🪔 🪔</div>',
    unsafe_allow_html=True
)


# =========================================================
# FEATURE 1
# DAILY BLESSING
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🙏 Bappa's Blessing")

blessings = [

    "🙏 May Bappa remove every obstacle from your path. 🙏",

    "🌸 May your life be filled with happiness and peace. 🌸",

    "✨ May Lord Ganesha bless all your new beginnings. ✨",

    "🪔 May your home be filled with prosperity and positivity. 🪔",

    "🌺 May Bappa give you wisdom, strength and success. 🌺",

    "🙏 May every difficulty become easier with Bappa's blessings. 🙏"

]

if st.button(
    "✨ Receive New Blessing",
    key="blessing_button",
    use_container_width=True
):

    st.session_state.blessing = random.choice(
        blessings
    )

st.success(
    st.session_state.blessing
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FEATURE 2
# MANTRA
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🕉️ Divine Mantra")

mantras = [

    "ॐ गं गणपतये नमः",

    "ॐ श्री गणेशाय नमः",

    "गणपति बप्पा मोरया",

    "वक्रतुण्ड महाकाय"

]

selected_mantra = st.selectbox(
    "Choose a mantra",
    mantras,
    key="mantra_select"
)

st.markdown(
    f'<div class="mantra">{selected_mantra}</div>',
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FEATURE 3
# 108 MANTRA COUNTER
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🔢 108 Mantra Counter")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🙏 Chant +1",
        key="chant_button",
        use_container_width=True
    ):

        if st.session_state.count < 108:

            st.session_state.count += 1


with col2:

    if st.button(
        "🔄 Reset",
        key="reset_button",
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
        "🌺 108 Mantra Complete! "
        "Ganpati Bappa Morya! 🙏"
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FEATURE 4
# FLOWER OFFERING
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🌸 Offer Flowers")

if st.button(
    "🌺 Offer Flower to Bappa",
    key="flower_button",
    use_container_width=True
):

    st.session_state.flowers += 1

    st.toast(
        "🌸 Flower offered to Bappa! 🙏"
    )

st.markdown(
    f"""
    <div class="counter">
        🌸 {st.session_state.flowers} Flowers
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FEATURE 5
# FESTIVAL GREETING
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("🎉 Festival Greeting")

greetings = [

    "Happy Ganesh Chaturthi! 🙏",

    "Ganpati Bappa Morya! 🌺",

    "May Bappa bless your family! 🪔",

    "Wishing you peace, prosperity and happiness! ✨",

    "May every new beginning be blessed by Lord Ganesha! 🌸"

]

selected_greeting = st.selectbox(
    "Choose your greeting",
    greetings,
    key="greeting_select"
)

st.info(
    selected_greeting
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FEATURE 6
# ABOUT GANESH CHATURTHI
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

with st.expander("📖 About Ganesh Chaturthi"):

    st.write(
        "Ganesh Chaturthi is a festival dedicated to "
        "Lord Ganesha, who is traditionally worshipped "
        "as the remover of obstacles and a symbol of "
        "wisdom and auspicious beginnings."
    )

    st.write(
        "🙏 गणपति बप्पा मोरया 🙏"
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FEATURE 7
# SHARE MESSAGE
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("📱 Share Bappa's Message")

share_message = """
🙏 Happy Ganesh Chaturthi 2026! 🙏

May Lord Ganesha bless you and your family
with happiness, peace, prosperity and success.

🌺 Ganpati Bappa Morya! 🌺
"""

st.code(
    share_message,
    language=None
)

st.caption(
    "Copy this message and share it with your family and friends."
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FINAL MESSAGE
# =========================================================

st.markdown(
    """
    <div class="footer-main">
        🌺 Ganpati Bappa Morya 🙏
    </div>

    <div class="footer-credit">
        Developed by Rashpreet Kaur Arora | BCA 2nd Year
    </div>
    """,
    unsafe_allow_html=True
)
