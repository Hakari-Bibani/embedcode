from github_utils import GitHubManager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Modify the save_submission function
def save_submission(name, email, student_id, grade):
    """Save submission to both local CSV and GitHub repository."""
    try:
        # Save to GitHub
        github_manager = GitHubManager()
        github_manager.update_csv_file(name, email, student_id, grade)
        return True
    except Exception as e:
        st.error(f"Failed to save submission to GitHub: {str(e)}")
        return False

# Update the submit button section in main()
    with col2:
        if st.button("📤 Submit Assignment", use_container_width=True):
            if not name or not email:
                st.error("❌ Please fill in the required fields (Name and Email)")
            elif not code.strip():
                st.error("❌ Please paste your code before submitting")
            else:
                grade = grade_submission(code)
                if save_submission(name, email, student_id, grade):
                    st.balloons()
                    st.success(f"✅ Assignment submitted successfully! Your grade: {grade}/100")
                else:
                    st.error("Failed to save submission. Please try again or contact support.")
                    
import streamlit as st
from style import apply_style
from grade import grade_submission, calculate_distances, create_map
import pandas as pd
from streamlit_folium import folium_static
import os

def save_submission(name, email, student_id, grade):
    """Save submission details to CSV file."""
    submission = pd.DataFrame({
        'Name': [name],
        'Email': [email],
        'Student_ID': [student_id],
        'Grade': [grade],
        'Submission_Date': [pd.Timestamp.now()]
    })
    
    filepath = 'data_submission.csv'
    if os.path.exists(filepath):
        submission.to_csv(filepath, mode='a', header=False, index=False)
    else:
        submission.to_csv(filepath, index=False)

def main():
    apply_style()
    st.title("Geographic Coordinates Mapping Assignment")
    
    # Student Information Section
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name *")
        email = st.text_input("Email *")
    with col2:
        student_id = st.text_input("Student ID (Optional)")
    
    # Assignment Instructions
    with st.expander("📝 Assignment Instructions", expanded=True):
        st.markdown("""
        ### Week 1 – Mapping Coordinates and Calculating Distances
        
        **Required Points to Map:**
        - Point 1: (36.325735, 43.928414)
        - Point 2: (36.393432, 44.586781)
        - Point 3: (36.660477, 43.840174)
        
        **Expected Output:**
        1. Interactive map showing all three points
        2. Calculated distances between each pair of points
        
        **Reference Distances:**
        - Point 1 to Point 2: 59.57 km
        - Point 2 to Point 3: 73.14 km
        - Point 1 to Point 3: 37.98 km
        """)
    
    # Code Input Section
    st.markdown("### 💻 Code Submission")
    code = st.text_area("Paste your Google Colab code here:", height=300)
    
    col1, col2 = st.columns(2)
    
    # Run Code Button
    with col1:
        if st.button("▶️ Run Code", use_container_width=True):
            if code.strip():
                try:
                    points = [
                        (36.325735, 43.928414),
                        (36.393432, 44.586781),
                        (36.660477, 43.840174)
                    ]
                    
                    # Display map
                    m = create_map(points)
                    folium_static(m)
                    
                    # Calculate and display distances
                    dist_1_2, dist_2_3, dist_1_3 = calculate_distances(points)
                    st.success("✅ Distances calculated successfully!")
                    st.write(f"Distance Point 1 to Point 2: {dist_1_2:.2f} km")
                    st.write(f"Distance Point 2 to Point 3: {dist_2_3:.2f} km")
                    st.write(f"Distance Point 1 to Point 3: {dist_1_3:.2f} km")
                
                except Exception as e:
                    st.error(f"❌ Error in code execution: {str(e)}")
            else:
                st.warning("⚠️ Please paste your code before running")
    
    # Submit Button
    with col2:
        if st.button("📤 Submit Assignment", use_container_width=True):
            if not name or not email:
                st.error("❌ Please fill in the required fields (Name and Email)")
            elif not code.strip():
                st.error("❌ Please paste your code before submitting")
            else:
                grade = grade_submission(code)
                save_submission(name, email, student_id, grade)
                st.balloons()
                st.success(f"✅ Assignment submitted successfully! Your grade: {grade}/100")

if __name__ == "__main__":
    main()
