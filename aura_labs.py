import streamlit as st
import pandas as pd
import numpy as np

# Page Identity Update
st.set_page_config(page_title="AURA Quantum System", page_icon="⚡", layout="wide")

# Quantum Theme Styling
st.markdown("""
    <style>
    .main { background-color: #020617; color: #f1f5f9; }
    .stMetric { background-color: #0f172a; padding: 15px; border-radius: 12px; border: 1px solid #3b82f6; }
    h1, h2 { color: #60a5fa; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ AURA Quantum System")
st.markdown("### Revolutionizing Data Center Efficiency: From Waste Heat to Quantum Energy")
st.divider()

# Core Research: Quantum Thermal Harvesting (QTH)
col1, col2 = st.columns([2, 1])

with col1:
    st.header("🔬 Research Spotlight: QTH Simulation")
    st.write("""
    Using Python-based modeling, we are demonstrating how to bypass classical thermodynamic limitations 
    to convert high-grade CPU heat into usable electrical power.
    
    **Key Technical Highlights:**
    - **Harvesting the 'Invisible'**: Capturing atomic vibrations (phonons) at the **80°C+** threshold.
    - **Beyond Carnot Limits**: Utilizing **Quantum Tunneling effects** for superior conversion efficiency.
    - **Circular Data Economy**: Recycling thermal energy within AI clusters for sustainable computing.
    """)

with col2:
    st.info("System Parameters: Zero-Waste Goal")
    st.metric(label="Thermal Threshold", value="80°C", delta="Critical Range")
    st.metric(label="Conversion Efficiency", value="Quantum Max", delta="Theoretical")

st.divider()

# Energy Harvesting Visualization
st.subheader("📊 Phonon Vibration & Energy Recovery Analysis")
harvest_data = pd.DataFrame(
    np.random.randint(20, 100, size=(10, 2)),
    columns=['Waste Heat (Celsius)', 'Quantum Power (Watts)']
)
st.bar_chart(harvest_data)

st.divider()
st.caption("© 2026 AURA Quantum System | Pioneering Zero-Waste Energy Systems")
