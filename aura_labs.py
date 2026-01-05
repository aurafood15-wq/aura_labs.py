import streamlit as st
import time
import numpy as np
import pandas as pd

# --- PAGE CONFIGURATION (Scientist-Approved Style) ---
st.set_page_config(
    page_title="AURA LABS | Zero-Entropy Engine",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    h1 {
        color: #00FF99;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h2, h3 {
        color: #e0e0e0;
    }
    .stMetric {
        background-color: #1a1c24;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    a {
        color: #00FF99 !important;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🦁 AURA LABS")
    st.markdown("---")
    menu = st.radio("Navigation", ["Home: The Vision", "Demo 1: Hardware Optimization", "Demo 2: Agri-Regeneration", "Founder Profile"])
    st.markdown("---")
    st.caption("© 2026 AURA Inc. | Powered by Quantum Logic")

# --- SECTION 1: HOME (THE VISION) ---
if menu == "Home: The Vision":
    st.title("⚛️ Welcome to AURA LABS")
    st.subheader("Redefining Efficiency via Maxwell's Demon Logic")
    
    st.markdown("""
    ### The Core Problem: Entropy
    In every system—whether a **Data Center GPU** or a **Wheat Field**—energy is lost to chaos (Heat/Decay). 
    Traditional engineering fights this with more hardware. **AURA fights this with Information.**
    
    ### The Solution: The AURA Engine
    We utilize a **Quantum-inspired Observer Algorithm** that:
    1.  **Observes** micro-state fluctuations (thermal/biological).
    2.  **Predicts** entropy spikes before they occur.
    3.  **Reorders** the system to a Zero-Entropy State.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **For Tech:** Transforming Heat into Computational Power.")
    with col2:
        st.success("🌿 **For Agri:** Transforming Decay into Biological Yield.")

# --- SECTION 2: DEMO 1 (HARDWARE) ---
elif menu == "Demo 1: Hardware Optimization":
    st.title("💻 AURA Engine: Hardware Simulation")
    st.markdown("Comparing **Standard Linear Processing** vs. **AURA Quantum Batching**.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔴 Standard Mode (Chaos)")
        st.write("Simulating random electron flow & thermal throttling...")
        if st.button("Run Standard Benchmark"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulation Loop
            for i in range(100):
                time.sleep(0.05) # Slow processing
                progress_bar.progress(i + 1)
                status_text.text(f"Processing... CPU Temp: {50 + i/2:.1f}°C")
            
            st.error("❌ Result: High Latency | High Heat Output")
            st.metric(label="Processing Time", value="5.2s", delta="- Efficiency Loss", delta_color="inverse")

    with col2:
        st.markdown("### 🔵 AURA Mode (Order)")
        st.write("Activating Maxwell's Demon (Sorting Electron States)...")
        if st.button("Run AURA Optimization"):
            progress_bar_aura = st.progress(0)
            status_text_aura = st.empty()
            
            # Fast Simulation Loop
            for i in range(100):
                time.sleep(0.005) # Super fast
                progress_bar_aura.progress(i + 1)
                status_text_aura.text(f"Optimizing... CPU Temp: {45}°C (Stable)")
            
            st.success("✅ Result: Zero Latency | Thermal Stability")
            st.metric(label="Processing Time", value="0.5s", delta="+ 1040% Speed Boost")

    # Visualizing the Data (Simple Streamlit Chart)
    st.markdown("### 📊 Real-time Entropy Analysis")
    chart_data = pd.DataFrame({
        'Standard (Heat)': np.random.randn(20) + 10,
        'AURA (Stable)': np.random.randn(20) + 2
    })
    st.line_chart(chart_data)

# --- SECTION 3: DEMO 2 (AGRICULTURE) ---
elif menu == "Demo 2: Agri-Regeneration":
    st.title("🌿 AURA Bio-Regeneration")
    st.markdown("Applying Quantum Logic to Biological Systems to reverse decay.")
    
    # Interactive Slider
    decay_level = st.slider("Select Current Crop Decay Level (Entropy)", 0, 100, 80)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Current Yield Projection", value=f"{100 - decay_level}%", delta="Critical", delta_color="inverse")
        st.warning(f"⚠️ Warning: Crop death imminent due to high entropy ({decay_level}%).")
        
    with col2:
        # The Solution
        st.metric
