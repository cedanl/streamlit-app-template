# Home.py
import streamlit as st

title = "Home"
icon = ":material/home:"

st.markdown(
    """
    # Welcome to the CEDA Streamlit App Template!
    
    This template provides a structured foundation for building interactive data science 
    and machine learning applications for CEDA members.
    
    **👈 Explore the modules from the sidebar** to see example implementations
    and discover what's possible with this template!
    
    ## 🏗️ How to Use This Template
    
    ### Adding New Pages
    - Create new Python files in the `frontend/` directory
    - Add your page configuration to `src/main.py` in the page configuration section
    - Your new page will be accessible from the sidebar
    - **Use `st.session_state` to maintain data across page interactions**
    
    ### Backend Functions
    - Create reusable functions in the `backend/` directory
    - Import and call these functions from your frontend pages
    - Keep your business logic separated from your UI components
    - **Optimize performance with `@st.cache_data` for data loading functions**
    - **Use `@st.cache_resource` for database connections and ML models**
    
    ## 🚀 Get Started
    
    1. **Check out the Examples** - Browse the modules section to see working implementations
    2. **Create Your First Page** - Add a new `.py` file to the frontend directory
    3. **Build Backend Functions** - Create supporting functions in the backend directory
    4. **Configure Navigation** - Update the page configuration in `main.py`
    5. **Implement State Management** - Use `st.session_state` for user data persistence
    
    ## 📚 Resources
    
    - [Streamlit Documentation](https://docs.streamlit.io) - Official Streamlit guides
    - [Streamlit API Reference](https://docs.streamlit.io/develop/api-reference) - Complete Component & API documentation
    - [Caching and State Management](https://docs.streamlit.io/develop/api-reference/caching-and-state) - Essential for performance
    - [Streamlit Community](https://discuss.streamlit.io) - Get help and share ideas
    
    ## 💡 Template Features
    
    - **Modular Architecture** - Clean separation between frontend and backend
    - **Easy Page Management** - Simple configuration-based page routing
    - **Reusable Components** - Shared backend functions across pages
    - **Professional Structure** - Industry-standard project organization
    - **Performance Optimized** - Built-in caching strategies for data and resources
    - **State Management** - Persistent user interactions across sessions
    
    ## 🔧 Key Streamlit Features to Leverage
    
    ### Caching for Performance
    ```python
    @st.cache_data
    def load_dataset(file_path):
        # Cache expensive data loading operations
        return pd.read_csv(file_path)
    
    @st.cache_resource
    def initialize_model():
        # Cache resource-heavy objects like ML models
        return joblib.load('model.pkl')
    ```
    
    ### Session State for Interactivity
    ```python
    # Initialize session state
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    
    # Store user inputs persistently
    st.session_state.user_data['name'] = st.text_input("Name")
    ```
    
    ### Dynamic Page Updates
    ```python
    # Trigger page rerun when data changes
    if st.button("Update Results"):
        st.rerun()
    
    # Stop execution conditionally
    if not user_authenticated:
        st.stop()
    ```
    
    ## 📊 Best Practices for CEDA Apps
    
    - **Cache data loading functions** to avoid repeated file reads
    - **Use session state** to maintain user selections across interactions  
    - **Implement error handling** with `st.error()` and `st.exception()`
    - **Show progress** for long operations with `st.progress()` and `st.status()`
    - **Organize layouts** with `st.columns()`, `st.tabs()`, and `st.container()`
    - **Handle user input validation** before processing
    
    Ready to build something amazing? Start exploring the examples in the sidebar and 
    leverage Streamlit's powerful caching and state management features!
    """)