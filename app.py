import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Alpha Studio",
    page_icon="⚡",
    layout="wide"
)

# --- Custom CSS (Futuristic UI) ---
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    margin-bottom: 40px;
    color: #ccc;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    transition: 0.3s;
    border: 1px solid rgba(255,255,255,0.1);
}

.card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(0,255,255,0.6);
    cursor: pointer;
}

.btn {
    background: linear-gradient(90deg,#00c6ff,#0072ff);
    padding: 10px 25px;
    border-radius: 10px;
    color: white;
    text-decoration: none;
    display: inline-block;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="title">⚡ Alpha Studio</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create the Future with Alpha AI</div>', unsafe_allow_html=True)

# --- Cards Layout ---
col1, col2, col3 = st.columns(3)

# --- AI Tools ---
with col1:
    st.markdown("""
    <div class="card">
        <h2>🧠 AI Tools Hub</h2>
        <p>Text generation, ideas, coding help & more</p>
        <a class="btn">Explore</a>
    </div>
    """, unsafe_allow_html=True)

# --- Alpha AI (CLICKABLE LINK) ---
with col2:
    st.markdown("""
    <a href="https://alpha-ai-dibjvtzmag2vhb8a4knhdh.streamlit.app/" target="_blank">
    <div class="card">
        <h2>🤖 Alpha AI</h2>
        <p>Your smart AI assistant for chat, coding, and creation</p>
        <div class="btn">Open Alpha AI</div>
    </div>
    </a>
    """, unsafe_allow_html=True)

# --- Developer Tools ---
with col3:
    st.markdown("""
    <div class="card">
        <h2>💻 Developer Zone</h2>
        <p>Code, debug & build faster</p>
        <a class="btn">Start</a>
    </div>
    """, unsafe_allow_html=True)

# --- About Section ---
st.markdown("## 🚀 About Alpha Studio")
st.write("""
Alpha Studio is an all-in-one AI-powered creative platform designed to help users build, create, and innovate.

It combines advanced AI tools, smart automation, and modern UI to give the best experience.
""")

# --- Features ---
st.markdown("## 🎨 Features")
st.write("""
- 🧠 AI Tools Hub  
- 🤖 Alpha AI Assistant  
- 🎬 Creative Studio  
- 💻 Developer Tools  
- ☁️ Cloud Project Saving  
""")

# --- Alpha AI Description ---
st.markdown("## 🤖 Alpha AI")
st.write("""
Alpha AI is a powerful assistant that helps with chatting, coding, content creation, and problem-solving in real-time.
""")

# --- Vision ---
st.markdown("## 🌟 Vision")
st.write("Make AI + Creativity available for everyone.")

# --- Footer ---
st.markdown("---")
st.markdown("© 2026 Alpha Studio | Powered by Alpha AI ⚡")
