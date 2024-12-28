import streamlit as st

def apply_style():
    """Apply custom styling to the Streamlit app."""
    # Configure page settings
    st.set_page_config(
        page_title="Geographic Coordinates Assignment",
        page_icon="🗺️",
        layout="wide"
    )
    
    # Custom CSS styling
    st.markdown("""
        <style>
        /* Input fields styling */
        .stTextInput > div > div > input {
            background-color: #f0f2f6;
            border-radius: 5px;
            padding: 8px 12px;
            border: 1px solid #e0e0e0;
        }
        
        /* Expander header styling */
        .streamlit-expanderHeader {
            background-color: #f0f2f6;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
        }
        
        /* Code input area styling */
        .stTextArea > div > div > textarea {
            background-color: #f0f2f6;
            font-family: 'Courier New', Courier, monospace;
            padding: 12px;
            border: 1px solid #e0e0e0;
        }
        
        /* Button styling */
        .stButton > button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        
        /* Main content spacing */
        .css-1v0mbdj.etr89bj1 {
            margin-top: 2em;
            margin-bottom: 2em;
        }
        
        /* Success message styling */
        .element-container .stAlert {
            padding: 1em;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)
