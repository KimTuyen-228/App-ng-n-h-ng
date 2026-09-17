import streamlit as st
import pandas as pd

# ==========================================
# CẤU HÌNH ỨNG DỤNG
# ==========================================
st.set_page_config(
    page_title="Máy tính lãi suất",
    page_icon="💵",
    layout="wide"
)

# ==========================================
# TIÊU ĐỀ
# ==========================================
st.title("💵 MÁY TÍNH LÃI TIẾT KIỆM")

st.markdown("""
Ứng dụng giúp bạn tính toán và so sánh:
- 📌 Lãi đơn
- 📌 Lãi kép
- 📊 Chênh lệch tiền lãi
""")

st.divider()

# ==========================================
# NHẬP THÔNG TIN
# ==========================================
st.subheader("📋 Thông tin khoản tiền gửi")

col1, col2, col3 = st.columns(3)

with col1:
    tien_goc = st.number_input(
        "💰 Số tiền gửi (VNĐ)",
        min_value=1000,
        value=100_000_000,
        step=1_000_000,
        format="%d"
    )

with col2:
    lai_suat = st.number_input(
        "📈 Lãi suất (%/năm)",
        min_value=0.0,
        max_value=30.0,
        value=6.0,
        step=0.1
    )

with col3:
    so_thang = st.number_input(
        "📅 Thời gian gửi (tháng)",
        min_value=1,
        max_value=360,
        value=12,
        step=1
    )

# ==========================================
# TẦN SUẤT NHẬP LÃI
# ==========================================
tan_suat = st.selectbox(
    "🔄 Tần suất nhập lãi",
    [
        "Hàng tháng",
        "Hàng quý",
        "Hàng năm"
    ]
)

tan_suat_dict = {
    "Hàng tháng": 12,
    "Hàng quý": 4,
    "Hàng năm
