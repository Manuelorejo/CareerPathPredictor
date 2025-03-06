#IMPORT STATEMENTS
import streamlit as st
import joblib

model = joblib.load('EnsembleModel.sav')

#Page configuration
st.set_page_config(
    page_title="Skills Assessment |  Career Advisor",
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
    
    /* Error message styling */
    .error-message {
        color: #d9534f;
        background-color: #f9e2e2;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
        margin-bottom: 20px;
        text-align: center;
        font-weight: bold;
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

# Dictionary mapping skill areas to job roles for explanation purposes
skill_to_job_mapping = {
    "database design, SQL, and data management": ["Database Administrator", "Business Analyst"],
    "CPU architecture, memory systems, and hardware components": ["Hardware Engineer", "Networking Engineer"],
    "distributed systems and parallel processing": ["AI ML Specialist", "Software Developer"],
    "network protocols, configuration, and troubleshooting": ["Networking Engineer", "Cyber Security Specialist"],
    "digital investigations and recover electronic evidence": ["Cyber Security Specialist", "Information Security Specialist"],
    "cybersecurity measures and threat detection": ["Cyber Security Specialist", "Information Security Specialist"],
    "developing and deploying software applications": ["Software Developer", "API Specialist"],
    "writing efficient code across multiple programming languages": ["Software Developer", "AI ML Specialist"],
    "leading technical projects and managing development teams": ["Project Manager", "Business Analyst"],
    "explain complex technical concepts to diverse audiences": ["Technical Writer", "Business Analyst"],
    "developing and implementing machine learning models": ["AI ML Specialist", "Software Developer"],
    "software design patterns and development methodologies": ["Software Developer", "Project Manager"],
    "statistical analysis and data visualization techniques": ["Business Analyst", "AI ML Specialist"],
    "identifying and resolving complex technical issues": ["Application Support Engineer", "Helpdesk Engineer"],
    "creating professional digital designs and graphics": ["Graphics Designer", "Technical Writer"]
}

# Job descriptions for each role
job_descriptions = {
    'Database Administrator': "Database Administrators organize, store, and protect data using specialized software. They ensure databases operate efficiently, maintain data integrity, back up systems, and implement security measures. They also optimize database performance, troubleshoot issues, and ensure data accessibility while maintaining security protocols.",
    
    'Hardware Engineer': "Hardware Engineers design, develop, and test computer systems and components. They create specifications for computer equipment, design hardware components like circuit boards, processors, and memory devices, and test prototypes. They also oversee manufacturing processes and collaborate with software developers to ensure compatibility.",
    
    'Application Support Engineer': "Application Support Engineers maintain and troubleshoot software applications. They respond to user issues, implement software updates, perform regular maintenance, and collaborate with development teams to improve application performance. They also document solutions, train users, and contribute to continuous improvement initiatives.",
    
    'Cyber Security Specialist': "Cyber Security Specialists protect computer systems and networks from threats. They implement security measures, monitor for breaches, conduct risk assessments, and develop security protocols. They also stay updated on emerging threats, respond to security incidents, and ensure compliance with security policies and regulations.",
    
    'Networking Engineer': "Networking Engineers design, implement, and manage computer networks. They configure networking hardware like routers and switches, troubleshoot connectivity issues, implement security protocols, and optimize network performance. They also plan network upgrades, maintain documentation, and ensure network reliability and security.",
    
    'Software Developer': "Software Developers design, code, and test software applications. They analyze user requirements, write clean and efficient code, debug programs, and implement software updates. They also collaborate with other developers, document code, and stay current with programming languages and development methodologies.",
    
    'API Specialist': "API Specialists develop and maintain Application Programming Interfaces that allow different software systems to communicate. They design API architectures, implement integration solutions, ensure data security during transfers, and document API functionalities. They also troubleshoot integration issues and optimize API performance.",
    
    'Project Manager': "Project Managers plan, execute, and close technology projects. They define project scope, create timelines, allocate resources, and coordinate team members. They also track progress, manage risks, communicate with stakeholders, and ensure project deliverables meet requirements within time and budget constraints.",
    
    'Information Security Specialist': "Information Security Specialists establish and enforce policies to protect digital information. They assess security risks, implement protection systems, monitor for security breaches, and respond to incidents. They also educate users about security practices, stay updated on emerging threats, and ensure regulatory compliance.",
    
    'Technical Writer': "Technical Writers create clear documentation for technology products and services. They develop user manuals, online help systems, tutorials, and reference guides. They also collaborate with subject matter experts, organize information logically, adhere to documentation standards, and ensure materials are accessible to the target audience.",
    
    'AI ML Specialist': "AI/ML Specialists develop algorithms and systems that enable machines to learn from data and make decisions. They design and implement machine learning models, prepare and analyze data sets, train algorithms, and evaluate model performance. They also collaborate with teams to integrate AI solutions into applications and continuously improve model accuracy.",
    
    'Software tester': "Software Testers evaluate applications to ensure quality and identify defects. They design and execute test cases, perform various testing types (functional, regression, performance), document bugs, and verify fixes. They also develop automated test scripts, participate in quality assurance processes, and help ensure software meets requirements.",
    
    'Business Analyst': "Business Analysts bridge the gap between IT and business needs. They gather and document requirements, analyze business processes, recommend solutions, and communicate between stakeholders and development teams. They also create functional specifications, validate deliverables against requirements, and support system implementation.",
    
    'Customer Service Executive': "Customer Service Executives in tech support users with product issues and inquiries. They troubleshoot technical problems, provide guidance on product features, manage customer accounts, and escalate complex issues. They also gather customer feedback, maintain service records, and contribute to improving customer experience.",
    
    'Helpdesk Engineer': "Helpdesk Engineers provide technical support to resolve user issues. They diagnose and troubleshoot hardware and software problems, perform basic repairs, set up user accounts, and provide technical guidance. They also document solutions, track support tickets, and identify recurring issues for permanent resolution.",
    
    'Graphics Designer': "Graphics Designers in tech create visual elements for digital products and interfaces. They design user interfaces, create illustrations and icons, develop brand visual identities, and produce graphics for websites and applications. They also collaborate with product teams, incorporate user feedback, and ensure designs enhance user experience."
}

#A function to reset the form after each click
def reset_form():
    for i in range(len(questions)):
        if f"question_{i}" in st.session_state:
            del st.session_state[f"question_{i}"]

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

# Function to validate responses
def validate_responses(responses):
    # Check if all responses are "Not Interested"
    if all(response == "Not Interested" for response in responses.values()):
        return False, "Please express interest in at least one skill area to get accurate career recommendations."
    return True, ""

# Function to generate explanation for prediction
def generate_explanation(responses):
    # Find highest-rated skills (excluding "Not Interested")
    numeric_responses = {q: mapping(r) for q, r in responses.items()}
    # Filter out "Not Interested" responses (which map to 0)
    interested_skills = {q: score for q, score in numeric_responses.items() if score > 0}
    
    # If no interested skills, provide a generic explanation
    if not interested_skills:
        return "Based on your overall pattern of responses, our model has identified this career path as potentially suitable. Consider exploring this field to see if it aligns with your interests and goals."
    
    # Sort by score
    sorted_skills = sorted(interested_skills.items(), key=lambda x: x[1], reverse=True)
    # Get top 3 or all if less than 3
    top_skills = sorted_skills[:min(3, len(sorted_skills))]
    
    # Generate explanation
    explanation = "Based on your assessment, you demonstrated interest or proficiency in:"
    
    for question, score in top_skills:
        # Extract key skill area from the question
        for skill_area, roles in skill_to_job_mapping.items():
            if skill_area in question.lower():
                # Convert score back to option text (Poor, Beginner, etc.)
                rating = options[score]  # This will get the corresponding skill level
                explanation += f"\n• {skill_area.title()} (rated as '{rating}')"
                break
    
    explanation += "\n\nThese skills are particularly valuable for a " + st.session_state.predicted_role + "."
    return explanation

# Function to save user responses for the results page
def save_user_responses(responses):
    # Convert to numeric values for prediction
    answer_list = [mapping(responses[q]) for q in questions]
    
    # Store in session state for the results page
    st.session_state.user_responses = responses
    st.session_state.numeric_responses = answer_list
    
    # Get prediction using the pre-loaded model
    prediction = model.predict([answer_list])
    st.session_state.prediction = prediction[0]
    st.session_state.predicted_role = Category_mapping.get(prediction[0], "Unknown Role")
    
    # Generate explanation for the prediction
    st.session_state.explanation = generate_explanation(responses)

#The main function which runs when the file is executed
def main():
    # Check if we're on the results page
    if 'show_results' in st.session_state and st.session_state.show_results:
        show_results_page()
    else:
        show_assessment_page()

def show_assessment_page():
    st.markdown("<h1>� Career Path Predictor</h1>", unsafe_allow_html=True)
    
    # Introduction
    col1, col2, col3 = st.columns([1,2,1])
    with col2:  
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px; margin-bottom: 30px'>
            <h2>Welcome to Your Career Assessment!</h2>
            <p>This tool will help predict your ideal role based on your skills and interests.
            Please rate your proficiency in various technical areas below.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Initialize error message in session state if not present
    if 'error_message' not in st.session_state:
        st.session_state.error_message = ""
    
    # Display error message if it exists
    if st.session_state.error_message:
        st.markdown(f"""
            <div class="error-message">
                {st.session_state.error_message}
            </div>
        """, unsafe_allow_html=True)
    
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
               "See My Results 🚀",
               use_container_width=True,
           )
           
    # When the submit button is pressed, validate responses before proceeding
    if submitted:
        valid, error_message = validate_responses(responses)
        if valid:
            # Clear any previous error message
            st.session_state.error_message = ""
            save_user_responses(responses)
            st.session_state.show_results = True
            st.rerun()
        else:
            # Set error message and don't proceed to results page
            st.session_state.error_message = error_message
            st.rerun()

    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 20px; margin-top: 50px; color: #666;'>
            <p>Built with ❤️ using Streamlit and Machine Learning</p>
        </div>
    """, unsafe_allow_html=True)

def show_results_page():
    st.markdown("<h1>🎯 Your Career Path Results</h1>", unsafe_allow_html=True)
    
    # Display prediction with some animation
    st.markdown(f"""
        <div style='background-color: #e3f2fd; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px;'>
            <h2>Your Predicted Career Path</h2>
            <h3 style='color: #1976d2; font-size: 2.5rem; margin: 20px 0;'>🎉 {st.session_state.predicted_role}</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Job description
    st.markdown("""
        <h3 style='margin-top: 30px; margin-bottom: 15px;'>What Does This Role Involve?</h3>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <p style='font-size: 1.1rem;'>{job_descriptions.get(st.session_state.predicted_role, "This role involves a unique combination of technical skills.")}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Explanation of why this role was chosen
    st.markdown("""
        <h3 style='margin-top: 30px; margin-bottom: 15px;'>Why This Role Matches You</h3>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <p style='font-size: 1.1rem; white-space: pre-line;'>{st.session_state.explanation}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Career outlook
    st.markdown("""
        <h3 style='margin-top: 30px; margin-bottom: 15px;'>Career Outlook</h3>
    """, unsafe_allow_html=True)
    
    career_outlooks = {
        'Database Administrator': "The demand for Database Administrators remains strong as organizations continue to collect and leverage increasing amounts of data. Growth opportunities exist in cloud database management, data security, and big data environments.",
        'Hardware Engineer': "Hardware Engineering offers stable career prospects with growth in specialized areas like IoT devices, embedded systems, and custom computing solutions for AI applications.",
        'Application Support Engineer': "This role continues to see steady demand as businesses rely on complex software applications. Career advancement opportunities include moving into systems architecture or specialized application management.",
        'Cyber Security Specialist': "Cybersecurity remains one of the fastest-growing technology fields due to increasing threats and regulatory requirements. Specialists with hands-on experience are in high demand across all industries.",
        'Networking Engineer': "With the expansion of cloud computing and remote work infrastructures, skilled Networking Engineers remain essential. Growth areas include cloud networking, software-defined networking, and wireless technologies.",
        'Software Developer': "Software development continues to be a cornerstone of the tech industry with strong job prospects. Specialization in areas like cloud development, mobile applications, or AI integration offers additional growth opportunities.",
        'API Specialist': "As systems become increasingly interconnected, API development and management skills are in growing demand. This role offers career paths into software architecture or specialized integration services.",
        'Project Manager': "Technical Project Managers remain in demand as organizations need skilled professionals to oversee complex technology implementations. Certification in agile methodologies or specific industries can enhance career prospects.",
        'Information Security Specialist': "With increasing focus on data protection and privacy regulations, Information Security Specialists enjoy excellent job prospects and competitive compensation.",
        'Technical Writer': "As technology becomes more complex, clear documentation becomes increasingly valuable. Growth areas include API documentation, developer experience, and user experience writing.",
        'AI ML Specialist': "This is one of the fastest-growing fields in technology, with strong demand across industries implementing AI solutions. Continuing education is important as the field evolves rapidly.",
        'Software tester': "Quality Assurance professionals remain essential in software development. Career growth opportunities include test automation, security testing, and quality management leadership.",
        'Business Analyst': "Business Analysts with technical expertise are valuable bridges between business needs and technology solutions. Growth paths include product management or specialized industry analysis.",
        'Customer Service Executive': "Technical customer service roles provide stable employment with advancement opportunities in customer success management or specialized product support.",
        'Helpdesk Engineer': "Entry-level helpdesk positions offer excellent opportunities to gain experience across multiple technologies, with clear advancement paths to specialized technical roles.",
        'Graphics Designer': "Technical design specialists focusing on UI/UX for digital products remain in demand. Career growth opportunities include moving into UX research, product design leadership, or specialized interface design."
    }
    
    st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <p style='font-size: 1.1rem;'>{career_outlooks.get(st.session_state.predicted_role, "This field offers strong growth opportunities for professionals with your skill set.")}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Technical details in an expander
    with st.expander("View Assessment Details 🔍"):
        st.markdown("### Your Responses")
        for question, response in st.session_state.user_responses.items():
            st.markdown(f"**Q:** {question}")
            st.markdown(f"**A:** {response}")
            st.markdown("---")
        
        st.markdown("### Technical Details")
        st.write(f"Prediction Value: {st.session_state.prediction}")
        st.write(f"Role Mapping: {st.session_state.prediction} → {st.session_state.predicted_role}")
    
    # Next steps suggestions
    st.markdown("""
        <h3 style='margin-top: 30px; margin-bottom: 15px;'>Recommended Next Steps</h3>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <ul style='font-size: 1.1rem;'>
                <li><strong>Research the role:</strong> Learn more about what {st.session_state.predicted_role}s do day-to-day</li>
                <li><strong>Connect with professionals:</strong> Find people working in this field on LinkedIn or professional communities</li>
                <li><strong>Identify skill gaps:</strong> Look for specific technologies or certifications that could strengthen your profile</li>
                <li><strong>Look for entry points:</strong> Explore internships, junior positions, or related roles that could lead to this career</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("← Back to Assessment", use_container_width=True):
            st.session_state.show_results = False
            # Clear previous error message
            st.session_state.error_message = ""
            # Clear previous responses
            reset_form()
            st.rerun()
    
    with col2:
        if st.button("🏠 Return to Home", use_container_width=True):
            st.session_state.show_results = False
            # Clear previous error message
            st.session_state.error_message = ""
            # Clear previous responses 
            reset_form()
            st.switch_page("homepage.py")
    
    with col3:
        if st.button("📋 Take New Assessment", use_container_width=True):
            st.session_state.show_results = False
            # Clear previous error message
            st.session_state.error_message = ""
            # Clear previous responses
            reset_form()
            st.rerun()
    
    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 20px; margin-top: 50px; color: #666;'>
            <p>2025 Career Advisor</p>
        </div>
    """, unsafe_allow_html=True)

#Main 
if __name__ == "__main__":
    main()
