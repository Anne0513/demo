import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Demo App - Home",
    page_icon="🏠",
    layout="wide"
)

# Main title
st.title("🌍 Demo Dashboard")

# Welcome text
st.markdown("""
## Welcome to the Demo Dashboard!

This application provides two main features:

### 🌍 World Cities Explorer
Explore and visualize data about cities around the world. You can filter cities by 
population, capital status, and country to gain insights into global urbanization patterns.

**Features:**
- 📊 Interactive population filtering
- 🏛️ Capital city selection
- 🌏 Map visualization
- 📈 Population analysis charts
- 📋 Detailed city information

### 🚢 Titanic Survival Prediction
Use machine learning to predict survival probability on the Titanic based on passenger characteristics.

**Features:**
- 🎯 ML-based survival prediction
- 📊 Interactive input widgets
- 📈 Probability visualization
- 📋 Feature explanation

Choose an option below to get started!
""")

# Add some spacing
st.markdown("---")

# Navigation section
st.subheader("🚀 Get Started")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Create prominent buttons to navigate to different pages
    if st.button("📍 Explore World Cities", type="primary", use_container_width=True):
        st.switch_page("pages/app.py")
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚢 Titanic Prediction", type="secondary", use_container_width=True):
        st.switch_page("pages/titanic_prediction.py")

# Add footer information
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with Streamlit 🎈 | Explore cities data interactively</p>
</div>
""", unsafe_allow_html=True)