import streamlit as st
from pathlib import Path

from utility.session import authenticate_user

# Path untuk logo
DASHBOARD_DIR = Path(__file__).resolve().parents[1]
LOGO_TULISAN_PATH = DASHBOARD_DIR / "Asset" / "Logo tulisan (remove bg).png"


def show():
    # Center logo
    col1, col2, col3 = st.columns([1.5,2,1])
    with col2:
        if LOGO_TULISAN_PATH.exists():
            st.image(str(LOGO_TULISAN_PATH), width=500)
    
    st.write("")
    st.title("Login ABSA Insight")
    with st.form("login_form"):
        user = st.text_input("Username", key="login_username")
        pwd = st.text_input("Password", type="password", key="login_password")
        login_clicked = st.form_submit_button("Login", width="stretch")

    if login_clicked:
        if authenticate_user(user, pwd):
            st.session_state.login_status = True
            st.session_state.page = "Overview"
            st.success("✅ Login berhasil")
            st.rerun()
        else:
            st.error("❌ Username atau password salah")
