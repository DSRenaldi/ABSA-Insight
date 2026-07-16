from pathlib import Path
import sqlite3

import streamlit as st


DASHBOARD_DIR = Path(__file__).resolve().parents[1]
DB_PATH = DASHBOARD_DIR / "Database" / "ABSA_insight.db"
LOGO_PATH = DASHBOARD_DIR / "Asset" / "Logo Gambar (remove bg).png"


st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght=400;600;800&display=swap" rel="stylesheet">
    <style>
    section[data-testid="stSidebar"] h1 {
        font-family: 'Poppins', sans-serif !important;
        font-size: 26px !important;
        font-weight: 650 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def init_session():
    if "login_status" not in st.session_state:
        st.session_state.login_status = False
    if "page" not in st.session_state:
        st.session_state.page = "Login"


def authenticate_user(username: str, password: str) -> bool:
    """Validasi kredensial menggunakan tabel user di database SQLite."""
    with sqlite3.connect(DB_PATH) as connection:
        result = connection.execute(
            """
            SELECT 1
            FROM user
            WHERE username = ? AND password = ?
            LIMIT 1
            """,
            (username, password),
        ).fetchone()

    return result is not None


def show_sidebar():
    if LOGO_PATH.exists():
        col1, col2, col3 = st.sidebar.columns([1, 2, 1])
        with col2:
            st.image(str(LOGO_PATH), width=150)

    st.sidebar.title("Menu Navigasi")

    if not st.session_state.login_status:
        st.sidebar.exception(Exception("Login terlebih dahulu🚨"))
        return

    page_options = [
        "Overview",
        "Analisis Aspek",
        "Sentiments & Aspects Trends",
        "Tabel Data Komentar",
        "Input Data",
    ]
    current_page = st.session_state.page if st.session_state.page in page_options else page_options[0]
    menu_desc = {
        "Overview": "Ringkasan utama sentimen dan aspek layanan.",
        "Analisis Aspek": "Analisis detail performa sentimen per aspek.",
        "Sentiments & Aspects Trends": "Tren sentimen dan aspek dari data user.",
        "Tabel Data Komentar": "Tabel komentar lengkap dan hasil segmentasi.",
        "Input Data": "Upload CSV dan uji komentar manual.",
    }

    for page in page_options:
        is_active = current_page == page
        active_class = " active" if is_active else ""
        st.sidebar.markdown(
            f'<div class="sidebar-menu-anchor{active_class}"></div>',
            unsafe_allow_html=True,
        )
        if st.sidebar.button(
            page,
            key=f"menu_{page}",
            type="primary" if is_active else "secondary",
            width="stretch",
        ):
            st.session_state.page = page
            st.rerun()
        if is_active:
            st.sidebar.markdown(
                f'<div class="menu-desc">{menu_desc[page]}</div>',
                unsafe_allow_html=True,
            )

    logout_clicked = st.sidebar.button("Logout", key="logout_btn", width="stretch")

    if logout_clicked:
        st.session_state.login_status = False
        st.rerun()
