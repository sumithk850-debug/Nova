import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Alpha Studio & Shop",
    page_icon="🎬",
    layout="wide"
)

# --- CSS ---
st.markdown("""
<style>
body {
    margin:0;
}

/* HERO SECTION */
.hero {
    position: relative;
    height: 500px;
    background-image: url("https://images.unsplash.com/photo-1516035069371-29a1b244cc32");
    background-size: cover;
    background-position: center;
    border-radius: 20px;
}

.hero-overlay {
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background: linear-gradient(to right, rgba(0,0,0,0.8), rgba(0,0,0,0.2));
    border-radius: 20px;
}

.hero-text {
    position:absolute;
    top:50%;
    left:50px;
    transform:translateY(-50%);
    color:white;
}

.hero-text h1 {
    font-size:50px;
    margin-bottom:10px;
}

.btn {
    padding:10px 20px;
    background:#ff6600;
    color:white;
    border-radius:5px;
    text-decoration:none;
    margin-right:10px;
}

/* CARDS */
.card {
    background:#111;
    border-radius:15px;
    overflow:hidden;
    transition:0.3s;
}

.card:hover {
    transform:scale(1.05);
}

.card img {
    width:100%;
}

.card-body {
    padding:15px;
    color:white;
}

.section-title {
    font-size:28px;
    margin-top:30px;
    margin-bottom:20px;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
    <div class="hero-overlay"></div>
    <div class="hero-text">
        <h1>Welcome to Alpha Studio & Shop</h1>
        <p>Your hub for professional video production and gear</p>
        <a href="#" class="btn">Explore Films</a>
        <a href="#" class="btn">Visit Shop</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- FEATURED SECTION ---
st.markdown('<div class="section-title">Featured Films & Videos</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

def film_card(title, img):
    return f"""
    <div class="card">
        <img src="{img}">
        <div class="card-body">
            <h4>{title}</h4>
        </div>
    </div>
    """

with col1:
    st.markdown(film_card("Action Short",
    "https://images.unsplash.com/photo-1505685296765-3a2736de412f"), unsafe_allow_html=True)

with col2:
    st.markdown(film_card("Music Video",
    "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4"), unsafe_allow_html=True)

with col3:
    st.markdown(film_card("Drama Film",
    "https://images.unsplash.com/photo-1497032205916-ac775f0649ae"), unsafe_allow_html=True)

# --- SERVICES ---
st.markdown('<div class="section-title">Professional Services</div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    st.markdown(film_card("Video Production",
    "https://images.unsplash.com/photo-1519183071298-a2962eadc59f"), unsafe_allow_html=True)

with col5:
    st.markdown(film_card("Editing & Post-Production",
    "https://images.unsplash.com/photo-1485846234645-a62644f84728"), unsafe_allow_html=True)

# --- SHOP ---
st.markdown('<div class="section-title">Shop for Gear & Accessories</div>', unsafe_allow_html=True)

col6, col7 = st.columns(2)

with col6:
    st.markdown(film_card("Cameras",
    "https://images.unsplash.com/photo-1516724562728-afc824a36e84"), unsafe_allow_html=True)

with col7:
    st.markdown(film_card("Accessories",
    "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f"), unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<center style='color:gray;margin-top:40px;'>© 2026 Alpha Studio</center>", unsafe_allow_html=True)
