import streamlit as st
import pandas as pd
import numpy as np

# Page Identity & Theme
st.set_page_config(page_title="AURA Quantum System", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #020617; color: #f1f5f9; }
    .stMetric { background-color: #0f172a; padding: 15px; border-radius: 12px; border: 1px solid #3b82f6; }
    h1, h2, h3 { color: #60a5fa; }
    .stSidebar { background-color: #0f172a; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🧭 Navigation")
    page = st.radio("Go to:", ["Research Portal", "Categories", "The AURA Philosophy"])
    st.divider()
    st.info("System Status: Online (200% Sync)")
    st.write("Researcher: Maung Maung Hla")

# --- PAGE 1: RESEARCH PORTAL ---
if page == "Research Portal":
    st.title("⚡ AURA Quantum System: Research Portal")
    st.subheader("Quantum Thermal Harvesting (QTH) Simulation")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("**Current Focus:** Converting Data Center Waste Heat into usable Quantum Energy")
        # LinkedIn data visualization
        data = {'Parameter': ['CPU Heat (°C)', 'Quantum Power (W)'], 'Value': [70.95, 5.86]}
        df = pd.DataFrame(data)
        st.bar_chart(df.set_index('Parameter'))
        st.caption("Simulation Result: Demonstrating phonon-to-electron conversion at the 70.95°C threshold.")
    with col2:
        st.metric("Thermal Threshold", "80°C", "Critical")
        st.metric("Sync Rate", "200%", "Optimal")
        st.metric("Power Output", "5.86 W", "Harvested")

# --- PAGE 2: CATEGORIES ---
elif page == "Categories":
    st.title("📂 Strategic Research Domains")
    tab1, tab2, tab3 = st.tabs(["Quantum Energy", "AI Sustainability", "Bio-Information"])
    
    with tab1:
        st.subheader("Quantum Thermal Harvesting")
        st.write("Exploring ways to bypass classical thermodynamic limitations (Carnot Limits) using Quantum Tunneling.")
    with tab2:
        st.subheader("Circular Data Economy")
        st.write("Recycling the massive thermal output from AI clusters to create self-sustaining power loops.")
    with tab3:
        st.subheader("Aura Field Analysis")
        st.write("Measuring electromagnetic frequency emissions from biological systems as quantum oscillators.")

# --- PAGE 3: THE AURA PHILOSOPHY (About Us) ---
elif page == "The AURA Philosophy":
    st.title("🔬 The AURA Quantum Philosophy")
    st.markdown("### *'Harvesting the Invisible, Powering the Future'*")
    
    st.write("""
    **AURA Quantum System** represents 20 years of empirical research at the intersection of 
    Quantum Bio-Physics and high-efficiency energy systems. 
    
    Our core mission is to solve the world's energy crisis by looking into 
    **quantum thermal fluctuations** and **bio-electromagnetic resonances**.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Our Core Pillars")
        st.write("- **QTH Technology**: Bypassing Carnot limits via Phonon Harvesting.")
        st.write("- **Bio-Quantum Sync**: 200% Sync rate integration for biological monitoring.")
    with col2:
        st.subheader("The Research Goal")
        st.write("- **Zero-Waste**: Turning 80°C+ waste heat into sustainable power.")
        st.write("- **Circular Economy**: Self-sustaining AI and Data Clusters.")

    st.divider()
    st.markdown("[Connect with me on LinkedIn](https://www.linkedin.com/in/maung-maung-hla-11a3b3105/)")
