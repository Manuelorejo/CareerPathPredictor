#IMPORT STATEMENTS
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC




#Page configuration
st.set_page_config(
    page_title="Skills Assessment | Tech Career Advisor",
    page_icon="🎯",
    layout="wide"
)

if st.button("← Back to Home", key="home_button"):
    st.switch_page("homepage.py")
    
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
    
    /* Question group styling */
    .question-group {
        padding: 15px;
        margin: 10px 0;
        border-bottom: 2px solid #ffffff;
    }
    
    /* Remove the line from the last question group */
    .question-group:last-child {
        border-bottom: none;
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
        margin-bottom: 5px !important;
    }
    
    /* Radio button styling */
    .stRadio {
        margin-bottom: 20px;
    }
    
    .stRadio > label {
        color: #2c3e50 !important;
        background-color: #f0f2f6;
        padding: 8px;
        border-radius: 5px;
        font-size: calc(0.8rem + 0.2vw) !important;
    }
    
    /* Mobile adjustments */
    @media (max-width: 768px) {
        .question-group {
            padding: 10px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Maps predictions from the ML model to the corresponding field of interest
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

#A list of questions to be asked on the form
questions = [
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



#A function to reset the form after each click
def reset_form():
    for i in range(len(questions)):
        if f"question_{i}" in st.session_state:
            del st.session_state[f"question_{i}"]
            

            
#A function to load the dataset, and train the model
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
    
    stacking_classifier.fit(X_train, y_train)
    return stacking_classifier, scaler

#A dataset that maps the input from the form to integers which can be passed into the model
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


#The main function which runs when the file is executed
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

    # Load model and scaler if not already in the  session state
    if 'model' not in st.session_state:
        st.session_state.model, st.session_state.scaler = load_and_train_model()
    
    # Form for getting user input
    with st.form("skill_assessment"):
       st.markdown("<h2>Skills Assessment Form</h2>", unsafe_allow_html=True)
       
       responses = {}
       for i, question in enumerate(questions):
           # Create a div for each question group
           st.markdown(f"""
               <div class="question-group">
                   <h5>{question}</h5>
               </div>
           """, unsafe_allow_html=True)
           
           #Create a radio button format with the options
           response = st.radio(
               "",
               options,
               key=f"question_{i}",
               horizontal=True
           )
           responses[question] = response

       # Creates the submit button
       _, col2, _ = st.columns([1,2,1])
       with col2:
           submitted = st.form_submit_button(
               "Predict My Career Path 🚀",
               use_container_width=True,
           )
           
    #When the submit button is pressed the answers from the form are mapped to integers and passed into the model    
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


#Main 
if __name__ == "__main__":
    main()