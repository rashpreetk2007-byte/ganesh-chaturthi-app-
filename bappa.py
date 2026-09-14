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

if "flowers" not in st.session_state:
    st.session_state.flowers = 0

if "blessing" not in st.session_state:
    st.session_state.blessing = (
        "🙏 May Bappa bless you with happiness, peace and success. 🙏"
    )


# =========================================================
# THEME
# =========================================================

theme = st.selectbox(
    "🎨 Choose Theme",
    [
        "🌅 Cream & Saffron",
        "🌸 Divine Pink",
        "🌼 Golden Festive",
        "💙 Divine Sky"
    ]
)


# =========================================================
# ANIMATION
# =========================================================

animation = st.toggle(
    "✨ Enable Animation",
    value=True
)


# =========================================================
# THEME COLOURS
# =========================================================

if theme == "🌸 Divine Pink":

    background = """
        radial-gradient(circle at 50% 8%,
        rgba(255,150,180,0.38),
        transparent 30%),
        linear-gradient(
        180deg,
        #fff5f7 0%,
        #ffe2e8 50%,
        #fff0e5 100%
        )
    """

    title_color = "#b83268"
    accent_color = "#d94f82"

elif theme == "🌼 Golden Festive":

    background = """
        radial-gradient(circle at 50% 8%,
        rgba(255,190,45,0.45),
        transparent 30%),
        linear-gradient(
        180deg,
        #fffbed 0%,
        #ffedb8 50%,
        #fff1d5 100%
        )
    """

    title_color = "#a85b00"
    accent_color = "#d98208"

elif theme == "💙 Divine Sky":

    background = """
        radial-gradient(circle at 50% 8%,
        rgba(110,190,255,0.30),
        transparent 30%),
        linear-gradient(
        180deg,
        #f7fcff 0%,
        #dff2ff 50%,
        #fff1dc 100%
        )
    """

    title_color = "#17649b"
    accent_color = "#287fb8"

else:

    background = """
        radial-gradient(circle at 50% 8%,
        rgba(255,195,65,0.42),
        transparent 30%),

        radial-gradient(circle at 8% 65%,
        rgba(255,150,180,0.24),
        transparent 25%),

        radial-gradient(circle at 92% 70%,
        rgba(255,210,90,0.25),
        transparent 25%),

        linear-gradient(
        180deg,
        #fffaf0 0%,
        #fff0d5 48%,
        #ffe5c4 100%
        )
    """

    title_color = "#b84f08"
    accent_color = "#d87908"


# =========================================================
# MAIN CSS
# =========================================================

