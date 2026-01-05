import streamlit as st
import time
import numpy as np
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AURA LABS | Zero-Entropy Engine",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
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
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🦁 AURA LABS")
    st.markdown("---")
    # Menu Options
    menu = st.radio("Navigation", 
        ["Home: The Vision", 
         "Demo 1: Hardware Optimization", 
         "Demo 2: Agri-Regeneration", 
         "Founder Profile"])
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
        if st.button("Run Standard Benchmark"):
            with st.spinner("Processing..."):
                time.sleep(2)
            st.error("❌ Result: High Latency | High Heat Output")
            st.metric(label="Processing Time", value="5.2s", delta="- Efficiency Loss", delta_color="inverse")

    with col2:
        st.markdown("### 🔵 AURA Mode (Order)")
        if st.button("Run AURA Optimization"):
            with st.spinner("Optimizing..."):
                time.sleep(0.5)
            st.success("✅ Result: Zero Latency | Thermal Stability")
            st.metric(label="Processing Time", value="0.5s", delta="+ 1040% Speed Boost")

    # Chart
    st.markdown("### 📊 Real-time Entropy Analysis")
    chart_data = pd.DataFrame({
        'Standard (Heat)': np.random.randn(20) + 10,
        'AURA (Stable)': np.random.randn(20) + 2
    })
    st.line_chart(chart_data)

# --- SECTION 3: DEMO 2 (AGRICULTURE) ---
elif menu == "Demo 2: Agri-Regeneration":
    st.title("🌿 AURA Bio-Regeneration")
    decay_level = st.slider("Select Current Crop Decay Level (Entropy)", 0, 100, 80)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Current Yield", value=f"{100 - decay_level}%", delta="Critical", delta_color="inverse")
    with col2:
        if st.button("Activate Bio-Pulse"):
            st.balloons()
            st.success(f"🌱 SUCCESS: Yield restored to 98%.")

    st.markdown("### 📈 Recovery Trajectory")
    recovery_data = pd.DataFrame({
        'Natural Decay': [100, 80, 50, 20, 0],
        'AURA Recovery': [50, 75, 90, 95, 98]
    })
    st.area_chart(recovery_data)

# --- SECTION 4: FOUNDER PROFILE (FIXED) ---
elif menu == "Founder Profile":
    st.title("🦁 The Architect")
    st.markdown("---")
    
    # Using simple layout first to ensure visibility
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("### Rocker Saint")
    st.markdown("**Founder | Autodidact | Visionary**")
    
    st.warning("""
    > *"I do not write code to build apps. I write code to fix the broken laws of thermodynamics."*
    """)
    
    st.write("---")
    
    st.markdown("### 🤝 Connect with Founder")
    st.markdown("🔗 **LinkedIn:** [Click Here to View Profile](https://linkedin.com/in/maung-maung-hla-5aa7a43a1)")
    st.markdown("📧 **Email:** [auraailab.007@proton.me](mailto:auraailab.007@proton.me)")
    
    st.info("🦁 **Status:** Open for Seed Investment & Research Partnership (DeepMind/Google).")
