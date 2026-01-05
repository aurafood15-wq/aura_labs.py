import streamlit as st

# AURA AI Labs - Quantum Research Interface
st.set_page_config(page_title="AURA AI Labs", page_icon="🔬", layout="wide")

# Styling for a professional Lab Vibe
st.markdown("""
    <style>
    .stApp { background-color: #050a14; color: #e0e0e0; }
    h1 { color: #00d4ff; }
    .stAlert { background-color: #112244; border: 1px solid #00d4ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔬 AURA AI Labs")
st.markdown("### Practical Quantum Information & Bio-Systems Portal")
st.divider()

# Core Research Sections
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Fundamental Empirical Research")
    st.write("#### 1. Bio-Field Mapping (Aura Analysis)")
    st.write("Measurement of electromagnetic frequency emissions from biological systems as quantum oscillators.")
    
    st.write("#### 2. Wave-Particle Interaction")
    st.write("Experimental data on how human observation (The Observer Effect) influences quantum state collapses.")

with col2:
    st.info("System Calibration")
    st.metric(label="Quantum Resonance (Sync Rate)", value="200%", delta="Optimal")
    st.metric(label="Information Entropy", value="0.003", delta="Minimum", delta_color="inverse")

st.divider()
st.chat_input("Input parameters for AURA Frequency Analysis...")