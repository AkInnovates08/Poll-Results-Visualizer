import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from src.data_processing import load_data, clean_data, explode_languages, get_language_counts, get_country_counts

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="Poll Results Visualizer", layout="wide")

# ==============================
# HEADER
# ==============================
st.markdown("<h1 style='text-align: center;'>📊 Poll Results Visualizer Dashboard</h1>", unsafe_allow_html=True)

st.markdown(
"""
This dashboard analyzes **Stack Overflow Developer Survey dataset**  
to understand developer preferences, trends, and insights.

📌 You can explore:
- Most popular programming languages  
- Country-wise participation  
- Distribution of responses  
"""
)

st.markdown("---")

# ==============================
# LOAD DATA
# ==============================
file_path = "data/survey_results_public.csv"

df = load_data(file_path)
df = clean_data(df)
df = explode_languages(df)

# ==============================
# SIDEBAR FILTER
# ==============================
st.sidebar.header("🔍 Filter Data")

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].unique().tolist())
)

if selected_country != "All":
    df = df[df["Country"] == selected_country]

# ==============================
# KPI SECTION
# ==============================
lang_counts = get_language_counts(df)
country_counts = get_country_counts(df)

col1, col2, col3 = st.columns(3)

col1.metric("👥 Total Responses", len(df))
col2.metric("🌍 Countries", df["Country"].nunique())
col3.metric("🔥 Top Language", lang_counts.idxmax())

st.markdown("---")

# ==============================
# DATA INFO SECTION
# ==============================
with st.expander("📄 About Dataset"):
    st.write("""
Dataset Used: Stack Overflow Developer Survey (Public Dataset)

Columns Used:
- Country → Respondent location  
- Age → Age group  
- LanguageHaveWorkedWith → Programming languages  

Note:
- Multi-select values are split into individual rows  
- Missing values are removed for clean analysis  
""")

# ==============================
# DATA PREVIEW
# ==============================
with st.expander("🔍 Preview Data"):
    st.dataframe(df.head(20))

# ==============================
# CHARTS SECTION
# ==============================

st.subheader("📊 Programming Language Analysis")

col4, col5 = st.columns(2)

# -------- BAR CHART --------
with col4:
    st.markdown("**Top 10 Programming Languages**")

    fig1, ax1 = plt.subplots(figsize=(8,5))

    lang_counts_top = lang_counts.head(10)

    sns.barplot(
        x=lang_counts_top.values,
        y=lang_counts_top.index,
        palette="viridis",
        ax=ax1
    )

    ax1.set_xlabel("Number of Developers")
    ax1.set_ylabel("Programming Language")

    st.pyplot(fig1)

# -------- PIE CHART --------
with col5:
    st.markdown("**Language Share (Top 5)**")

    top5 = lang_counts.head(5)

    fig2, ax2 = plt.subplots(figsize=(5,5))
    ax2.pie(
        top5,
        labels=top5.index,
        autopct='%1.1f%%',
        startangle=90
    )

    ax2.set_title("Language Distribution")

    st.pyplot(fig2)

st.markdown("---")

# ==============================
# COUNTRY ANALYSIS
# ==============================

st.subheader("🌍 Country-wise Participation")

fig3, ax3 = plt.subplots(figsize=(8,5))

sns.barplot(
    x=country_counts.values,
    y=country_counts.index,
    palette="coolwarm",
    ax=ax3
)

ax3.set_xlabel("Number of Responses")
ax3.set_ylabel("Country")

st.pyplot(fig3)

st.markdown("---")

# ==============================
# INSIGHTS
# ==============================

st.subheader("📈 Key Insights")

st.write(f"✔ The most popular programming language is **{lang_counts.idxmax()}**.")

st.write(f"✔ Total responses analyzed: **{len(df)}**.")

st.write(f"✔ The country with highest participation is **{country_counts.idxmax()}**.")

st.write("""
✔ This data shows strong trends in developer preferences  
✔ Useful for companies to understand technology demand  
✔ Helps in making data-driven decisions  
""")

# ==============================
# FOOTER
# ==============================

st.markdown("---")
st.markdown(
"<p style='text-align: center;'>Built using Python, Pandas, and Streamlit</p>",
unsafe_allow_html=True
)