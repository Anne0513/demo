import streamlit as st
import joblib
import numpy as np
import os

# Configure the page
st.set_page_config(
    page_title="Titanic Prediction",
    page_icon="🚢",
    layout="wide"
)

st.title('🚢 Titanic Survival Prediction')

# Load the trained model
@st.cache_resource
def load_model():
    """Load the trained Titanic survival prediction model."""
    try:
        # Get the absolute path to the model file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        model_path = os.path.join(parent_dir, 'titanic_model.pkl')
        
        # Load model using joblib (handles sklearn models better)
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load the model
model = load_model()

if model is not None:
    st.success("Model loaded successfully!")
    
    # Create input widgets for user features
    st.subheader("Enter Passenger Information:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Passenger Class (1, 2, 3)
        pclass = st.selectbox(
            "Passenger Class:",
            options=[1, 2, 3],
            index=2,  # Default to 3rd class
            help="Ship class: 1 = First Class, 2 = Second Class, 3 = Third Class"
        )
        
        # Age
        age = st.number_input(
            "Age:",
            min_value=0.0,
            max_value=100.0,
            value=30.0,
            step=1.0,
            help="Age of the passenger in years"
        )
    
    with col2:
        # Sex (male/female)
        sex_option = st.selectbox(
            "Sex:",
            options=["female", "male"],
            index=0,  # Default to female
            help="Gender of the passenger"
        )
        
        # Fare
        fare = st.number_input(
            "Fare:",
            min_value=0.0,
            max_value=1000.0,
            value=32.0,
            step=0.1,
            help="Ticket fare in pounds"
        )
    
    # Encode the inputs
    # Sex encoding: male=1, female=0 (as expected by the model)
    sex_encoded = 1 if sex_option == "male" else 0
    
    # Create input array for prediction
    input_features = np.array([[pclass, sex_encoded, age, fare]])
    
    # Display the encoded inputs for transparency
    st.subheader("Encoded Input Features:")
    feature_df = {
        "Feature": ["Passenger Class", "Sex (0=female, 1=male)", "Age", "Fare"],
        "Value": [pclass, sex_encoded, age, fare]
    }
    st.table(feature_df)
    
    # Make prediction when button is clicked
    if st.button("Predict Survival Probability", type="primary"):
        try:
            # Use model's predict_proba method to get survival probability
            probabilities = model.predict_proba(input_features)
            
            # probabilities[0][0] = probability of not surviving (class 0)
            # probabilities[0][1] = probability of surviving (class 1)
            survival_prob = probabilities[0][1]
            death_prob = probabilities[0][0]
            
            # Display results
            st.subheader("Prediction Results:")
            
            # Create columns for better layout
            result_col1, result_col2 = st.columns(2)
            
            with result_col1:
                # Survival probability
                if survival_prob > 0.5:
                    st.success(f"**Likely to Survive** 🎉")
                else:
                    st.error(f"**Unlikely to Survive** 😔")
                    
                st.metric(
                    label="Survival Probability",
                    value=f"{survival_prob:.2%}",
                    delta=None
                )
            
            with result_col2:
                st.metric(
                    label="Death Probability", 
                    value=f"{death_prob:.2%}",
                    delta=None
                )
            
            # Additional detailed output using st.write
            st.write("---")
            st.write("**Detailed Prediction Results:**")
            st.write(f"• Probability of **survival**: {survival_prob:.4f} ({survival_prob:.2%})")
            st.write(f"• Probability of **death**: {death_prob:.4f} ({death_prob:.2%})")
            
            # Add some context
            st.info("""
            **Note:** This prediction is based on historical Titanic passenger data and 
            considers factors like passenger class, gender, age, and fare paid. 
            The model uses these features to estimate survival probability.
            """)
            
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    
    # Add some information about the features
    st.subheader("About the Features:")
    st.write("""
    - **Passenger Class**: Ship class (1st = upper, 2nd = middle, 3rd = lower class)
    - **Sex**: Gender of the passenger (historically, women and children were prioritized)
    - **Age**: Age in years (children had higher survival rates)
    - **Fare**: Ticket price (higher fares often meant better cabin locations and access to lifeboats)
    """)
    
else:
    st.error("Unable to load the Titanic prediction model. Please check if 'titanic_model.pkl' exists in the repository root.")