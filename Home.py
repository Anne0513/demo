import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Demo App - Home",
    page_icon="🏠",
    layout="wide"
)

# Main title
st.title("🌍 World Cities Dashboard")

# Welcome text
st.markdown("""
## Welcome to the World Cities Dashboard!

This application allows you to explore and visualize data about cities around the world. 
You can filter cities by population, capital status, and country to gain insights into 
global urbanization patterns.

### Features:
- 📊 Interactive population filtering
- 🏛️ Capital city selection
- 🌏 Map visualization
- 📈 Population analysis charts
- 📋 Detailed city information

Get started by navigating to the **World Cities** page to explore the data!
""")

# Add some spacing
st.markdown("---")

# Navigation section
st.subheader("🚀 Get Started")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Create a prominent button to navigate to the app
    if st.button("📍 Explore World Cities", type="primary", use_container_width=True):
        st.switch_page("pages/app.py")

# Add footer information
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with Streamlit 🎈 | Explore cities data interactively</p>
</div>
""", unsafe_allow_html=True)