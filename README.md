<div align="center">
  <h1>CEDA Streamlit App Template</h1>

  <p>🚀 A simple template to quickly build interactive data science applications!</p>

  <p>
    <a href="#"><img src="https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white" alt="Windows"></a>
    <a href="#"><img src="https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=F0F0F0" alt="macOS"></a>
    <a href="#"><img src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black" alt="Linux"></a>
    <img src="https://badgen.net/github/last-commit/cedanl/streamlit-app-template" alt="GitHub Last Commit">
    <img src="https://img.shields.io/github/license/cedanl/streamlit-app-template" alt="GitHub License">
  </p>
</div>

## 📋 Overview
> [!NOTE]
> **Quick Start**: 1) [![Use Template](https://img.shields.io/badge/Use-Template-green)](https://github.com/cedanl/streamlit-app-template/generate) → 2) Clone locally → 3) Install [![uv Badge](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=fff&style=flat)](https://docs.astral.sh/uv/) → 4) Run `uv run streamlit run src/main.py`

The CEDA Streamlit App Template helps researchers and data scientists quickly build interactive web applications for data analysis and visualization. Perfect for creating:

- Data analysis dashboards
- Interactive visualizations
- Machine learning demos
- Research presentation tools

## ✨ Features
- [x] **Ready-to-Use Structure**: Pre-organized folders and files for instant development
- [x] **User-Friendly Interface**: Streamlit-based UI requiring no web development knowledge
- [x] **Easy Page Creation**: Add new pages with just a few lines of code
- [x] **Professional Layout**: Clean, organized project structure
- [x] **`uv` Powered Setup**: One-click installation that handles Python and dependencies automatically

<br>

## 🔧 First Time Setup
> [!WARNING]
> Do not skip these steps if this is your first time using this template. It will not work without them.

> [!TIP]
> Save the repository in a Projects/CEDA folder on your main drive for quick access.

### 1. Get the Template

#### Option A: Use Template (For CEDA Members)
1. Click the green **"Use this template"** button on GitHub
2. Name your new app repository
3. Choose Public or Private
4. Click **"Create repository"**

#### Option B: Download ZIP
[![Download Template](https://img.shields.io/badge/Download-Template-green)](https://github.com/cedanl/streamlit-app-template/archive/refs/heads/main.zip)

After downloading, extract the ZIP file and navigate into the folder.

### 2. Install [![uv Badge](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=fff&style=flat)](https://docs.astral.sh/uv/)

#### MacOS & Linux (Terminal)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows (Powershell or [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?hl=nl-NL&gl=NL))
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Close and reopen your terminal after installation.

#### Verify installation
```bash
uv self update
```

<br>

## 🚀 Running Your App

Ready to see your app come to life? It's just one command away! ✨

### First, get to the right spot:

Open a terminal in your app folder - it's super easy!
- **Windows**: `Shift + Right-click` in folder → `Open in Windows Terminal` 
- **Mac**: `Right-click` folder → `New Terminal at Folder`
- **VS Code**: Just click `Terminal` → `New Terminal`

Or navigate there:
```bash
cd path/to/your-app-folder
```

### Then, launch with a single command:

```bash
uv run streamlit run src/main.py
```

That's it! Your app will automatically open in your browser. If you've completed the setup correctly, this is the **only command** you'll need going forward. 🎉

<br>

## 🎯 Building Your First App

### Adding New Pages
1. Create a new `.py` file in the `src/frontend/` folder
2. Add your page to the navigation in `src/main.py`
3. Your page appears automatically in the sidebar!

### Example Page Structure
```python
import streamlit as st

def show():
    st.title("My New Page")
    st.write("Hello, world!")
    
    # Add your content here
    user_input = st.text_input("Enter something:")
    if user_input:
        st.success(f"You entered: {user_input}")
```

### What You Can Build
- **Data Upload & Analysis**: Let users upload CSV files and see instant insights
- **Interactive Charts**: Build dynamic visualizations that respond to user input  
- **Machine Learning Demos**: Create interfaces for ML models and predictions
- **Research Dashboards**: Display your research findings in an interactive format

<br>

## 🛠️ Built With
[![uv Badge](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=fff&style=flat)](https://docs.astral.sh/uv/)
[![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=flat)](https://streamlit.io/)
[![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)](https://www.python.org/)

## 🤲 Support
If you find this template helpful, please consider:
- ⭐ Starring the repo
- 🐛 Reporting bugs
- 💡 Suggesting improvements
- 💻 Contributing code

Need help? Feel free to [open an issue](https://github.com/cedanl/streamlit-app-template/issues) or contact us at a.sewnandan@hhs.nl

## 🙏 Contributors
Thank you to all the [people](https://github.com/cedanl/streamlit-app-template/graphs/contributors) who have contributed to this template.

[![](https://github.com/asewnandan.png?size=50)](https://github.com/asewnandan)
[![](https://github.com/tin900.png?size=50)](https://github.com/tin900)

## 🚦 License
![GitHub License](https://img.shields.io/github/license/cedanl/streamlit-app-template)
