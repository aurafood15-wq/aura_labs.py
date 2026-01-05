import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="AURA Quantum System", page_icon="🌐", layout="wide")

# Styling
st.markdown("""
    <style>
    .main { background-color: #020617; color: #f1f5f9; }
    h1, h2, h3 { color: #60a5fa; }
    .stSidebar { background-color: #0f172a; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🧭 Navigation")
    page = st.radio("Go to:", ["Research Portal", "Categories", "About AURA"])
    st.divider()
    st.info("System Status: Online (200% Sync)")

# --- PAGE 1: RESEARCH PORTAL (HOME) ---
if page == "Research Portal":
    st.title("⚡ AURA Quantum System: Research Portal")
    st.subheader("Quantum Thermal Harvesting (QTH) Simulation")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("**Current Focus:** Converting Data Center Waste Heat to Energy")
        # LinkedIn data visualization
        data = {'Parameter': ['CPU Heat (°C)', 'Quantum Power (W)'], 'Value': [70.95, 5.86]}
        df = pd.DataFrame(data)
        st.bar_chart(df.set_index('Parameter'))
    with col2:
        st.metric("Thermal Threshold", "80°C", "Critical")
        st.metric("Sync Rate", "200%", "Optimal")

# --- PAGE 2: CATEGORIES ---
elif page == "Categories":
    st.title("📂 Research Categories")
    tab1, tab2, tab3 = st.tabs(["Quantum Energy", "AI Sustainability", "Bio-Information"])
    
    with tab1:
        st.subheader("Quantum Thermal Harvesting")
        st.write("Beyond Carnot limits research focusing on phonon-to-electron conversion.")
    with tab2:
        st.subheader("Circular Data Economy")
        st.write("Recycling thermal outputs for self-sustaining AI clusters.")
    with tab3:
        st.subheader("Aura Field Analysis")
        st.write("Analyzing biological electromagnetic signatures at the quantum level.")

# --- PAGE 3: ABOUT AURA ---
elif page == "About AURA":
    st.title("🔬 About AURA Quantum System")
    st.write("""
    **Mission:** To pioneer zero-waste energy systems using quantum mechanics.
    
    **History:** Built upon 20 years of empirical observations and advanced Python-based modeling. 
    AURA represents the bridge between classical physics and the future of quantum resource harvesting.
    """)
    st.divider()
    st.markdown("[Visit LinkedIn Profile for more updates](https://www.linkedin.com/in/maung-maung-hla-11a3b3105/)")
