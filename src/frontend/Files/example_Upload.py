import streamlit as st

# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------
title = "File Upload"
icon = ":material/file_upload:"

# ---------------------------------------
# PAGE ELEMENTS
# ---------------------------------------
def save_uploaded_file(uploaded_file):
    """Save uploaded file to session state
    
    NOTE: You can move this file handler function to a separate file 
    (frontend/utils or backend/utils - depending if it helps the UI or 
    does a backend transformation needed for the project) and import it here
    """
    if uploaded_file is not None:
        st.session_state['uploaded_file'] = uploaded_file
        st.session_state['file_name'] = uploaded_file.name
        st.session_state['file_size'] = uploaded_file.size

# File upload section
st.header("📁 Upload File")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    save_uploaded_file(uploaded_file)
    st.success(f"File '{uploaded_file.name}' saved to session!")

# File inspection section  
st.header("📋 File Inspector")
if 'uploaded_file' in st.session_state:
    st.write(f"**File Name:** {st.session_state['file_name']}")
    st.write(f"**File Size:** {st.session_state['file_size']} bytes")
    st.dataframe(st.session_state['uploaded_file'])
    
    # Show preview for text files
    if st.session_state['uploaded_file'].type == "text/plain":
        content = str(st.session_state['uploaded_file'].read(), "utf-8")
        st.text_area("Preview:", content, height=200)
else:
    st.info("No file uploaded yet")