import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RMS Approval Trend Dashboard",
    layout="wide"
)

# -----------------------------
# Data
# -----------------------------
quarterly = pd.DataFrame({
    "Period": ["Q1'26", "Q2'26", "Q3'26"],
    "Count": [1427, 1674, 264]
})

monthly = pd.DataFrame({
    "Period": [
        "Jan'26", "Feb'26", "Mar'26", "Apr'26", "May'26",
        "Jun'26", "Jul'26", "Aug'26", "Sep'26"
    ],
    "Count": [102, 1177, 148, 1287, 195, 220, 107, 79, 50]
})

weekly = pd.DataFrame({
    "Period": ["WW35", "WW36", "WW37", "WW38"],
    "Count": [3, 13, 27, 10]
})

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
    .main-title {
        background: #1f4e78;
        color: white;
        padding: 10px 15px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        border-radius: 4px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 12px;
        font-style: italic;
        margin-bottom: 15px;
    }

    .chart-title {
        text-align: center;
        font-size: 17px;
        font-weight: bold;
        margin: 5px 0 8px 0;
    }

    [data-testid="stMetricValue"] {
        font-size: 22px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">RMS APPROVAL — TREND DASHBOARD '
    '(Quarterly → Monthly → Weekly Drill-Down)</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Data as of 8-Sep-2026 | Analysis: '
    'Quarterly vs Monthly vs Weekly drill-down</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Top row
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        '<div class="chart-title">RMS Approval — Quarterly Trend</div>',
        unsafe_allow_html=True
    )

    st.bar_chart(
        quarterly.set_index("Period"),
        y="Count",
        height=320,
        use_container_width=True
    )

    st.dataframe(
        quarterly,
        hide_index=True,
        use_container_width=True
    )

with col2:
    st.markdown(
        '<div class="chart-title">RMS Approval — Monthly Trend</div>',
        unsafe_allow_html=True
    )

    st.bar_chart(
        monthly.set_index("Period"),
        y="Count",
        height=320,
        use_container_width=True
    )

    st.dataframe(
        monthly,
        hide_index=True,
        use_container_width=True
    )

# -----------------------------
# Bottom row
# -----------------------------
col3, col4 = st.columns(2)

with col3:
    st.markdown(
        '<div class="chart-title">RMS Approval — Weekly Trend</div>',
        unsafe_allow_html=True
    )

    st.bar_chart(
        weekly.set_index("Period"),
        y="Count",
        height=320,
        use_container_width=True
    )

    st.dataframe(
        weekly,
        hide_index=True,
        use_container_width=True
    )

with col4:
    st.markdown(
        '<div class="chart-title">RMS Approval — Quarterly / Monthly / WW</div>',
        unsafe_allow_html=True
    )

    combined = pd.concat([
        quarterly.assign(Level="Quarterly"),
        monthly.assign(Level="Monthly"),
        weekly.assign(Level="Weekly")
    ], ignore_index=True)

    # Create a compact combined table for Streamlit's native chart.
    combined_chart = combined.copy()
    combined_chart["Label"] = (
        combined_chart["Level"] + " - " + combined_chart["Period"]
    )

    st.bar_chart(
        combined_chart.set_index("Label"),
        y="Count",
        height=320,
        use_container_width=True
    )

    st.dataframe(
        combined,
        hide_index=True,
        use_container_width=True
    )

# -----------------------------
# Summary
# -----------------------------
st.markdown("---")
st.subheader("RMS Approval Summary")

a, b, c, d = st.columns(4)

with a:
    st.metric("Q1'26", f"{quarterly.loc[0, 'Count']:,}")

with b:
    st.metric("Q2'26", f"{quarterly.loc[1, 'Count']:,}")

with c:
    st.metric("Q3'26", f"{quarterly.loc[2, 'Count']:,}")

with d:
    st.metric("Weekly Peak", f"{weekly['Count'].max():,}")
