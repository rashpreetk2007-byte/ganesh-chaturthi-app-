import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Happy Ganesh Chaturthi 2026", page_icon="🙏", layout="centered")

if "count" not in st.session_state:
    st.session_state.count = 0

with st.sidebar:
    st.header("🎨 Choose Theme")
    theme = st.selectbox("Theme", ["Royal Gold", "Saffron Sunrise", "Pink Lotus", "Emerald Divine"])
    animation = st.toggle("✨ Enable Animation", True)
    uploaded = st.file_uploader("🖼️ Upload Ganesh Ji Image", type=["jpg", "jpeg", "png", "webp"])

themes = {
    "Royal Gold": ("#FFF8E8", "#FFE8C2", "#D88900", "#F4B41A", "#633A24"),
    "Saffron Sunrise": ("#FFF6E8", "#FFD9A8", "#D65A00", "#F39A18", "#66351E"),
    "Pink Lotus": ("#FFF7FA", "#FFE0EA", "#B53B67", "#E989A7", "#633142"),
    "Emerald Divine": ("#F4FFF9", "#D9F2E4", "#247A54", "#5DBA83", "#214D39"),
}
bg1, bg2, accent, accent2, text = themes[theme]

fall_css = """
@keyframes fall {
0%{transform:translateY(-80px) rotate(0deg);opacity:0}
15%{opacity:1} 85%{opacity:1}
100%{transform:translateY(100vh) rotate(360deg);opacity:0}
}
.fall{position:fixed;top:-50px;font-size:25px;z-index:9999;pointer-events:none;animation:fall 8s linear infinite}
.f1{left:8%;animation-delay:0s}.f2{left:25%;animation-delay:2s}
.f3{left:43%;animation-delay:4s}.f4{left:62%;animation-delay:1s}
.f5{left:80%;animation-delay:3s}.f6{left:94%;animation-delay:5s}
"""
if not animation:
    fall_css = ""

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
.stApp{{background:linear-gradient(135deg,{bg1},{bg2});font-family:Poppins,sans-serif}}
.block-container{{max-width:760px;padding:1rem .9rem 3rem}}
.hero{{text-align:center;padding:20px 5px}}
.title{{font-size:clamp(2rem,8vw,3.2rem);font-weight:800;color:{accent};line-height:1.1}}
.year{{font-size:clamp(2.5rem,10vw,4rem);font-weight:800;color:{accent2}}}
.subtitle{{font-size:1rem;font-weight:600;color:{text}}}
.divider{{height:6px;border-radius:20px;background:linear-gradient(90deg,transparent,{accent2},transparent);margin:12px 0 20px}}
.card{{background:rgba(255,255,255,.86);border:1px solid {accent2};border-radius:24px;padding:20px;margin:18px 0;box-shadow:0 10px 28px rgba(90,55,20,.12)}}
.section{{font-size:1.45rem;font-weight:800;color:{text};margin-bottom:12px}}
.ganesh{{width:100%;border-radius:18px;display:block;max-height:700px;object-fit:cover}}
.frame{{border:5px solid {accent2};border-radius:25px;padding:6px;background:white;overflow:hidden}}
.placeholder{{height:380px;border-radius:18px;background:radial-gradient(circle,#FFE9A8,#F2B83F);display:flex;align-items:center;justify-content:center;text-align:center;color:#6B3D12;font-size:5rem}}
.mantra{{background:linear-gradient(135deg,#FFF4D5,#FFE7A7);border:1px solid {accent2};border-radius:20px;padding:22px;text-align:center;color:{accent};font-size:1.3rem;font-weight:700}}
.blessing{{background:#E1F5E9;border:1px solid #B8DFC7;border-radius:20px;padding:18px;text-align:center;color:#28714A;font-weight:700}}
.counter{{text-align:center;color:{accent};font-size:2.6rem;font-weight:800;margin:12px}}
.bar{{height:13px;background:white;border-radius:20px;overflow:hidden;border:1px solid {accent2}}}
.fill{{height:100%;width:{st.session_state.count/108*100:.2f}%;background:linear-gradient(90deg,{accent},{accent2});border-radius:20px}}
.greeting{{text-align:center;color:{text};line-height:1.8;font-size:1rem}}
.greeting-main{{font-size:1.2rem;font-weight:700;color:{accent}}}
.morya{{font-size:1.3rem;font-weight:800;color:{accent};margin-top:12px}}
.footer{{text-align:center;padding:28px 5px 5px;color:{text}}}
.footer-main{{font-size:1.5rem;font-weight:800;color:{accent}}}
{fall_css}
</style>
""", unsafe_allow_html=True)

if animation:
    st.markdown("""
    <div class="fall f1">🌸</div><div class="fall f2">🌺</div>
    <div class="fall f3">🌼</div><div class="fall f4">✦</div>
    <div class="fall f5">🌸</div><div class="fall f6">🌺</div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<div class="title">🙏 Happy Ganesh Chaturthi</div>
<div class="year">2026</div>
<div class="subtitle">🌸 May Bappa bless you with joy, peace & prosperity 🌸</div>
<div>✦ &nbsp; ✦ &nbsp; ✦</div>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

if uploaded:
    data = base64.b64encode(uploaded.getvalue()).decode()
    mime = uploaded.type
    st.markdown(f'<div class="frame"><img class="ganesh" src="data:{mime};base64,{data}" alt="Ganesh Ji"></div>', unsafe_allow_html=True)
elif Path("GaneshJi.jpg").exists():
    data = base64.b64encode(Path("GaneshJi.jpg").read_bytes()).decode()
    st.markdown(f'<div class="frame"><img class="ganesh" src="data:image/jpeg;base64,{data}" alt="Ganesh Ji"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="frame"><div class="placeholder">🙏<br><span style="font-size:1rem">Upload Ganesh Ji image from the sidebar</span></div></div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center;font-size:2rem;padding:14px">🪔 &nbsp; 🪔 &nbsp; 🪔</div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="section">🕉️ Divine Mantra</div>', unsafe_allow_html=True)
mantra = st.selectbox("Choose a mantra", [
    "ॐ गं गणपतये नमः", "ॐ श्री गणेशाय नमः", "गणपति बप्पा मोरया", "वक्रतुण्ड महाकाय"
])
st.markdown(f'<div class="mantra">{mantra}</div></div>', unsafe_allow_html=True)

st.markdown('<div class="card"><div class="section">🔢 108 Mantra Counter</div>', unsafe_allow_html=True)
a, b = st.columns(2)
with a:
    if st.button("🙏 Chant +1", use_container_width=True):
        if st.session_state.count < 108:
            st.session_state.count += 1
        st.rerun()
with b:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.count = 0
        st.rerun()
st.markdown(f'<div class="counter">{st.session_state.count} / 108</div><div class="bar"><div class="fill"></div></div></div>', unsafe_allow_html=True)

st.markdown('<div class="blessing">🌸 May Bappa bring wisdom, prosperity and positivity into your life. 🌸</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<div class="section">📱 Bappa's Greeting</div>
<div class="greeting">
<div class="greeting-main">🙏 Happy Ganesh Chaturthi 2026! 🙏</div><br>
May Lord Ganesha bless you and your family with happiness, peace, prosperity and success.
<div class="morya">🌺 Ganpati Bappa Morya! 🙏</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card"><div class="section">🎉 Festival Message</div>', unsafe_allow_html=True)
message = st.selectbox("Choose a festival message", [
    "🙏 Happy Ganesh Chaturthi 2026!",
    "🌺 Ganpati Bappa Morya 🙏",
    "🌸 May Bappa bless your home with happiness and peace.",
    "🕉️ Wishing you wisdom, prosperity and new beginnings."
])
st.markdown(f'<div class="mantra">{message}</div></div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
<div class="footer-main">🌺 Ganpati Bappa Morya 🙏</div>
<div>Developed by Rashpreet Kaur Arora | BCA 2nd Year</div>
</div>
""", unsafe_allow_html=True)
