import streamlit as st
import pandas as pd
import json

# Load JSON data
with open("analysis_results.json", "r") as file:
    raw_data = json.load(file)

# Extract redundancies into a DataFrame
data = pd.DataFrame(raw_data["redundancies"])

# Sidebar inputs
repo_url = st.sidebar.text_input("GitHub Repo URL")
similarity_threshold = st.sidebar.slider("Similarity Threshold", 0, 100, 80)

# Main page
st.title("Redundancy Detection Dashboard")

# Summary stats
st.metric("Total Redundant Pairs", len(data))
avg_similarity = data["similarity"].mean()
st.metric("Average Similarity Score", f"{avg_similarity:.2f}%")

# Filtered table
filtered_data = data[data["similarity"] >= similarity_threshold]
st.dataframe(filtered_data)

# Code comparison
st.subheader("Detailed Comparison")
for index, row in filtered_data.iterrows():
    st.text(f"File A: {row['file_a']}")
    st.text(f"File B: {row['file_b']}")
    st.code(row["code_a"], language="python")
    st.code(row["code_b"], language="python")
