import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
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
    .main {
        padding: 20px;
    }
    .stRadio > label {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .stForm {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1f77b4;
        text-align: center;
        padding-bottom: 20px;
    }
    h2 {
        color: #2c3e50;
        margin-bottom: 20px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
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

questions = [
    "How would you rate your understanding of Database Fundamentals?",
    "How would you rate your understanding of Computer Architecture?",
    "How would you rate your understanding of Distributed Computing Systems?",
    "How would you rate your understanding of Networking",
    "How would you rate your understanding of Computer Forensics Fundamentals?",
    "How would you rate your Cybersecurity skills?",
    "How would you rate your Software Development skills?",
    "How would you rate your Programming skills?",
    "How would you rate your Project Management skills?",
    "How would you rate your Technical Communication skills?",
    "How would you rate your AI/ML skills?",
    "How would you rate your Software Engineering skills?",
    "How would you rate your Data Science skills?",
    "How would you rate your Troubleshooting skills?",
    "How would you rate your Graphics Designing skills?"
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
    
    stacking_classifier = SVC(kernel='rbf', probability=True, random_state=42, max_iter=1000)
    
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
        
        # Create two columns for questions
        col1, col2 = st.columns(2)
        responses = {}
        
        # Distribute questions between columns
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
        
        # Center the submit button
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            submitted = st.form_submit_button(
                "Predict My Career Path 🚀", 
                on_click=reset_form(),
                use_container_width=True
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
