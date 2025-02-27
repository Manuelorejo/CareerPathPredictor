import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Tech Career Advisor",
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
# Replace the career options section with this interactive version
st.markdown("<h2 style='text-align: center; margin-top: 20px;'>Find Your Tech Career</h2>", unsafe_allow_html=True)

# Dictionary with career options and their descriptions
career_info = {
    "AI/ML Specialist": "AI/ML Specialists develop algorithms and models that enable computers to learn from data. They work on applications like natural language processing, computer vision, and predictive analytics. This role requires strong mathematics, statistics, and programming skills.",
    
    "Software Developer": "Software Developers design, code, and test computer programs for applications and operating systems. They collaborate with teams to create software solutions that meet user needs. This role requires programming skills, problem-solving abilities, and attention to detail.",
    
    "Database Administrator": "Database Administrators manage and maintain database systems to ensure data integrity, security, and performance. They design database structures, implement backup solutions, and optimize queries. This role requires SQL expertise and a good understanding of data management principles.",
    
    "Cyber Security Specialist": "Cyber Security Specialists protect systems and networks from digital threats. They implement security measures, conduct vulnerability assessments, and respond to security incidents. This role requires knowledge of security protocols, threat detection, and risk management.",
    
    "Project Manager": "Project Managers plan, execute, and close technology projects. They manage resources, timelines, and team coordination to ensure successful project delivery. This role requires leadership skills, organizational abilities, and technical knowledge.",
    
    "Business Analyst": "Business Analysts bridge the gap between IT and business needs. They gather requirements, analyze processes, and recommend technology solutions to improve business operations. This role requires analytical thinking, communication skills, and business acumen.",
    
    "Graphics Designer": "Graphics Designers in tech create visual elements for websites, applications, and digital products. They work on user interfaces, logos, and visual branding. This role requires creativity, design software expertise, and an understanding of user experience principles.",
    
    "Technical Writer": "Technical Writers create documentation for software, hardware, and technical processes. They translate complex information into clear, user-friendly content. This role requires excellent writing skills, attention to detail, and the ability to understand technical concepts.",
    
    "Networking Engineer": "Networking Engineers design, implement, and maintain computer networks. They configure hardware, troubleshoot connectivity issues, and ensure network security and performance. This role requires knowledge of networking protocols, hardware, and security principles."
}

# Display career options in a grid with expandable information
cols = st.columns(3)
for i, (career, description) in enumerate(career_info.items()):
    with cols[i % 3]:
        with st.expander(career):
            st.write(description)
# Footer
st.markdown("""
<div class='footer'>
    <p>© 2025 Tech Career Advisor | Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)