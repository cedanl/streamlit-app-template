# -----------------------------------------------------------------------------
# Organization: CEDA
# Original Authors: Ash Sewnandan, Iwan Tomer
# -----------------------------------------------------------------------------
"""
Main Entrypoint for the Streamlit App
"""
import streamlit as st

# Sidebar Configuration
LOGO_URL = "src/assets/npuls_logo.png"
st.logo(LOGO_URL)

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION - Add new sections/pages here
# -----------------------------------------------------------------------------
home_page = st.Page("frontend/Overview/Home.py", icon=":material/home:")
example_upload_page = st.Page("frontend/Files/example_Upload.py", icon=":material/folder:")
example_sales_page = st.Page("frontend/Modules/example_Sales.py", icon=":material/euro:")
example_task_page = st.Page("frontend/Modules/example_Task.py", icon=":material/note:")

# Initialize Navigation, Sections, and Pages
pg = st.navigation ( {
    "Overview": [home_page],
    "Files": [example_upload_page],
    "Modules": [example_sales_page, example_task_page]
})

# -----------------------------------------------------------------------------
# Run the app
# -----------------------------------------------------------------------------
pg.run()