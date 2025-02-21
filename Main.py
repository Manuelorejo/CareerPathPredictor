import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import StackingClassifier

# Set page configuration
st.set_page_config(
    page_title="Career Path Predictor",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    /* Base styles */
    .main {
        padding: 10px;
    }
    
    /* Form styling */
    .stForm {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Text colors and spacing */
    h1 {
        color: #1f77b4 !important;
        text-align: center;
        padding-bottom: 15px;
        font-size: calc(1.5rem + 1vw) !important;
    }
    
    h2 {
        color: #2c3e50 !important;
        margin-bottom: 15px;
        font-size: calc(1.2rem + 0.5vw) !important;
    }
    
    h5 {
        color: #2c3e50 !important;
        font-size: calc(0.9rem + 0.3vw) !important;
    }
    
    /* Radio button improvements */
    .stRadio > label {
        color: #2c3e50 !important;
        background-color: #f0f2f6;
        padding: 8px;
        border-radius: 5px;
        margin: 3px 0;
        font-size: calc(0.8rem + 0.2vw) !important;
    }
    
    /* Prediction box */
    .prediction-box {
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
        text-align: center;
        background-color: #e3f2fd !important;
    }
    
    /* Mobile-specific adjustments */
    @media (max-width: 768px) {
        .main {
            padding: 5px;
        }
        
        .stForm {
            padding: 10px;
        }
        
        .stRadio > label {
            padding: 5px;
            margin: 2px 0;
        }
        
        /* Ensure text is visible on mobile */
        p, label, .stRadio label {
            color: #2c3e50 !important;
            font-size: 0.9rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Constants
Category_mapping = {
    6: 'Database Administrator', 8: 'Hardware Engineer',
    2: 'Application Support Engineer', 5: 'Cyber Security Specialist',
    11: 'Networking Engineer', 13: 'Software Developer',
    1: 'API Specialist', 12: 'Project Manager',
    10: 'Information Security Specialist', 15: 'Technical Writer',
    0: 'AI ML Specialist', 14: 'Software tester',
    3: 'Business Analyst', 4: 'Customer Service Executive',
    9: 'Helpdesk Engineer', 7: 'Graphics Designer'
}

questions =[
"What is your level of expertise in database design, SQL, and data management principles?",
"How proficient are you in understanding CPU architecture, memory systems, and hardware components?",
"Rate your experience with implementing and managing distributed systems and parallel processing.",
"How skilled are you in network protocols, configuration, and troubleshooting?",
"Rate your ability to conduct digital investigations and recover electronic evidence.",
"What is your proficiency level in implementing cybersecurity measures and threat detection?",
"How experienced are you in developing and deploying software applications?",
"Rate your proficiency in writing efficient code across multiple programming languages.",
"How experienced are you in leading technical projects and managing development teams?",
"Rate your ability to explain complex technical concepts to diverse audiences.",
"What is your skill level in developing and implementing machine learning models?",
"How proficient are you in software design patterns and development methodologies?",
"Rate your expertise in statistical analysis and data visualization techniques.",
"How skilled are you in identifying and resolving complex technical issues?",
"What is your proficiency level in creating professional digital designs and graphics?"
]
options = ["Not Interested", "Poor", "Beginner", "Average", "Intermediate", "Excellent", "Professional"]



def reset_form():
    for i in range(len(questions)):
        if f"question_{i}" in st.session_state:
            del st.session_state[f"question_{i}"]
            
            
def load_and_train_model():
    """Load data and train the model"""
    training_df = pd.read_csv('CleanedData.csv')
    training_df.dropna(inplace=True)
    
    X = training_df.drop('Role', axis=1)
    y = training_df['Role']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    stacking_classifier = GaussianNB()
    
    stacking_classifier.fit(X_train_scaled, y_train)
    return stacking_classifier, scaler

def mapping(answer):
    """Map questionnaire responses to numerical values"""
    if answer == "Not Interested":
        return 0
    elif answer == "Poor":
        return 1
    elif answer == "Beginner":
        return 2
    elif answer == "Average":
        return 3
    elif answer == "Intermediate":
        return 3
    elif answer == "Excellent":
        return 4
    elif answer == "Professional":
        return 5
    return 0

def main():
    st.markdown("<h1>🎯 Tech Career Path Predictor</h1>", unsafe_allow_html=True)
    
    # Introduction
    col1, col2, col3 = st.columns([1,2,1])
    with col2:  
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px; margin-bottom: 30px'>
            <h2>Welcome to Your Career Assessment!</h2>
            <p>This tool will help predict your ideal tech role based on your skills and interests.
            Please rate your proficiency in various technical areas below.</p>
        </div>
        """, unsafe_allow_html=True)

    # Load model and scaler if not in session state
    if 'model' not in st.session_state:
        st.session_state.model, st.session_state.scaler = load_and_train_model()
    
    # Create form
    with st.form("skill_assessment"):
        st.markdown("<h2>Skills Assessment Form</h2>", unsafe_allow_html=True)
        
        # For mobile, use a single column instead of two
        if st.session_state.get('mobile_view', False):
            responses = {}
            for i, question in enumerate(questions):
                st.markdown(f"##### {question}")
                response = st.radio(
                    "",
                    options,
                    key=f"question_{i}",
                    horizontal=True
                )
                responses[question] = response
        else:
            # Desktop view with two columns
            col1, col2 = st.columns(2)
            responses = {}
            half = len(questions) // 2
            for i, question in enumerate(questions):
                with col1 if i < half else col2:
                    st.markdown(f"##### {question}")
                    response = st.radio(
                        "",
                        options,
                        key=f"question_{i}",
                        horizontal=True
                    )
                    responses[question] = response

        # Submit button styling
        _, col2, _ = st.columns([1,2,1])
        with col2:
            submitted = st.form_submit_button(
                "Predict My Career Path 🚀",
                use_container_width=True,
            )
        
        if submitted:
            answer_list = [mapping(responses[q]) for q in questions]
            scaled_features = [answer_list]
            prediction = st.session_state.model.predict(scaled_features)
            predicted_role = Category_mapping.get(prediction[0], "Unknown Role")
            
            # Display prediction
            st.markdown(f"""
                <div class='prediction-box' style='background-color: #e3f2fd;'>
                    <h2>Your Predicted Career Path</h2>
                    <h3 style='color: #1976d2;'>🎉 {predicted_role}</h3>
                </div>
            """, unsafe_allow_html=True)
            
            # Technical details in an expander
            with st.expander("View Technical Details 🔍"):
                st.markdown("### Feature Vector")
                st.json(dict(zip(questions, answer_list)))
                st.markdown("### Prediction Details")
                st.write(f"Prediction Value: {prediction[0]}")

    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 20px; margin-top: 50px; color: #666;'>
            <p>Built with ❤️ using Streamlit and Machine Learning</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