st.markdown(
    f"""
<style>

* {{
    box-sizing: border-box;
}}


/* =====================================================
   BACKGROUND
   ===================================================== */

.stApp {{

    min-height: 100vh;

    background:
        {background};

    color: #5b321c;
}}


/* =====================================================
   PHONE CONTAINER
   ===================================================== */

.block-container {{

    max-width: 500px !important;

    padding-top: 14px !important;

    padding-left: 11px !important;

    padding-right: 11px !important;

    padding-bottom: 35px !important;

    margin: auto;
}}


/* =====================================================
   TITLE
   ===================================================== */

.main-title {{

    text-align: center;

    color: {title_color};

    font-size: clamp(
        28px,
        8vw,
        42px
    );

    font-weight: 900;

    line-height: 1.12;

    margin-top: 5px;

    margin-bottom: 3px;

    animation:
        titleGlow 2.5s ease-in-out infinite alternate;
}}


@keyframes titleGlow {{

    from {{

        text-shadow:
            0 2px 5px
            rgba(150,75,0,0.12);
    }}

    to {{

        text-shadow:
            0 2px 8px
            rgba(220,130,20,0.35),

            0 0 20px
            rgba(255,190,60,0.25);
    }}
}}


/* =====================================================
   YEAR
   ===================================================== */

.year {{

    text-align: center;

    color: {accent_color};

    font-size: 39px;

    font-weight: 900;

    line-height: 1;

    margin-bottom: 9px;
}}


/* =====================================================
   SUBTITLE
   ===================================================== */

.subtitle {{

    text-align: center;

    color: #63391f;

    font-size: 16px;

    font-weight: 650;

    line-height: 1.5;

    padding: 0 9px;

    margin-bottom: 12px;
}}


/* =====================================================
   DECORATION
   ===================================================== */

.decor {{

    text-align: center;

    color: {accent_color};

    font-size: 20px;

    letter-spacing: 7px;

    margin-bottom: 13px;
}}


/* =====================================================
   IMAGE CARD
   ===================================================== */

.image-card {{

    width: 100%;

    max-width: 445px;

    margin: auto;

    padding: 8px;

    border-radius: 25px;

    background:
        linear-gradient(
            145deg,
            #fffefa,
            #fff0d2
        );

    border: 3px solid #dfa52f;

    overflow: hidden;

    animation:
        imageGlow 3s ease-in-out infinite alternate;
}}


@keyframes imageGlow {{

    from {{

        box-shadow:
            0 5px 20px
            rgba(150,85,20,0.14),

            0 0 18px
            rgba(230,165,50,0.20);
    }}

    to {{

        box-shadow:
            0 5px 20px
            rgba(150,85,20,0.14),

            0 0 40px
            rgba(230,165,50,0.45);
    }}
}}


/* =====================================================
   GANESH IMAGE
   ===================================================== */

.image-card img {{

    width: 100% !important;

    max-height: 440px !important;

    object-fit: contain !important;

    border-radius: 18px !important;

    display: block;

    margin: auto;
}}


/* =====================================================
   DIYAS
   ===================================================== */

.diya-row {{

    text-align: center;

    font-size: 27px;

    letter-spacing: 12px;

    margin-top: 14px;

    margin-bottom: 13px;

    animation:
        diyaGlow 1.7s ease-in-out infinite alternate;
}}


@keyframes diyaGlow {{

    from {{

        transform: scale(0.98);

        filter: brightness(0.95);
    }}

    to {{

        transform: scale(1.05);

        filter: brightness(1.18);
    }}
}}


/* =====================================================
   CARDS
   ===================================================== */

.section-card {{

    background:
        rgba(
            255,
            255,
            255,
            0.80
        );

    border:
        1px solid
        rgba(
            205,
            130,
            35,
            0.27
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
}}


/* =====================================================
   HEADINGS
   ===================================================== */

.section-card h3 {{

    color: #98450b !important;

    font-weight: 850 !important;
}}


/* =====================================================
   MANTRA
   ===================================================== */

.mantra {{

    text-align: center;

    color: #a94e08;

    font-size: 20px;

    font-weight: 800;

    padding: 10px 4px;
}}


/* =====================================================
   COUNTER
   ===================================================== */

.counter {{

    text-align: center;

    color: {accent_color};

    font-size: 29px;

    font-weight: 900;

    margin: 8px 0;
}}


/* =====================================================
   BUTTONS
   ===================================================== */

.stButton > button {{

    width: 100%;

    min-height: 48px;

    border-radius: 14px;

    border: 2px solid #d89427;

    background:
        linear-gradient(
            135deg,
            #df8617,
            #f1b532
        );

    color: white;

    font-size: 15px;

    font-weight: 800;

    box-shadow:
        0 4px 11px
        rgba(
            170,
            90,
            15,
            0.16
        );

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}}


.stButton > button:hover {{

    transform: translateY(-2px);

    box-shadow:
        0 6px 15px
        rgba(
            170,
            90,
            15,
            0.22
        );

    color: white;
}}


/* =====================================================
   SELECTBOX
   ===================================================== */

.stSelectbox label {{

    color: #63391f !important;

    font-weight: 700 !important;
}}


/* =====================================================
   TOGGLE
   ===================================================== */

.stCheckbox label {{

    color: #63391f !important;

    font-weight: 700 !important;
}}


/* =====================================================
   FOOTER
   ===================================================== */

.footer-main {{

    text-align: center;

    color: {title_color};

    font-size: 22px;

    font-weight: 900;

    margin-top: 24px;
}}


.footer-credit {{

    text-align: center;

    color: #795c4b;

    font-size: 12px;

    margin-top: 9px;
}}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width:400px) {{

    .block-container {{

        padding-left: 8px !important;

        padding-right: 8px !important;
    }}

    .main-title {{

        font-size: 29px;
    }}

    .year {{

        font-size: 36px;
    }}

    .subtitle {{

        font-size: 15px;
    }}

    .image-card {{

        padding: 6px;

        border-radius: 21px;
    }}

    .image-card img {{

        max-height: 390px !important;
    }}

    .diya-row {{

        font-size: 24px;

        letter-spacing: 8px;
    }}

}}


/* =====================================================
   HIDE STREAMLIT DEFAULT UI
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
# FLOATING ANIMATION
# =========================================================

if animation:

    st.markdown(
        """
<style>

.festive-animation {

    position: fixed;

    inset: 0;

    width: 100%;

    height: 100%;

    pointer-events: none;

    overflow: hidden;

    z-index: 0;
}


.float-item {

    position: absolute;

    bottom: -60px;

    opacity: 0;

    animation:
        floatUp linear infinite;
}


.flower {

    font-size: 22px;
}


.f1 {

    left: 4%;

    animation-duration: 8s;

    animation-delay: 0s;
}


.f2 {

    left: 18%;

    animation-duration: 10s;

    animation-delay: 2s;
}


.f3 {

    left: 34%;

    animation-duration: 9s;

    animation-delay: 4s;
}


.f4 {

    left: 51%;

    animation-duration: 11s;

    animation-delay: 1s;
}


.f5 {

    left: 69%;

    animation-duration: 8s;

    animation-delay: 3s;
}


.f6 {

    left: 87%;

    animation-duration: 10s;

    animation-delay: 5s;
}


.star {

    font-size: 16px;
}


.s1 {

    left: 10%;

    animation-duration: 7s;

    animation-delay: 1s;
}


.s2 {

    left: 28%;

    animation-duration: 9s;

    animation-delay: 3s;
}


.s3 {

    left: 46%;

    animation-duration: 8s;

    animation-delay: 0s;
}


.s4 {

    left: 65%;

    animation-duration: 10s;

    animation-delay: 4s;
}


.s5 {

    left: 83%;

    animation-duration: 7s;

    animation-delay: 2s;
}


@keyframes floatUp {

    0% {

        transform:
            translateY(0)
            rotate(0deg)
            scale(0.7);

        opacity: 0;
    }

    15% {

        opacity: 0.8;
    }

    50% {

        transform:
            translateY(-50vh)
            rotate(120deg)
            scale(1);
    }

    85% {

        opacity: 0.6;
    }

    100% {

        transform:
            translateY(-115vh)
            rotate(260deg)
            scale(1.2);

        opacity: 0;
    }
}

</style>


<div class="festive-animation">

    <div class="float-item flower f1">🌸</div>

    <div class="float-item flower f2">🌺</div>

    <div class="float-item flower f3">🌼</div>

    <div class="float-item flower f4">🌸</div>

    <div class="float-item flower f5">🌺</div>

    <div class="float-item flower f6">🌼</div>


    <div class="float-item star s1">✦</div>

    <div class="float-item star s2">✧</div>

    <div class="float-item star s3">✨</div>

    <div class="float-item star s4">✦</div>

    <div class="float-item star s5">✧</div>

</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="main-title">
        🙏 Happy Ganesh Chaturthi 🙏
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="year">
        2026
    </div>
    """,
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
    """
    <div class="decor">
        ✦ ✦ ✦
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# GANESH JI IMAGE
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


if image_path:

    try:

        ganesh_image = Image.open(image_path)

        if ganesh_image.mode not in [
            "RGB",
            "RGBA"
        ]:

            ganesh_image = ganesh_image.convert(
                "RGB"
            )

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
        "🙏 Ganesh Ji image not found."
    )

    st.info(
        "Put GaneshJi.png in the same GitHub folder as bappa.py."
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
# BLESSING
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
# DIVINE MANTRA
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
    f"""
    <div class="mantra">
        {selected_mantra}
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
        "🌺 108 Mantra Complete! Ganpati Bappa Morya! 🙏"
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
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
# ABOUT GANESH CHATURTHI
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("📖 About Ganesh Chaturthi")

with st.expander("Read about the festival"):

    st.write(
        "Ganesh Chaturthi is a festival dedicated "
        "to Lord Ganesha. He is traditionally "
        "worshipped as a symbol of wisdom, "
        "auspicious beginnings and the remover "
        "of obstacles."
    )

    st.write(
        "🙏 गणपति बप्पा मोरया 🙏"
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SHARE MESSAGE
# =========================================================

st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True
)

st.subheader("📱 Bappa's Greeting")

share_message = """🙏 Happy Ganesh Chaturthi 2026! 🙏

May Lord Ganesha bless you and your family
with happiness, peace, prosperity and success.

🌺 Ganpati Bappa Morya! 🌺"""

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
# FINAL FOOTER
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
