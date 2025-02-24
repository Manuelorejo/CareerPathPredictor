import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Career Path Predictor",
    page_icon="🧭",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 20px;
    }
    .title {
        color: #1f77b4;
        text-align: center;
        font-size: calc(1.8rem + 1vw) !important;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #2c3e50;
        text-align: center;
        font-size: calc(1.2rem + 0.5vw) !important;
        margin-bottom: 30px;
    }
    .feature-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
    }
    .feature-icon {
        font-size: 40px;
        text-align: center;
        margin-bottom: 15px;
    }
    .feature-title {
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        color: #1f77b4;
    }
    .cta-button {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 40px;
    }
    .footer {
        text-align: center;
        color: #666;
        padding-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("<h1 class='title'>🧭 Tech Career Advisor</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Discover Your Ideal Tech Career Path</h2>", unsafe_allow_html=True)

# Main image or illustration
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("https://img.freepik.com/free-vector/career-path-concept-illustration_114360-3982.jpg", use_container_width=True)

# Introduction
st.markdown("""
<div style='text-align: center; max-width: 800px; margin: 0 auto; padding: 20px;'>
    <p style='font-size: 18px;'>
        Not sure which tech career path is right for you? Our Tech Career Advisor uses 
        machine learning to analyze your skills and interests to recommend the perfect 
        tech role that matches your unique profile.
    </p>
</div>
""", unsafe_allow_html=True)

# Features section
st.markdown("<h2 style='text-align: center; margin-top: 30px;'>How It Works</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>📋</div>
        <div class='feature-title'>Complete the Assessment</div>
        <p>Answer questions about your skills and interests across 15 technical areas.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>🤖</div>
        <div class='feature-title'>AI Analysis</div>
        <p>Our machine learning algorithm analyzes your responses using data from thousands of tech professionals.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>🎯</div>
        <div class='feature-title'>Get Your Match</div>
        <p>Receive a personalized career recommendation that best matches your skill profile.</p>
    </div>
    """, unsafe_allow_html=True)

# Call to action
st.markdown("""
<div class='cta-button'>
    <a href='/Skills_Assessment' target='_self'>
        <button style='
            background-color: #1f77b4;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
        '>
            Take the Assessment Now
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# Testimonials or additional information
st.markdown("<h2 style='text-align: center; margin-top: 20px;'>Find Your Tech Career</h2>", unsafe_allow_html=True)

career_options = [
    "AI/ML Specialist", "Software Developer", "Database Administrator", 
    "Cyber Security Specialist", "Project Manager", "Business Analyst",
    "Graphics Designer", "Technical Writer", "Networking Engineer"
]

# Display career options in a grid
cols = st.columns(3)
for i, career in enumerate(career_options):
    with cols[i % 3]:
        st.markdown(f"""
        <div style='
            background-color: #f8f9fa;
            border-radius: 5px;
            padding: 10px;
            margin: 5px;
            text-align: center;
        '>
            {career}
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <p>© 2025 Tech Career Advisor | Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
